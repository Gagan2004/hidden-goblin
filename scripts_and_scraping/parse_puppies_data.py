import json
import re

with open('scraped_pages/puppies.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's inspect scripts containing "self.__next_f.push"
scripts = re.findall(r'self\.__next_f\.push\(\[1,"(.*?)"\]\)', content, re.DOTALL)
print(f"Found {len(scripts)} push scripts")

combined = ""
for s in scripts:
    # unescape string
    unescaped = s.encode('utf-8').decode('unicode_escape', errors='ignore')
    combined += unescaped

print(f"Combined unescaped length: {len(combined)}")

# Let's search for keywords like "maltipoo", "price", "breed", "available"
import re
# Look for json-like objects or arrays
matches = re.findall(r'\{[^{}]*"name"[^{}]*"breed"[^{}]*\}', combined)
print(f"Found {len(matches)} name+breed matches:")
for m in matches[:5]:
    print(" ", m[:150])

# Let's write the combined flight data to a file to inspect
with open('flight_puppies.txt', 'w', encoding='utf-8') as f:
    f.write(combined)
print("Saved flight_puppies.txt")

