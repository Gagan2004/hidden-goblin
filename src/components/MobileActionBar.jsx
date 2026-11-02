import React from 'react';

export default function MobileActionBar() {
  return (
    <div className="fixed inset-x-0 bottom-0 z-40 border-t-2 border-cocoa bg-[#fffdf8] px-3 py-2 md:hidden shadow-lg pb-[calc(0.5rem+env(safe-area-inset-bottom))]">
      <div className="flex items-center gap-2 max-w-sm mx-auto">
        <a
          href="https://wa.me/971541676733"
          target="_blank"
          rel="noopener noreferrer"
          className="flex-1 min-h-[42px] rounded-full bg-[#1e6f47] text-white flex items-center justify-center font-bold text-xs sm:text-sm shadow hover:bg-[#185938] transition-colors"
        >
          <span>WhatsApp us</span>
        </a>
        <a
          href="tel:+971541676733"
          className="min-h-[42px] px-5 rounded-full border-2 border-cocoa text-cocoa bg-[#fffdf8] flex items-center justify-center font-bold text-xs sm:text-sm hover:bg-cocoa hover:text-white transition-colors"
        >
          Call
        </a>
      </div>
    </div>
  );
}
