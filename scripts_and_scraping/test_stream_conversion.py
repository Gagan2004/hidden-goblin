from bs4 import BeautifulSoup
from html_to_jsx_helper import html_to_jsx

with open('extracted_puppy_stream.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

stream_div = soup.find('div', id='S:0')
if stream_div:
    # First child is usually the container
    container = list(stream_div.children)[0]
    print("Container tag:", container.name, "class:", container.get('class'))
    jsx = html_to_jsx(str(container))
    print("Generated JSX length:", len(jsx))
    with open('puppy_detail_jsx_sample.jsx', 'w', encoding='utf-8') as out:
        out.write(jsx)
    print("Saved puppy_detail_jsx_sample.jsx")

