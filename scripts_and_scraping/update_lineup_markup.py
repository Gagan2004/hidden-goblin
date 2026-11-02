import re

with open('src/pages/HomePage.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Update lineup seats:
# Search for <li className="tp-lineup__seat" style={{ '--x': '...', ... '--i': '(\d+)' }}>
# <a aria-label="..." className="tp-lineup__pup" data-pup-friend="true" ...

pattern_pup = r'(<li className="tp-lineup__seat"[^>]*?\'--i\': \'(\d+)\'[^>]*?>\s*<a[^>]*?className="tp-lineup__pup"[^>]*?)(>)'

def repl_pup(match):
    prefix = match.group(1)
    i = match.group(2)
    # Check if already has data-state
    if 'onPointerEnter' in prefix:
        return match.group(0)
    extra = f' data-state={{hoveredSeat === {i} || randomPopSeat === {i} ? "pop" : undefined}} onPointerEnter={{() => setHoveredSeat({i})}} onPointerLeave={{() => setHoveredSeat(null)}} onFocus={{() => setHoveredSeat({i})}} onBlur={{() => setHoveredSeat(null)}}'
    return prefix + extra + match.group(3)

content = re.sub(pattern_pup, repl_pup, content)

# Update tags:
# <li className="tp-lineup__seat" style={{ '--x': '...', ... '--i': '(\d+)' }}><span className="tp-lineup__ghost"><span className="tp-lineup__name
pattern_tag = r'(<li className="tp-lineup__seat"[^>]*?\'--i\': \'(\d+)\'[^>]*?>\s*<span className="tp-lineup__ghost")'

def repl_tag(match):
    prefix = match.group(1)
    i = match.group(2)
    return f'{prefix} data-tag={{hoveredSeat === {i} || randomPopSeat === {i} ? "show" : undefined}}'

content = re.sub(pattern_tag, repl_tag, content)

with open('src/pages/HomePage.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated lineup pup and tag attributes')

