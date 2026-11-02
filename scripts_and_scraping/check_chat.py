with open('src/pages/HomePage.jsx', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('tp-chat__grid')
print('tp-chat length context:')
print(text[idx-100:idx+3500])

