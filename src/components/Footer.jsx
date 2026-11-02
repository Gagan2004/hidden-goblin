import React from 'react';

export default function Footer({ navigate }) {
  const handleNav = (path) => {
    navigate(path);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  return (
    <footer className="tp-footer relative bg-[#2a170e] text-[#fffdf8] pt-16 pb-24 md:pb-12 overflow-hidden">
      {/* Decorative Twinkling Stars Sky */}
      <div aria-hidden="true" className="pointer-events-none absolute inset-0">
        <svg viewBox="0 0 40 40" className="tp-twinkle absolute text-honey" style={{ left: '6%', top: '18%', width: '12.6px', animationDelay: '0.00s' }} aria-hidden="true"><path d="M20 3c1.6 9.4 7.6 15.4 17 17-9.4 1.6-15.4 7.6-17 17-1.6-9.4-7.6-15.4-17-17 9.4-1.6 15.4-7.6 17-17z" fill="currentColor" /></svg>
        <svg viewBox="0 0 40 40" className="tp-twinkle absolute text-honey" style={{ left: '14%', top: '42%', width: '8.4px', animationDelay: '0.40s' }} aria-hidden="true"><path d="M20 3c1.6 9.4 7.6 15.4 17 17-9.4 1.6-15.4 7.6-17 17-1.6-9.4-7.6-15.4-17-17 9.4-1.6 15.4-7.6 17-17z" fill="currentColor" /></svg>
        <svg viewBox="0 0 40 40" className="tp-twinkle absolute text-honey" style={{ left: '23%', top: '12%', width: '9.8px', animationDelay: '0.80s' }} aria-hidden="true"><path d="M20 3c1.6 9.4 7.6 15.4 17 17-9.4 1.6-15.4 7.6-17 17-1.6-9.4-7.6-15.4-17-17 9.4-1.6 15.4-7.6 17-17z" fill="currentColor" /></svg>
        <svg viewBox="0 0 40 40" className="tp-twinkle absolute text-honey" style={{ left: '31%', top: '30%', width: '7px', animationDelay: '1.20s' }} aria-hidden="true"><path d="M20 3c1.6 9.4 7.6 15.4 17 17-9.4 1.6-15.4 7.6-17 17-1.6-9.4-7.6-15.4-17-17 9.4-1.6 15.4-7.6 17-17z" fill="currentColor" /></svg>
        <svg viewBox="0 0 40 40" className="tp-twinkle absolute text-honey" style={{ left: '44%', top: '9%', width: '11.2px', animationDelay: '1.60s' }} aria-hidden="true"><path d="M20 3c1.6 9.4 7.6 15.4 17 17-9.4 1.6-15.4 7.6-17 17-1.6-9.4-7.6-15.4-17-17 9.4-1.6 15.4-7.6 17-17z" fill="currentColor" /></svg>
        <svg viewBox="0 0 40 40" className="tp-twinkle absolute text-honey" style={{ left: '52%', top: '36%', width: '7.7px', animationDelay: '2.00s' }} aria-hidden="true"><path d="M20 3c1.6 9.4 7.6 15.4 17 17-9.4 1.6-15.4 7.6-17 17-1.6-9.4-7.6-15.4-17-17 9.4-1.6 15.4-7.6 17-17z" fill="currentColor" /></svg>
        <svg viewBox="0 0 40 40" className="tp-twinkle absolute text-honey" style={{ left: '63%', top: '15%', width: '10.5px', animationDelay: '2.40s' }} aria-hidden="true"><path d="M20 3c1.6 9.4 7.6 15.4 17 17-9.4 1.6-15.4 7.6-17 17-1.6-9.4-7.6-15.4-17-17 9.4-1.6 15.4-7.6 17-17z" fill="currentColor" /></svg>
        <svg viewBox="0 0 40 40" className="tp-twinkle absolute text-honey" style={{ left: '71%', top: '40%', width: '7px', animationDelay: '2.80s' }} aria-hidden="true"><path d="M20 3c1.6 9.4 7.6 15.4 17 17-9.4 1.6-15.4 7.6-17 17-1.6-9.4-7.6-15.4-17-17 9.4-1.6 15.4-7.6 17-17z" fill="currentColor" /></svg>
        <svg viewBox="0 0 40 40" className="tp-twinkle absolute text-honey" style={{ left: '92%', top: '33%', width: '8.4px', animationDelay: '3.20s' }} aria-hidden="true"><path d="M20 3c1.6 9.4 7.6 15.4 17 17-9.4 1.6-15.4 7.6-17 17-1.6-9.4-7.6-15.4-17-17 9.4-1.6 15.4-7.6 17-17z" fill="currentColor" /></svg>
      </div>
      <div className="absolute top-8 right-12 md:right-24 pointer-events-none select-none">
        <svg className="w-12 h-12 text-[#fbe3b4] opacity-80" viewBox="0 0 50 50" fill="currentColor">
          <path d="M25 5C14 5 5 14 5 25c0 11 9 20 20 20 5 0 9.6-1.8 13.2-4.8-10.4-.6-18.7-9.3-18.7-20 0-4.8 1.7-9.2 4.6-12.7C27.5 5.9 26.3 5 25 5z" />
        </svg>
      </div>

      <div className="gutter relative mx-auto grid max-w-[110rem] gap-12 pt-20 md:grid-cols-12 md:gap-x-12 md:gap-y-6 md:pt-28">
        {/* Brand */}
        <div className="md:col-span-5">
          <p className="font-plush text-big text-honey-soft">Home, at last.</p>
          <p className="mt-5 max-w-md text-milk/80 text-sm sm:text-base leading-relaxed">
            TeddyPups U.A.E. is a Dubai-based brand specializing in miniature puppies, offering premium services and worldwide shipping.
          </p>
        </div>

        {/* Puppy in Wicker Basket Illustration / Live Pup Stop */}
        <div className="order-last md:order-none md:col-span-5 md:col-start-1 md:row-start-2">
          <div className="tp-basket">
              <svg aria-hidden="true" className="tp-basket__back" viewBox="0 0 300 240">
                <ellipse className="tp-basket__hollow" cx="212" cy="145" rx="96" ry="12"></ellipse>
                <path className="tp-basket__rim-line" d="M116 145 A96 12 0 0 1 308 145"></path>
                <path className="tp-basket__rim" d="M116 145 A96 12 0 0 1 308 145"></path>
              </svg>
              <div
                className="pup-stop tp-basket__pup"
                data-act="basket"
                data-behind="true"
                data-facing="right"
                data-lane="true"
                data-pose="snug"
                data-pup-stop="true"
              >
                <div className="pup-buddy" data-facing="right">
                  <svg aria-label="Teddy, sitting snug in his basket" focusable="false" role="img" style={{ overflow: 'visible' }} viewBox="0 0 300 240">
                    <g data-p="root">
                      <g data-p="head" transform="translate(0 9) rotate(4 212 100)">
                        <path d="M178 146 Q212 162 246 146 L246 154 Q212 170 178 154 Z" fill="#a24a1a" stroke="#2a170e" strokeLinecap="round" strokeLinejoin="round" strokeWidth="3" />
                        <path d="M212 160 C212 156 206 155 206 159.4 C206 163 212 166.6 212 168.4 C212 166.6 218 163 218 159.4 C218 155 212 156 212 160 Z" fill="#fbe3b4" stroke="#2a170e" strokeLinecap="round" strokeLinejoin="round" strokeWidth="2.4" />
                        <path d="M177.1 78.7Q186.9 70.8 186.6 87.4Q196.0 89.9 189.9 105.5Q195.2 117.3 185.5 126.0Q184.7 142.8 175.2 141.2Q168.7 156.5 162.9 145.3Q153.1 153.2 153.4 136.6Q144.0 134.1 150.1 118.5Q144.8 106.7 154.5 98.0Q155.3 81.2 164.8 82.8Q171.3 67.5 177.1 78.7Z" data-p="earL" fill="#e4a352" stroke="#2a170e" strokeLinecap="round" strokeLinejoin="round" strokeWidth="3.4" transform="rotate(3 174 82)" />
                        <path d="M246.9 78.7Q252.7 67.5 259.2 82.8Q268.7 81.2 269.5 98.0Q279.2 106.7 273.9 118.5Q280.0 134.1 270.6 136.6Q270.9 153.2 261.1 145.3Q255.3 156.5 248.8 141.2Q239.3 142.8 238.5 126.0Q228.8 117.3 234.1 105.5Q228.0 89.9 237.4 87.4Q237.1 70.8 246.9 78.7Z" data-p="earR" fill="#e4a352" stroke="#2a170e" strokeLinecap="round" strokeLinejoin="round" strokeWidth="3.4" transform="rotate(-3 250 82)" />
                        <path d="M212.0 54.0Q223.4 48.2 231.5 57.5Q244.5 56.1 248.1 67.5Q260.7 70.7 259.1 82.4Q269.4 89.7 263.0 100.0Q269.4 110.3 259.1 117.6Q260.7 129.3 248.1 132.5Q244.5 143.9 231.5 142.5Q223.4 151.8 212.0 146.0Q200.6 151.8 192.5 142.5Q179.5 143.9 175.9 132.5Q163.3 129.3 164.9 117.6Q154.6 110.3 161.0 100.0Q154.6 89.7 164.9 82.4Q163.3 70.7 175.9 67.5Q179.5 56.1 192.5 57.5Q200.6 48.2 212.0 54.0Z" fill="#f2be6b" stroke="#2a170e" strokeLinecap="round" strokeLinejoin="round" strokeWidth="3.4" />
                        <path d="M195.0 52.0Q190.7 45.8 200.0 43.5Q203.2 36.9 212.0 40.0Q220.8 36.9 224.0 43.5Q233.3 45.8 229.0 52.0Q233.3 58.2 224.0 60.5Q220.8 67.1 212.0 64.0Q203.2 67.1 200.0 60.5Q190.7 58.2 195.0 52.0Z" fill="#f2be6b" stroke="#2a170e" strokeLinecap="round" strokeLinejoin="round" strokeWidth="3" />
                        <path d="M188 120 C188 106 200 100 212 100 C224 100 236 106 236 120 C236 133 225 140 212 140 C199 140 188 133 188 120 Z" fill="#fbe3b4" />
                        <circle cx="181" cy="116" fill="#f9b9a6" opacity="0.85" r="7" />
                        <circle cx="243" cy="116" fill="#f9b9a6" opacity="0.85" r="7" />
                        <g data-p="eyes" transform="translate(0 0)">
                          <g data-p="open" opacity="1">
                            <g data-p="blink" transform="translate(0 0) scale(1 1)">
                              <ellipse cx="194" cy="98" fill="#2a170e" rx="7.4" ry="8.6" />
                              <ellipse cx="230" cy="98" fill="#2a170e" rx="7.4" ry="8.6" />
                              <circle cx="196.6" cy="94.6" fill="#fff" r="2.7" />
                              <circle cx="232.6" cy="94.6" fill="#fff" r="2.7" />
                              <circle cx="192" cy="101.2" fill="#fff" r="1.2" />
                              <circle cx="228" cy="101.2" fill="#fff" r="1.2" />
                            </g>
                          </g>
                        </g>
                        <path d="M204.5 111.5 Q212 107.2 219.5 111.5 Q218.2 118.4 212 120 Q205.8 118.4 204.5 111.5 Z" fill="#2a170e" />
                        <path d="M212 120 V124.5 M212 124.5 Q207.2 129.6 202.8 125.2 M212 124.5 Q216.8 129.6 221.2 125.2" fill="none" stroke="#2a170e" strokeLinecap="round" strokeLinejoin="round" strokeWidth="3" />
                      </g>
                      <g data-p="ledge" opacity="1">
                        <path d="M175 159 C175 148 181 142 190 142 C199 142 205 148 205 159 Z M219 159 C219 148 225 142 234 142 C243 142 249 148 249 159 Z" fill="#f2be6b" stroke="#2a170e" strokeLinecap="round" strokeLinejoin="round" strokeWidth="3.4" />
                        <path d="M186 153 v-4.5 M194 153 v-4.5 M230 153 v-4.5 M238 153 v-4.5" fill="none" stroke="#2a170e" strokeLinecap="round" strokeLinejoin="round" strokeWidth="2.4" />
                      </g>
                    </g>
                  </svg>
                  <span aria-hidden="true" className="pup-bubble" data-show="false"></span>
                </div>
              </div>
              <svg aria-hidden="true" className="tp-basket__front" viewBox="0 0 300 240">
                <path className="tp-basket__body" d="M116 145 C118 180 126 214 138 232 L286 232 C298 214 306 180 308 145 A96 12 0 0 1 116 145 Z"></path>
                <path className="tp-basket__weave" d="M121 178 Q212 197 303 178 M127 206 Q212 223 297 206"></path>
                <path className="tp-basket__weave tp-basket__weave--stakes" d="M150 164 L158 230 M182 168 L185 232 M212 169 V232 M242 168 L239 232 M274 164 L266 230"></path>
                <path className="tp-basket__rim-line" d="M116 145 A96 12 0 0 0 308 145"></path>
                <path className="tp-basket__rim" d="M116 145 A96 12 0 0 0 308 145"></path>
              </svg>
            </div>
          </div>

          {/* Explore Links */}
          <div className="md:col-span-3 space-y-3">
            <h2 className="font-scrawl text-lg text-honey">Explore</h2>
            <ul className="space-y-2 text-sm text-[#fffdf8]/80 font-medium">
              <li>
                <button onClick={() => handleNav('/puppies')} className="hover:text-[#f2be6b] transition-colors text-left">
                  Available puppies
                </button>
              </li>
              <li>
                <button onClick={() => handleNav('/gone-home')} className="hover:text-[#f2be6b] transition-colors text-left">
                  Gone home
                </button>
              </li>
              <li>
                <button onClick={() => handleNav('/happy-families')} className="hover:text-[#f2be6b] transition-colors text-left">
                  Happy families
                </button>
              </li>
              <li>
                <button onClick={() => handleNav('/how-it-works')} className="hover:text-[#f2be6b] transition-colors text-left">
                  How it works
                </button>
              </li>
              <li>
                <button onClick={() => handleNav('/how-it-works#delivery')} className="hover:text-[#f2be6b] transition-colors text-left">
                  Delivery & collection
                </button>
              </li>
              <li>
                <button onClick={() => handleNav('/faq')} className="hover:text-[#f2be6b] transition-colors text-left">
                  FAQ
                </button>
              </li>
              <li>
                <button onClick={() => handleNav('/contact')} className="hover:text-[#f2be6b] transition-colors text-left">
                  Visit & contact
                </button>
              </li>
            </ul>
          </div>

          {/* Say Hello */}
          <div className="md:col-span-4 space-y-3">
            <h2 className="font-scrawl text-lg text-honey">Say hello</h2>
            <div className="space-y-2 text-sm text-[#fffdf8]/80">
              <p>
                <span className="block text-xs uppercase tracking-wider text-[#fbe3b4]/60 font-semibold">WhatsApp</span>
                <a href="https://wa.me/971541676733" target="_blank" rel="noopener noreferrer" className="hover:text-[#f2be6b] transition-colors font-medium">
                  +971 54 167 6733
                </a>
              </p>
              <p>
                <span className="block text-xs uppercase tracking-wider text-[#fbe3b4]/60 font-semibold">Email</span>
                <a href="mailto:teddypupsadmin@gmail.com" className="hover:text-[#f2be6b] transition-colors font-medium">
                  teddypupsadmin@gmail.com
                </a>
              </p>
              <p>
                <span className="block text-xs uppercase tracking-wider text-[#fbe3b4]/60 font-semibold">Showroom</span>
                <span>Downtown Dubai, United Arab Emirates</span>
              </p>
            </div>

            {/* Social Pills */}
            <div className="pt-3 flex flex-wrap gap-2">
              <a
                href="https://instagram.com"
                target="_blank"
                rel="noopener noreferrer"
                className="px-4 py-1.5 rounded-full border border-[#fffdf8]/30 text-xs font-semibold hover:border-[#f2be6b] hover:text-[#f2be6b] transition-colors"
              >
                Instagram
              </a>
              <a
                href="https://tiktok.com"
                target="_blank"
                rel="noopener noreferrer"
                className="px-4 py-1.5 rounded-full border border-[#fffdf8]/30 text-xs font-semibold hover:border-[#f2be6b] hover:text-[#f2be6b] transition-colors"
              >
                TikTok
              </a>
              <a
                href="https://facebook.com"
                target="_blank"
                rel="noopener noreferrer"
                className="px-4 py-1.5 rounded-full border border-[#fffdf8]/30 text-xs font-semibold hover:border-[#f2be6b] hover:text-[#f2be6b] transition-colors"
              >
                Facebook
              </a>
            </div>
          </div>
        </div>

        {/* Bottom Bar */}
        <div className="gutter relative mx-auto max-w-[110rem] mt-16 pt-8 border-t border-[#fffdf8]/15 flex flex-col sm:flex-row items-center justify-between text-xs text-[#fffdf8]/60 gap-4">
          <div className="flex items-center gap-2">
            <img src="/brand/logo.png" alt="" className="w-5 h-5 rounded-full opacity-80" />
            <span>© 2026 TeddyPups U.A.E.</span>
          </div>
          <div className="font-scrawl text-sm text-[#fbe3b4]">
            every puppy is family
          </div>
        </div>
    </footer>
  );
}

