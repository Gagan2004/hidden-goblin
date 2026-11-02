import re

with open('src/pages/HomePage.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update component header
old_head = """import React from 'react';

export default function HomePage({ navigate, onWatchVideo }) {"""

new_head = """import React, { useState, useEffect, useRef } from 'react';

export default function HomePage({ navigate, onWatchVideo }) {
  const [hoveredSeat, setHoveredSeat] = useState(null);
  const [randomPopSeat, setRandomPopSeat] = useState(null);
  const [chatStep, setChatStep] = useState(0);
  const [isTyping, setIsTyping] = useState(false);
  const chatStepsRef = useRef(null);

  // Lineup periodic random pop
  useEffect(() => {
    const timer = setInterval(() => {
      if (hoveredSeat === null) {
        const rand = Math.floor(Math.random() * 6);
        setRandomPopSeat(rand);
        setTimeout(() => setRandomPopSeat(null), 1200);
      }
    }, 3600);
    return () => clearInterval(timer);
  }, [hoveredSeat]);

  // Chat scroll observer
  useEffect(() => {
    const stepsEl = chatStepsRef.current;
    if (!stepsEl) return;
    const isMobile = window.innerWidth < 1024;
    if (isMobile) {
      setChatStep(2);
      return;
    }

    const children = Array.from(stepsEl.children);
    const io = new IntersectionObserver(
      (entries) => {
        for (const entry of entries) {
          if (entry.isIntersecting) {
            const idx = children.indexOf(entry.target);
            if (idx !== -1) {
              setChatStep((prev) => {
                if (idx > prev) {
                  setIsTyping(true);
                  setTimeout(() => setIsTyping(false), 750);
                }
                return idx;
              });
            }
          }
        }
      },
      { rootMargin: '-28% 0px -62% 0px', threshold: 0.1 }
    );

    children.forEach((c) => io.observe(c));
    return () => io.disconnect();
  }, []);"""

content = content.replace(old_head, new_head, 1)

# 2. Update lineup pups
for i in range(6):
    target = f"--i': '{i}'"
    # Find occurrence
    idx = content.find(target)
    if idx != -1:
        # Find next className="tp-lineup__pup"
        pup_idx = content.find('className="tp-lineup__pup"', idx)
        if pup_idx != -1 and pup_idx - idx < 200:
            replace_with = f'className="tp-lineup__pup" data-state={{hoveredSeat === {i} || randomPopSeat === {i} ? "pop" : undefined}} onPointerEnter={{() => setHoveredSeat({i})}} onPointerLeave={{() => setHoveredSeat(null)}} onFocus={{() => setHoveredSeat({i})}} onBlur={{() => setHoveredSeat(null)}}'
            content = content[:pup_idx] + replace_with + content[pup_idx + len('className="tp-lineup__pup"'):]

# 3. Update lineup tags
tags_idx = content.find('className="tp-lineup tp-lineup--tags"')
if tags_idx != -1:
    ghost_str = '<span className="tp-lineup__ghost"'
    curr = tags_idx
    for i in range(6):
        found = content.find(ghost_str, curr)
        if found != -1:
            repl = f'<span className="tp-lineup__ghost" data-tag={{hoveredSeat === {i} || randomPopSeat === {i} ? "show" : undefined}}'
            content = content[:found] + repl + content[found + len(ghost_str):]
            curr = found + len(repl)

# 4. Update chat section
content = content.replace('<ol className="tp-chat__steps">', '<ol ref={chatStepsRef} className="tp-chat__steps">', 1)

old_steps = '''<li className="tp-chat__step" data-done="true"><span aria-hidden="true" className="tp-chat__num font-plush">1</span><h3 className="font-plush tp-chat__title">Choose your breed</h3><p className="tp-chat__text">Select your preferred breed or tell us what you're looking for. We'll guide you based on availability and your lifestyle.</p></li><li className="tp-chat__step" data-done="true"><span aria-hidden="true" className="tp-chat__num font-plush">2</span><h3 className="font-plush tp-chat__title">Get photos & details</h3><p className="tp-chat__text">Our team will share real photos, health details, and all necessary information directly on WhatsApp.</p></li><li className="tp-chat__step" data-active="true"><span aria-hidden="true" className="tp-chat__num font-plush">3</span><h3 className="font-plush tp-chat__title">Secure & safe delivery</h3><p className="tp-chat__text">Once confirmed, we handle everything professionally and ensure your puppy reaches you safely and stress-free.</p></li>'''

new_steps = '''<li className="tp-chat__step" data-active={chatStep === 0 ? "true" : undefined} data-done={chatStep > 0 ? "true" : undefined}><span aria-hidden="true" className="tp-chat__num font-plush">1</span><h3 className="font-plush tp-chat__title">Choose your breed</h3><p className="tp-chat__text">Select your preferred breed or tell us what you're looking for. We'll guide you based on availability and your lifestyle.</p></li><li className="tp-chat__step" data-active={chatStep === 1 ? "true" : undefined} data-done={chatStep > 1 ? "true" : undefined}><span aria-hidden="true" className="tp-chat__num font-plush">2</span><h3 className="font-plush tp-chat__title">Get photos & details</h3><p className="tp-chat__text">Our team will share real photos, health details, and all necessary information directly on WhatsApp.</p></li><li className="tp-chat__step" data-active={chatStep === 2 ? "true" : undefined} data-done={chatStep > 2 ? "true" : undefined}><span aria-hidden="true" className="tp-chat__num font-plush">3</span><h3 className="font-plush tp-chat__title">Secure & safe delivery</h3><p className="tp-chat__text">Once confirmed, we handle everything professionally and ensure your puppy reaches you safely and stress-free.</p></li>'''

content = content.replace(old_steps, new_steps, 1)

content = content.replace(
    '<span className="tp-phone__status">online</span>',
    '<span className="tp-phone__status">{isTyping ? "typing..." : "online"}</span>',
    1
)

content = content.replace(
    '<div className="tp-msg-group" data-show="true" data-step="0">',
    '<div className="tp-msg-group" data-show={chatStep >= 0 && (!isTyping || chatStep !== 0) ? "true" : "false"} data-step="0">',
    1
)

content = content.replace(
    '<div className="tp-msg-group" data-show="true" data-step="1">',
    '<div className="tp-msg-group" data-show={chatStep >= 1 && (!isTyping || chatStep !== 1) ? "true" : "false"} data-step="1">',
    1
)

content = content.replace(
    '<div className="tp-msg-group" data-show="true" data-step="2">',
    '<div className="tp-msg-group" data-show={chatStep >= 2 && (!isTyping || chatStep !== 2) ? "true" : "false"} data-step="2">',
    1
)

typing_bubble = '''{isTyping && (
  <div className="tp-msg tp-msg--them animate-pulse" style={{ padding: '0.45rem 0.85rem', width: 'fit-content' }}>
    <span className="inline-flex items-center gap-1">
      <span className="w-1.5 h-1.5 rounded-full bg-[#2a170e]/70 animate-bounce" style={{ animationDuration: '0.6s' }}></span>
      <span className="w-1.5 h-1.5 rounded-full bg-[#2a170e]/70 animate-bounce" style={{ animationDuration: '0.6s', animationDelay: '0.15s' }}></span>
      <span className="w-1.5 h-1.5 rounded-full bg-[#2a170e]/70 animate-bounce" style={{ animationDuration: '0.6s', animationDelay: '0.3s' }}></span>
    </span>
  </div>
)}'''

content = content.replace(
    '<p className="tp-msg tp-msg--me">Hi TeddyPups! I\'d love to know more about your puppies.</p>',
    '<p className="tp-msg tp-msg--me">Hi TeddyPups! I\'d love to know more about your puppies.</p>' + typing_bubble,
    1
)

with open('src/pages/HomePage.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print('Applied all HomePage animations successfully!')

