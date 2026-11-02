import React, { useEffect, useRef, useId } from 'react';

export default function Flight({ photo, label }) {
  const containerRef = useRef(null);
  const routePathRef = useRef(null);
  const planeGroupRef = useRef(null);
  const clipId = useId();

  useEffect(() => {
    const prefersReducedMotion =
      typeof window !== 'undefined' &&
      window.matchMedia &&
      window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    const updatePlane = (progress) => {
      const path = routePathRef.current;
      const plane = planeGroupRef.current;
      if (!path || !plane) return;

      const r = path.getTotalLength();
      if (!r) return;
      const l = Math.min(r, Math.max(0, progress * r));
      const n = path.getPointAtLength(l);
      const i = path.getPointAtLength(Math.min(r, l + 1));
      const a = path.getPointAtLength(Math.max(0, l - 1));
      const o = (180 * Math.atan2(i.y - a.y, i.x - a.x)) / Math.PI;

      plane.setAttribute('transform', `translate(${n.x.toFixed(1)} ${n.y.toFixed(1)}) rotate(${o.toFixed(1)})`);
      plane.style.opacity = String(Math.min(1, Math.max(0, (progress - 0.11) / 0.06)));
    };

    const onScroll = () => {
      if (prefersReducedMotion) {
        updatePlane(0.62);
        return;
      }

      const container = containerRef.current;
      if (!container) return;

      const rect = container.getBoundingClientRect();
      const containerTop = rect.top + window.scrollY;
      const containerHeight = rect.height;

      // offset: ["start 95%", "end 25%"]
      const startY = containerTop - window.innerHeight * 0.95;
      const endY = containerTop + containerHeight - window.innerHeight * 0.25;
      const totalRange = endY - startY;

      let progress = 0;
      if (totalRange > 0) {
        progress = Math.min(1, Math.max(0, (window.scrollY - startY) / totalRange));
      }
      updatePlane(progress);
    };

    onScroll();

    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', onScroll);

    let unsubLenis;
    if (window.lenis && typeof window.lenis.on === 'function') {
      unsubLenis = window.lenis.on('scroll', onScroll);
    }

    return () => {
      window.removeEventListener('scroll', onScroll);
      window.removeEventListener('resize', onScroll);
      if (unsubLenis) unsubLenis();
    };
  }, []);

  return (
    <div ref={containerRef} className="tp-flight">
      <svg aria-label={label || 'A plane flying puppies from Korea to Dubai'} role="img" viewBox="0 0 660 300">
        <defs>
          <clipPath id={clipId}>
            <circle r="25" />
          </clipPath>
        </defs>
        <path ref={routePathRef} className="tp-flight__route" d="M40 250 C 170 40, 470 20, 620 168" />
        <circle className="tp-flight__dot" cx="40" cy="250" r="7" />
        <circle className="tp-flight__dot" cx="620" cy="168" r="7" />
        <text className="tp-flight__label" textAnchor="middle" x="40" y="284">Korea</text>
        <text className="tp-flight__label" textAnchor="middle" x="620" y="202">Dubai</text>
        <g ref={planeGroupRef} transform="translate(410 70)">
          <g transform="translate(-126 -78)">
            <path className="tp-flight__wing" d="M28 60 L8 26 L34 26 L60 54 Z" />
            <path className="tp-flight__wing tp-flight__wing--far" d="M108 112 L142 156 L172 156 L158 112 Z" />
            <path className="tp-flight__body" d="M20 80 C20 52 52 44 80 44 L168 44 C200 44 224 60 232 80 C224 100 200 112 168 112 L80 112 C52 112 20 104 20 80 Z" />
            <path className="tp-flight__wing" d="M104 44 L138 2 L168 2 L154 44 Z" />
            <path className="tp-flight__line" d="M206 64 C215 67 221 73 224 80" />
          </g>
          {photo && (
            <g transform="translate(10 2)">
              <image href={photo} x="-25" y="-25" width="50" height="50" clipPath={`url(#${clipId})`} preserveAspectRatio="xMidYMid slice" />
              <circle r="25" className="tp-flight__porthole" />
            </g>
          )}
        </g>
      </svg>
    </div>
  );
}
