import React from 'react';

export default function PuppyCard({ puppy, onSelect, onWatchVideo }) {
  const isGone = puppy.status === 'gone_home';
  const primaryImg = puppy.images?.[0] || '/brand/logo.png';

  return (
    <div className="group relative flex flex-col items-center text-center p-3 transition-transform duration-300 hover:-translate-y-1">
      {/* Photo Container with Circular Frame & Stickers */}
      <div className="relative w-48 h-48 sm:w-56 sm:h-56 mb-4">
        {/* Cute hand-drawn Tape Sticker on top/right */}
        <div className="absolute -top-1.5 -right-1 z-20">
          <span
            className={`inline-block px-3 py-1 text-xs font-bold rounded-full shadow-sm tracking-wide transform rotate-3 border ${
              isGone
                ? 'bg-[#fbe3b4] text-cocoa border-cocoa/30'
                : 'bg-[#fffdf8] text-toffee border-toffee/40'
            }`}
          >
            {isGone ? 'gone home ♥' : 'Available'}
          </span>
        </div>

        {/* Video Badge if available */}
        {puppy.hasVideo && puppy.video && (
          <button
            onClick={(e) => {
              e.stopPropagation();
              onWatchVideo(puppy.video, puppy.name);
            }}
            className="absolute -top-1 -left-1 z-20 px-2.5 py-1 bg-black/85 text-white text-[11px] font-semibold rounded-full flex items-center gap-1 shadow-md hover:bg-black transition-colors"
          >
            <span>▶</span> video
          </button>
        )}

        {/* Hand-drawn Doodles around the circle */}
        <div className="absolute -bottom-2 -left-2 text-toffee opacity-60 pointer-events-none select-none text-lg">
          ♡
        </div>
        <div className="absolute top-1/2 -right-3 text-honey opacity-80 pointer-events-none select-none text-lg">
          ✦
        </div>

        {/* Circular Avatar */}
        <button
          onClick={() => onSelect(puppy.slug)}
          className="w-full h-full rounded-full overflow-hidden border-4 border-[#fbe3b4] group-hover:border-toffee transition-colors shadow-md bg-milk focus:outline-none focus:ring-4 focus:ring-honey/50"
        >
          <img
            src={primaryImg}
            alt={puppy.name}
            className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
            loading="lazy"
          />
        </button>
      </div>

      {/* Info Section */}
      <button
        onClick={() => onSelect(puppy.slug)}
        className="focus:outline-none flex flex-col items-center"
      >
        <h3 className="font-plush text-xl sm:text-2xl font-bold text-cocoa group-hover:text-toffee transition-colors">
          {puppy.name}
        </h3>
        <p className="mt-1 text-sm text-cocoa/75 font-medium flex items-center gap-1.5 flex-wrap justify-center">
          <span>{puppy.breed}</span>
          <span>·</span>
          <span className="capitalize">{puppy.gender}</span>
          {puppy.age && (
            <>
              <span>·</span>
              <span>{puppy.age}</span>
            </>
          )}
        </p>
      </button>
    </div>
  );
}

