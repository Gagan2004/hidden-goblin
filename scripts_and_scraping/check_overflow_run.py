import subprocess
import os

script = """
const docWidth = document.documentElement.clientWidth;
console.log('Document client width:', docWidth);
const elements = document.querySelectorAll('*');
let overflowing = [];
elements.forEach(el => {
  const rect = el.getBoundingClientRect();
  if (rect.right > docWidth + 2) {
    overflowing.push({
      tag: el.tagName,
      id: el.id,
      className: el.className,
      right: rect.right,
      width: rect.width
    });
  }
});
console.log('Total overflowing elements:', overflowing.length);
overflowing.slice(0, 10).forEach(o => console.log(JSON.stringify(o)));
"""

with open('check_overflow.js', 'w') as f:
    f.write(script)

# Run chrome headless and evaluate script
chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
cmd = [
    chrome,
    '--headless=new',
    '--window-size=390,844',
    '--disable-gpu',
    '--run-all-compositor-stages-before-draw',
    'http://localhost:4173/'
]

