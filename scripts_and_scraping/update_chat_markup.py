import re

with open('src/pages/HomePage.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add ref to tp-chat__steps
content = content.replace('<ol className="tp-chat__steps">', '<ol ref={chatStepsRef} className="tp-chat__steps">', 1)

# 2. Update steps data-active and data-done
old_steps = '''<li className="tp-chat__step" data-done="true"><span aria-hidden="true" className="tp-chat__num font-plush">1</span><h3 className="font-plush tp-chat__title">Choose your breed</h3><p className="tp-chat__text">Select your preferred breed or tell us what you're looking for. We'll guide you based on availability and your lifestyle.</p></li><li className="tp-chat__step" data-done="true"><span aria-hidden="true" className="tp-chat__num font-plush">2</span><h3 className="font-plush tp-chat__title">Get photos & details</h3><p className="tp-chat__text">Our team will share real photos, health details, and all necessary information directly on WhatsApp.</p></li><li className="tp-chat__step" data-active="true"><span aria-hidden="true" className="tp-chat__num font-plush">3</span><h3 className="font-plush tp-chat__title">Secure & safe delivery</h3><p className="tp-chat__text">Once confirmed, we handle everything professionally and ensure your puppy reaches you safely and stress-free.</p></li>'''

new_steps = '''<li className="tp-chat__step" data-active={chatStep === 0 ? "true" : undefined} data-done={chatStep > 0 ? "true" : undefined}><span aria-hidden="true" className="tp-chat__num font-plush">1</span><h3 className="font-plush tp-chat__title">Choose your breed</h3><p className="tp-chat__text">Select your preferred breed or tell us what you're looking for. We'll guide you based on availability and your lifestyle.</p></li><li className="tp-chat__step" data-active={chatStep === 1 ? "true" : undefined} data-done={chatStep > 1 ? "true" : undefined}><span aria-hidden="true" className="tp-chat__num font-plush">2</span><h3 className="font-plush tp-chat__title">Get photos & details</h3><p className="tp-chat__text">Our team will share real photos, health details, and all necessary information directly on WhatsApp.</p></li><li className="tp-chat__step" data-active={chatStep === 2 ? "true" : undefined} data-done={chatStep > 2 ? "true" : undefined}><span aria-hidden="true" className="tp-chat__num font-plush">3</span><h3 className="font-plush tp-chat__title">Secure & safe delivery</h3><p className="tp-chat__text">Once confirmed, we handle everything professionally and ensure your puppy reaches you safely and stress-free.</p></li>'''

content = content.replace(old_steps, new_steps, 1)

# 3. Update status
content = content.replace(
    '<span className="tp-phone__status">online</span>',
    '<span className="tp-phone__status">{isTyping ? "typing..." : "online"}</span>',
    1
)

# 4. Update msg groups
content = content.replace(
    '<div className="tp-msg-group" data-show="true" data-step="0">',
    '<div className="tp-msg-group" data-show={chatStep >= 0 && (!isTyping || chatStep !== 0) ? "true" : "false"} data-step="0">',
    1
)

content = content.replace(
    '<div className="tp-msg-group" data-show="true" data-step="1">',
    '<div className="tp-msg-group" data-show={chatStep >= 1 && (!isTyping || chatStep !== 1) ? "true" : "false"} data-step="1">',
    1
)

content = content.replace(
    '<div className="tp-msg-group" data-show="true" data-step="2">',
    '<div className="tp-msg-group" data-show={chatStep >= 2 && (!isTyping || chatStep !== 2) ? "true" : "false"} data-step="2">',
    1
)

# 5. Insert typing bubble right inside .tp-phone__screen
typing_bubble = '''{isTyping && (
  <div className="tp-msg tp-msg--them animate-pulse" style={{ padding: '0.45rem 0.85rem', width: 'fit-content' }}>
    <span className="inline-flex items-center gap-1">
      <span className="w-1.5 h-1.5 rounded-full bg-[#2a170e]/70 animate-bounce" style={{ animationDuration: '0.6s' }}></span>
      <span className="w-1.5 h-1.5 rounded-full bg-[#2a170e]/70 animate-bounce" style={{ animationDuration: '0.6s', animationDelay: '0.15s' }}></span>
      <span className="w-1.5 h-1.5 rounded-full bg-[#2a170e]/70 animate-bounce" style={{ animationDuration: '0.6s', animationDelay: '0.3s' }}></span>
    </span>
  </div>
)}'''

content = content.replace(
    '<p className="tp-msg tp-msg--me">Hi TeddyPups! I\'d love to know more about your puppies.</p>',
    '<p className="tp-msg tp-msg--me">Hi TeddyPups! I\'d love to know more about your puppies.</p>' + typing_bubble,
    1
)

with open('src/pages/HomePage.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated chat markup successfully')

