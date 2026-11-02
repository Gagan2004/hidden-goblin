with open('scripts_and_scraping/scraped_puppies/maltipoo-max-male.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('hidden id="S:0"')
print("Found S:0 at", idx)
if idx != -1:
    end_idx = c.find('</div>', idx)
    # The actual content is between <div hidden id="S:0"> and the matching closing </div>
    # Let's see the length
    print("Streamed content length:", len(c[idx:]))
    with open('extracted_puppy_stream.html', 'w', encoding='utf-8') as out:
        out.write(c[idx:])
    print("Saved extracted_puppy_stream.html")

