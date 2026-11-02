import subprocess

html_wrapper = """
<script>
window.addEventListener('load', () => {
  fetch('http://localhost:4173/').then(r => r.text()).then(html => {
    //
  });
});
</script>
"""

# Let's inspect rendered DOM of mobile homepage
chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
cmd = [chrome, '--headless=new', '--window-size=390,844', '--dump-dom', 'http://localhost:4173/']
res = subprocess.run(cmd, capture_output=True, text=True)

with open('mobile_dumped.html', 'w', encoding='utf-8') as f:
    f.write(res.stdout)

print("Dumped mobile html, size:", len(res.stdout))

# Check width and style in python
from bs4 import BeautifulSoup
soup = BeautifulSoup(res.stdout, 'html.parser')
header = soup.find('header')
print("Header classes:", header.get('class'))
print("Header inner div:", header.find('div').get('class'))

