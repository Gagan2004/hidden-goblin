import sys

with open('scripts_and_scraping/teddy_svg_jsx.txt', 'r', encoding='utf-8') as f:
    svg_jsx = f.read()

paw_path = "M32 30.5c-7.6 0-15.6 8.3-15.6 15.5 0 5.4 4.2 8.3 9.2 8.3 2.6 0 4.5-1.1 6.4-1.1s3.8 1.1 6.4 1.1c5 0 9.2-2.9 9.2-8.3 0-7.2-8-15.5-15.6-15.5zM14.6 22.3c-3 .1-5.6 3.3-5.6 7s2.6 6.9 5.6 6.9 5.6-3.2 5.6-6.9-2.6-7-5.6-7zM24.2 9.3c-3 0-5.6 3.3-5.6 7.3s2.5 7.3 5.6 7.3 5.6-3.3 5.6-7.3-2.5-7.3-5.6-7.3zM39.8 9.3c-3.1 0-5.6 3.3-5.6 7.3s2.5 7.3 5.6 7.3 5.6-3.3 5.6-7.3-2.5-7.3-5.6-7.3zM49.4 22.3c-3 0-5.6 3.3-5.6 7s2.6 6.9 5.6 6.9 5.6-3.2 5.6-6.9-2.6-7-5.6-7z"

component_code = f'''import React, {{ useEffect, useRef }} from 'react';

export default function PupJourney() {{
  const layerRef = useRef(null);
  const actorRef = useRef(null);
  const bodyRef = useRef(null);
  const bubbleRef = useRef(null);
  const bubbleAtRef = useRef(null);
  const printsRef = useRef(null);
  const probeRef = useRef(null);

  useEffect(() => {{
    // Check screen width and reduced motion
    const prefersReducedMotion =
      window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (prefersReducedMotion || window.innerWidth < 1024) {{
      return;
    }}

    const layer = layerRef.current;
    const actor = actorRef.current;
    const body = bodyRef.current;
    const bubble = bubbleRef.current;
    const bubbleAt = bubbleAtRef.current;
    const printsContainer = printsRef.current;

    if (!layer || !actor || !body || !printsContainer) return;

    const prints = Array.from(printsContainer.children);
    let printIdx = 0;

    // Enable live pup styling
    document.documentElement.dataset.pup = 'live';
    layer.hidden = false;

    let rafId;
    let lastScrollY = window.scrollY;
    let lastScrollTime = performance.now();
    let currentX = 0;
    let currentY = 0;
    let currentScale = 0.65;
    let facing = 1;
    let isMoving = false;
    let stopTimer = null;
    let bubbleTimer = null;
    let walkStep = 0;

    const say = (text, dur = 1800) => {{
      if (!bubble) return;
      bubble.textContent = text;
      bubble.dataset.show = 'true';
      clearTimeout(bubbleTimer);
      bubbleTimer = setTimeout(() => {{
        bubble.dataset.show = 'false';
      }}, dur);
    }};

    const spawnHearts = () => {{
      const rect = actor.getBoundingClientRect();
      for (let i = 0; i < 5; i++) {{
        const heart = document.createElement('span');
        heart.className = 'pup-heart';
        heart.textContent = '♥';
        heart.style.left = `${{rect.width * 0.5}}px`;
        heart.style.top = `${{rect.height * 0.25}}px`;
        actor.appendChild(heart);

        const offsetX = (Math.random() - 0.5) * 80;
        const offsetY = -60 - Math.random() * 50;

        heart
          .animate(
            [
              {{ transform: 'translate(-50%, 0) scale(0.4)', opacity: 0 }},
              {{ opacity: 1, offset: 0.2 }},
              {{
                transform: `translate(calc(-50% + ${{offsetX.toFixed(0)}}px), ${{offsetY.toFixed(0)}}px) scale(1.15)`,
                opacity: 0,
              }},
            ],
            {{
              duration: 1150 + 100 * i,
              delay: 75 * i,
              easing: 'cubic-bezier(.2,.7,.3,1)',
              fill: 'backwards',
            }}
          )
          .finished.then(
            () => heart.remove(),
            () => heart.remove()
          );
      }}
    }};

    const handleClick = () => {{
      const phrases = ['woof! ♡', 'peekaboo!', '*achoo!*', 'five more minutes?', 'I like you! ♡', 'coming!'];
      say(phrases[Math.floor(Math.random() * phrases.length)]);
      spawnHearts();
    }};

    actor.addEventListener('click', handleClick);

    const updatePhysics = () => {{
      const scrollY = window.scrollY;
      const now = performance.now();
      const deltaY = scrollY - lastScrollY;
      const dt = Math.max(1, now - lastScrollTime);

      lastScrollY = scrollY;
      lastScrollTime = now;

      // Find all candidate stops
      const stopElements = Array.from(document.querySelectorAll('[data-pup-stop]')).filter(
        (el) => el.getClientRects().length > 0
      );

      if (stopElements.length > 0) {{
        // Get absolute document coordinates of each stop
        const stops = stopElements.map((el) => {{
          const rect = el.getBoundingClientRect();
          return {{
            x: rect.left + rect.width / 2 - 150 * 0.65,
            y: rect.top, // relative to viewport
            screenY: rect.top,
            docY: rect.top + scrollY,
            scale: 0.65,
            facing: el.dataset.facing === 'left' ? -1 : 1,
            behind: el.dataset.behind === 'true',
          }};
        }});

        // Find which stops we are between
        let targetX = stops[0].x;
        let targetY = stops[0].y;
        let targetScale = stops[0].scale;
        let targetFacing = stops[0].facing;
        let front = !stops[0].behind;

        if (scrollY < 120) {{
          // At the hero booth
          targetX = stops[0].x;
          targetY = stops[0].y;
          targetScale = stops[0].scale;
          targetFacing = stops[0].facing;
          front = !stops[0].behind;
        }} else {{
          // Interpolate between stops or travel down the right lane
          const rightLaneX = window.innerWidth - 220;
          const targetScreenY = Math.min(window.innerHeight - 200, Math.max(120, window.innerHeight * 0.6));

          // Check if near any specific stop
          let nearest = null;
          let minDistance = Infinity;

          stops.forEach((s) => {{
            const dist = Math.abs(s.screenY - targetScreenY);
            if (dist < minDistance && dist < 180) {{
              minDistance = dist;
              nearest = s;
            }}
          }});

          if (nearest) {{
            const factor = 1 - minDistance / 180;
            targetX = rightLaneX * (1 - factor) + nearest.x * factor;
            targetY = nearest.y;
            targetFacing = nearest.facing;
            front = !nearest.behind;
          }} else {{
            targetX = rightLaneX;
            targetY = targetScreenY;
            targetFacing = deltaY >= 0 ? 1 : -1;
            front = true;
          }}
        }}

        // Smoothly interpolate current to target (spring/lerp)
        const lerpFactor = 0.14;
        currentX += (targetX - currentX) * lerpFactor;
        currentY += (targetY - currentY) * lerpFactor;
        currentScale += (targetScale - currentScale) * lerpFactor;

        if (Math.abs(deltaY) > 0.8) {{
          isMoving = true;
          facing = deltaY > 0 ? 1 : -1;
          walkStep += Math.abs(deltaY) * 0.08;

          // Paw print drop
          if (prints.length > 0 && Math.abs(deltaY) > 6 && Math.random() < 0.25) {{
            const p = prints[printIdx++ % prints.length];
            const px = currentX + (facing > 0 ? 140 : 60);
            const py = currentY + scrollY + 140;
            p.style.transform = `translate(${{px.toFixed(0)}}px, ${{py.toFixed(0)}}px) scale(1.1)`;
            p.animate(
              [
                {{ opacity: 0 }},
                {{ opacity: 0.5, offset: 0.1 }},
                {{ opacity: 0.5, offset: 0.5 }},
                {{ opacity: 0 }},
              ],
              {{ duration: 2400, easing: 'ease-out' }}
            );
          }}

          clearTimeout(stopTimer);
          stopTimer = setTimeout(() => {{
            isMoving = false;
            // If stopped for more than 2.6s, ask "coming?"
            stopTimer = setTimeout(() => {{
              if (!isMoving && window.scrollY > 400) {{
                say('coming?');
              }}
            }}, 2600);
          }}, 200);
        }}

        // Apply transforms
        layer.dataset.front = String(front);
        actor.style.transform = `translate3d(${{currentX.toFixed(2)}}px, ${{currentY.toFixed(2)}}px, 0)`;
        body.style.transform = `scale(${{currentScale.toFixed(4)}})`;

        // Leg walking cycle
        const frontLeg = body.querySelector('[data-p="ff"], [data-p="fn"]');
        const backLeg = body.querySelector('[data-p="bf"], [data-p="bn"]');
        const tail = body.querySelector('[data-p="tail"]');

        if (isMoving) {{
          const legAngle = Math.sin(walkStep) * 22;
          if (frontLeg) frontLeg.style.transform = `translate(168px, 192px) rotate(${{legAngle.toFixed(1)}}deg)`;
          if (backLeg) backLeg.style.transform = `translate(94px, 192px) rotate(${{(-legAngle).toFixed(1)}}deg)`;
          if (tail) tail.style.transform = `rotate(${{(Math.sin(walkStep * 2) * 16).toFixed(1)}}deg)`;
        }} else {{
          if (frontLeg) frontLeg.style.transform = 'translate(168px, 192px) rotate(0deg)';
          if (backLeg) backLeg.style.transform = 'translate(94px, 192px) rotate(0deg)';
          if (tail) tail.style.transform = 'rotate(0deg)';
        }}
      }}

      rafId = requestAnimationFrame(updatePhysics);
    }};

    rafId = requestAnimationFrame(updatePhysics);

    const handleResize = () => {{
      if (window.innerWidth < 1024) {{
        layer.hidden = true;
        delete document.documentElement.dataset.pup;
      }} else {{
        layer.hidden = false;
        document.documentElement.dataset.pup = 'live';
      }}
    }};

    window.addEventListener('resize', handleResize);

    return () => {{
      cancelAnimationFrame(rafId);
      clearTimeout(stopTimer);
      clearTimeout(bubbleTimer);
      delete document.documentElement.dataset.pup;
      if (layer) layer.hidden = true;
      actor.removeEventListener('click', handleClick);
      window.removeEventListener('resize', handleResize);
    }};
  }}, []);

  return (
    <>
      {{/* Probe */}}
      <div ref={{probeRef}} aria-hidden="true" className="pup-probe" />

      {{/* Floating Paw Prints */}}
      <div ref={{printsRef}} aria-hidden="true" className="pup-prints">
        {{Array.from({{ length: 24 }}, (_, a) => (
          <svg key={{a}} viewBox="0 0 64 64">
            <path d="{paw_path}" />
          </svg>
        ))}}
      </div>

      {{/* Floating Pup Companion Layer */}}
      <div ref={{layerRef}} aria-hidden="true" className="pup-layer" hidden data-front="true">
        <div ref={{actorRef}} className="pup-actor">
          <div ref={{bodyRef}} className="pup-actor__body">
            {svg_jsx}
          </div>
          <span ref={{bubbleAtRef}} className="pup-bubble-at">
            <span ref={{bubbleRef}} className="pup-bubble" data-show="false" />
          </span>
        </div>
      </div>
    </>
  );
}}
'''

with open('src/components/PupJourney.jsx', 'w', encoding='utf-8') as out:
    out.write(component_code)

print('Generated PupJourney.jsx successfully! Length:', len(component_code))

