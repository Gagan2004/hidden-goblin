from bs4 import BeautifulSoup
import json
import re

with open('scraped_pages/faq.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

faqs = []
# Find all note elements or question/answers
# Let's search for h2 or note elements
notes = soup.find_all(class_=lambda c: c and 'tp-note' in str(c))
print(f"tp-note elements found: {len(notes)}")

for n in notes:
    q = n.find(class_=lambda c: c and ('tp-note__q' in str(c) or 'question' in str(c))) or n.find('h2')
    a = n.find(class_=lambda c: c and ('tp-note__answer' in str(c) or 'tp-notes__a' in str(c) or 'answer' in str(c)))
    q_text = q.text.strip() if q else ''
    a_text = a.text.strip() if a else ''
    if q_text:
        faqs.append({'question': q_text, 'answer': a_text})

if not faqs:
    # search all h2
    for h2 in soup.find_all('h2'):
        q_text = h2.text.strip()
        # next sibling or parent sibling
        parent = h2.parent
        a_p = parent.find_all('p')
        a_text = ' '.join([p.text.strip() for p in a_p if p.text.strip() != q_text])
        faqs.append({'question': q_text, 'answer': a_text})

print(f"Extracted {len(faqs)} FAQs:")
for f in faqs:
    print("Q:", f['question'])
    print("A:", f['answer'][:100])
    print("---")

with open('extracted_faqs.json', 'w', encoding='utf-8') as f:
    json.dump(faqs, f, indent=2, ensure_ascii=False)

