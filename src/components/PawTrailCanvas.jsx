import React, { useEffect, useRef } from 'react';

function createPawPath() {
  function ellipsePath(cx, cy, rx, ry, deg) {
    const rad = (deg * Math.PI) / 180;
    const cos = Math.cos(rad);
    const sin = Math.sin(rad);
    const pt = (x, y) => `${(cx + x * cos - y * sin).toFixed(2)} ${(cy + x * sin + y * cos).toFixed(2)}`;
    return `M${pt(rx, 0)}C${pt(rx, 0.5523 * ry)} ${pt(0.5523 * rx, ry)} ${pt(0, ry)}C${pt(-0.5523 * rx, ry)} ${pt(-rx, 0.5523 * ry)} ${pt(-rx, 0)}C${pt(-rx, -0.5523 * ry)} ${pt(-0.5523 * rx, -ry)} ${pt(0, -ry)}C${pt(0.5523 * rx, -ry)} ${pt(rx, -0.5523 * ry)} ${pt(rx, 0)}Z`;
  }

  return (
    'M32 30.5c-7.6 0-15.6 8.3-15.6 15.5 0 5.4 4.2 8.3 9.2 8.3 2.6 0 4.5-1.1 6.4-1.1s3.8 1.1 6.4 1.1c5 0 9.2-2.9 9.2-8.3 0-7.2-8-15.5-15.6-15.5z' +
    ellipsePath(14.6, 29.2, 5.3, 6.9, -28) +
    ellipsePath(24.2, 16.6, 5.5, 7.3, -10) +
    ellipsePath(39.8, 16.6, 5.5, 7.3, 10) +
    ellipsePath(49.4, 29.2, 5.3, 6.9, 28)
  );
}

export default function PawTrailCanvas() {
  const canvasRef = useRef(null);

  useEffect(() => {
    // Only enable on devices with fine pointer (mouse/trackpad) and when reduced motion is not preferred
    const prefersReducedMotion =
      window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    const hasFinePointer =
      window.matchMedia && window.matchMedia('(hover: hover) and (pointer: fine)').matches;

    if (prefersReducedMotion || !hasFinePointer) return;

    const canvas = canvasRef.current;
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    const pawPath = new Path2D(createPawPath());
    const prints = [];
    let dpr = 1;
    let rafId = 0;
    let isAnimating = false;
    let lastX = NaN;
    let lastY = NaN;
    let dist = 0;
    let pawSide = 1;

    const resize = () => {
      dpr = Math.min(window.devicePixelRatio || 1, 2);
      canvas.width = window.innerWidth * dpr;
      canvas.height = window.innerHeight * dpr;
    };

    resize();

    const render = (time) => {
      ctx.setTransform(1, 0, 0, 1, 0, 0);
      ctx.clearRect(0, 0, canvas.width, canvas.height);

      for (let i = prints.length - 1; i >= 0; i--) {
        const p = prints[i];
        const age = time - p.born;

        if (age > 1000) {
          prints.splice(i, 1);
          continue;
        }

        const fade = age < 600 ? 1 : 1 - (age - 600) / 400;
        ctx.globalAlpha = 0.42 * fade * fade;
        ctx.setTransform(0.27 * dpr, 0, 0, 0.27 * dpr, p.x * dpr, p.y * dpr);
        ctx.rotate(p.angle);
        ctx.translate(-32, -34);
        ctx.fillStyle = '#c2622b';
        ctx.fill(pawPath);
      }

      if (prints.length > 0) {
        rafId = requestAnimationFrame(render);
      } else {
        isAnimating = false;
      }
    };

    const handlePointerMove = (e) => {
      if (e.pointerType !== 'mouse') return;

      if (Number.isNaN(lastX)) {
        lastX = e.clientX;
        lastY = e.clientY;
        return;
      }

      const dx = e.clientX - lastX;
      const dy = e.clientY - lastY;
      dist += Math.hypot(dx, dy);

      if (dist >= 46) {
        dist = 0;
        const angle = Math.atan2(dy, dx) + Math.PI / 2;
        pawSide = -pawSide;
        const sideOffset = 7 * pawSide;

        prints.push({
          x: e.clientX + Math.cos(angle) * sideOffset + 14,
          y: e.clientY + Math.sin(angle) * sideOffset + 16,
          angle,
          born: performance.now(),
        });

        if (prints.length > 14) {
          prints.shift();
        }

        if (!isAnimating) {
          isAnimating = true;
          rafId = requestAnimationFrame(render);
        }
      }

      lastX = e.clientX;
      lastY = e.clientY;
    };

    window.addEventListener('pointermove', handlePointerMove, { passive: true });
    window.addEventListener('resize', resize);

    return () => {
      window.removeEventListener('pointermove', handlePointerMove);
      window.removeEventListener('resize', resize);
      cancelAnimationFrame(rafId);
      if (ctx && canvas) {
        ctx.setTransform(1, 0, 0, 1, 0, 0);
        ctx.clearRect(0, 0, canvas.width, canvas.height);
      }
    };
  }, []);

  return (
    <canvas
      ref={canvasRef}
      aria-hidden="true"
      className="pointer-events-none fixed inset-0 z-[70] size-full"
    />
  );
}

