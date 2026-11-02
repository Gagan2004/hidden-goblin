import React, { useEffect, useRef } from 'react';

export default function RevealScope({ children, className = '', ...props }) {
  const ref = useRef(null);

  useEffect(() => {
    let timer;
    const root = ref.current;
    if (!root) return;

    // Check prefers-reduced-motion
    const prefersReducedMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (prefersReducedMotion) {
      const revealAll = () => {
        root.querySelectorAll('[data-reveal]:not([data-revealed])').forEach((el) => {
          el.dataset.revealed = 'true';
        });
      };
      revealAll();
      const mo = new MutationObserver(revealAll);
      mo.observe(root, { childList: true, subtree: true });
      return () => mo.disconnect();
    }

    const pending = new Set();
    const isCurtainDown = () => {
      const state = document.querySelector('.tp-curtain')?.dataset.state;
      return state === 'intro' || state === 'covering' || state === 'covered' || state === 'snap';
    };

    const reveal = (el) => {
      el.dataset.revealed = 'true';
      io.unobserve(el);
    };

    const io = new IntersectionObserver(
      (entries) => {
        for (const entry of entries) {
          if (!entry.isIntersecting) continue;
          const el = entry.target;
          if (isCurtainDown()) {
            pending.add(el);
          } else {
            reveal(el);
          }
        }
      },
      { rootMargin: '0px 0px -6% 0px', threshold: 0.08 }
    );

    const arm = (el) => {
      if (el.dataset.armed) return io.observe(el);
      el.dataset.armed = 'true';
      const rect = el.getBoundingClientRect();
      if (rect.top < window.innerHeight && rect.bottom > 0 && !isCurtainDown()) {
        requestAnimationFrame(() => {
          el.dataset.revealed = 'true';
        });
        return;
      }
      io.observe(el);
    };

    root.querySelectorAll('[data-reveal]:not([data-revealed])').forEach(arm);

    const mo = new MutationObserver(() => {
      root.querySelectorAll('[data-reveal]:not([data-revealed])').forEach(arm);
    });
    mo.observe(root, { childList: true, subtree: true });

    const flushPending = () => {
      pending.forEach(reveal);
      pending.clear();
    };

    window.addEventListener('tp:arrived', flushPending);

    const checkCurtain = () => {
      if (isCurtainDown()) {
        timer = setTimeout(checkCurtain, 400);
      } else {
        flushPending();
      }
    };
    timer = setTimeout(checkCurtain, 1200);

    return () => {
      clearTimeout(timer);
      io.disconnect();
      mo.disconnect();
      window.removeEventListener('tp:arrived', flushPending);
    };
  }, []);

  return (
    <div ref={ref} className={className} {...props}>
      {children}
    </div>
  );
}

