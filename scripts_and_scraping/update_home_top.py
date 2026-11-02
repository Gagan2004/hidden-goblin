import re

with open('src/pages/HomePage.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update imports and state at top of HomePage
old_top = '''import React, { useState } from 'react';

export default function HomePage({ navigate, onWatchVideo }) {
  const [activeFaq, setActiveFaq] = useState(null);'''

new_top = '''import React, { useState, useEffect, useRef } from 'react';

export default function HomePage({ navigate, onWatchVideo }) {
  const [activeFaq, setActiveFaq] = useState(null);
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
  }, []);'''

content = content.replace(old_top, new_top, 1)

with open('src/pages/HomePage.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated HomePage top successfully')

