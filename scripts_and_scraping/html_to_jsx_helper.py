import re
import urllib.parse
from bs4 import BeautifulSoup, Comment

VOID_TAGS = {'input', 'img', 'br', 'hr', 'area', 'base', 'col', 'embed', 'source', 'track', 'wbr', 'path', 'circle', 'rect', 'ellipse', 'polygon', 'polyline', 'line', 'stop', 'use'}

def clean_image_url(url):
    if not url:
        return ''
    if '/_next/image?url=' in url:
        parsed = urllib.parse.urlparse(url)
        qs = urllib.parse.parse_qs(parsed.query)
        if 'url' in qs:
            return qs['url'][0]
    return url

def convert_style_to_jsx(style_str):
    if not style_str:
        return None
    # e.g. "position:absolute;height:100%;width:100%;--x:9%"
    parts = [p.strip() for p in style_str.split(';') if p.strip()]
    props = []
    for part in parts:
        if ':' not in part:
            continue
        k, v = part.split(':', 1)
        k = k.strip()
        v = v.strip().replace('"', '\\"')
        if k.startswith('--'):
            props.append(f"'{k}': '{v}'")
        else:
            camel = re.sub(r'-([a-z])', lambda m: m.group(1).upper(), k)
            props.append(f"{camel}: '{v}'")
    return "{{ " + ", ".join(props) + " }}"

def node_to_jsx(tag):
    if isinstance(tag, Comment):
        return ''
    if isinstance(tag, str):
        # Text node: escape curly braces
        t = str(tag)
        # In JSX, curly braces must be escaped as {'{'} or {'}'}
        t = t.replace('{', "{'{'}").replace('}', "{'}'}")
        return t

    # Handle tags to skip
    if tag.name in ['script', 'noscript', 'template']:
        return ''

    tag_name = tag.name

    # Build attributes
    attrs = []
    has_navigate = False
    nav_href = None

    for attr_name, attr_val in list(tag.attrs.items()):
        # Handle class -> className
        if attr_name == 'class':
            val_str = ' '.join(attr_val) if isinstance(attr_val, list) else str(attr_val)
            attrs.append(f'className="{val_str}"')
            continue

        # Handle for -> htmlFor
        if attr_name == 'for':
            attrs.append(f'htmlFor="{attr_val}"')
            continue

        # Handle style
        if attr_name == 'style':
            jsx_style = convert_style_to_jsx(attr_val)
            if jsx_style:
                attrs.append(f'style={jsx_style}')
            continue

        # Handle src on img
        if tag_name == 'img' and attr_name == 'src':
            clean_src = clean_image_url(attr_val)
            attrs.append(f'src="{clean_src}"')
            continue

        # Skip Next.js specific image attributes
        if tag_name == 'img' and attr_name in ['srcset', 'sizes', 'loading', 'decoding', 'data-nimg']:
            continue

        # Handle internal href on <a>
        if tag_name == 'a' and attr_name == 'href':
            if attr_val.startswith('/') and not attr_val.startswith('//'):
                has_navigate = True
                nav_href = attr_val
                attrs.append(f'href="{attr_val}"')
                continue

        # CamelCase SVG and standard attributes
        attr_map = {
            'viewbox': 'viewBox',
            'fill-rule': 'fillRule',
            'clip-rule': 'clipRule',
            'stroke-width': 'strokeWidth',
            'stroke-linecap': 'strokeLinecap',
            'stroke-linejoin': 'strokeLinejoin',
            'stroke-dasharray': 'strokeDasharray',
            'stroke-dashoffset': 'strokeDashoffset',
            'clip-path': 'clipPath',
            'fetchpriority': 'fetchPriority',
            'patternunits': 'patternUnits',
            'patterncontentunits': 'patternContentUnits',
            'preserveaspectratio': 'preserveAspectRatio',
            'stop-color': 'stopColor',
            'stop-opacity': 'stopOpacity',
            'xlink:href': 'xlinkHref',
            'tabindex': 'tabIndex',
            'autocomplete': 'autoComplete',
            'autofocus': 'autoFocus',
        }
        react_attr = attr_map.get(attr_name.lower(), attr_name)

        if isinstance(attr_val, list):
            val_str = ' '.join(attr_val)
        elif isinstance(attr_val, bool):
            attrs.append(f'{react_attr}' if attr_val else '')
            continue
        else:
            val_str = str(attr_val).replace('"', '&quot;')

        attrs.append(f'{react_attr}="{val_str}"')

    if has_navigate and nav_href:
        attrs.append(f'onClick={{(e) => {{ e.preventDefault(); navigate("{nav_href}"); }}}}')

    attr_str = (' ' + ' '.join([a for a in attrs if a])) if attrs else ''

    if tag_name in VOID_TAGS:
        return f'<{tag_name}{attr_str} />'

    # Recursively render children
    children_jsx = ''.join(node_to_jsx(c) for c in tag.children)
    return f'<{tag_name}{attr_str}>{children_jsx}</{tag_name}>'

def html_to_jsx(html_string):
    soup = BeautifulSoup(html_string, 'html.parser')
    for comment in soup.find_all(text=lambda text: isinstance(text, Comment)):
        comment.extract()
    for tag in soup.find_all(class_=lambda c: c and any(x in c for x in ['pup-probe', 'pup-prints', 'pup-layer'])):
        tag.decompose()
    top_tags = [c for c in soup.children if not isinstance(c, Comment) and str(c).strip()]
    if len(top_tags) == 1 and hasattr(top_tags[0], 'name') and top_tags[0].name:
        return node_to_jsx(top_tags[0])
    return f"<div>{''.join(node_to_jsx(c) for c in top_tags)}</div>"

