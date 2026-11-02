import { useEffect } from 'react';

export default function useTeddyInteractivity() {
  useEffect(() => {
    const phrases = [
      'woof! ♡',
      'peekaboo!',
      '*achoo!*',
      'ready for cuddles!',
      'five more minutes?',
      'home soon! ♡',
      'best friend forever!'
    ];

    const spawnHearts = (container) => {
      const rect = container.getBoundingClientRect();
      for (let i = 0; i < 5; i++) {
        const heart = document.createElement('span');
        heart.className = 'pup-heart';
        heart.textContent = '♥';
        heart.style.left = `${rect.width * 0.55}px`;
        heart.style.top = `${rect.height * 0.28}px`;
        container.appendChild(heart);

        const offsetX = (Math.random() - 0.5) * 90;
        const offsetY = -70 - Math.random() * 60;

        heart
          .animate(
            [
              { transform: 'translate(-50%, 0) scale(0.4)', opacity: 0 },
              { opacity: 1, offset: 0.2 },
              {
                transform: `translate(calc(-50% + ${offsetX.toFixed(0)}px), ${offsetY.toFixed(0)}px) scale(1.15)`,
                opacity: 0
              }
            ],
            {
              duration: 1150 + 110 * i,
              delay: 80 * i,
              easing: 'cubic-bezier(.2,.7,.3,1)',
              fill: 'backwards'
            }
          )
          .finished.then(
            () => heart.remove(),
            () => heart.remove()
          );
      }
    };

    const handleClick = (e) => {
      const buddy = e.target.closest('.pup-buddy, [data-pup-stop]');
      if (!buddy) return;

      const targetBuddy = buddy.classList.contains('pup-buddy')
        ? buddy
        : buddy.querySelector('.pup-buddy') || buddy;

      // Ensure data-live is set so styling applies
      targetBuddy.setAttribute('data-live', '');
      targetBuddy.setAttribute('data-playing', 'true');

      // Speech bubble
      let bubble = targetBuddy.querySelector('.pup-bubble');
      if (!bubble) {
        bubble = document.createElement('span');
        bubble.className = 'pup-bubble';
        bubble.setAttribute('aria-hidden', 'true');
        targetBuddy.appendChild(bubble);
      }

      const randomPhrase = phrases[Math.floor(Math.random() * phrases.length)];
      bubble.textContent = randomPhrase;
      bubble.dataset.show = 'true';

      if (targetBuddy._bubbleTimer) clearTimeout(targetBuddy._bubbleTimer);
      targetBuddy._bubbleTimer = setTimeout(() => {
        bubble.dataset.show = 'false';
        targetBuddy.removeAttribute('data-playing');
      }, 1800);

      // Spawn hearts
      spawnHearts(targetBuddy);
    };

    // Subtle eye cursor tracking on desktop
    const handlePointerMove = (e) => {
      if (e.pointerType !== 'mouse') return;
      const buddies = document.querySelectorAll('.pup-buddy');
      buddies.forEach((buddy) => {
        if (buddy.closest('.tp-basket__pup')) return;
        buddy.setAttribute('data-live', '');
        const eyes = buddy.querySelector('[data-p="eyes"]');
        if (!eyes) return;

        const rect = buddy.getBoundingClientRect();
        if (
          rect.top > window.innerHeight ||
          rect.bottom < 0 ||
          rect.left > window.innerWidth ||
          rect.right < 0
        ) {
          return;
        }

        const eyeCenterX = rect.left + rect.width * 0.7;
        const eyeCenterY = rect.top + rect.height * 0.45;
        const dx = Math.max(-4, Math.min(4, (e.clientX - eyeCenterX) * 0.02));
        const dy = Math.max(-3, Math.min(3, (e.clientY - eyeCenterY) * 0.02));

        eyes.style.transform = `translate(${dx.toFixed(1)}px, ${dy.toFixed(1)}px)`;
      });
    };

    // Ensure non-basket buddies have data-live on mount
    document.querySelectorAll('.pup-buddy').forEach((b) => {
      if (!b.closest('.tp-basket__pup')) {
        b.setAttribute('data-live', '');
      }
    });

    document.addEventListener('click', handleClick);
    window.addEventListener('pointermove', handlePointerMove, { passive: true });

    return () => {
      document.removeEventListener('click', handleClick);
      window.removeEventListener('pointermove', handlePointerMove);
    };
  }, []);
}

