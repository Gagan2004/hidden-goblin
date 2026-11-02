import React from 'react';

export default function VideoModal({ videoUrl, onClose, puppyName }) {
  if (!videoUrl) return null;

  return (
    <div
      role="dialog"
      aria-modal="true"
      aria-label={puppyName ? `${puppyName}'s Video` : 'Puppy Video'}
      className="fixed inset-0 z-[110] flex items-center justify-center bg-black/80 backdrop-blur-sm p-4 animate-fade-in"
      onClick={onClose}
    >
      <div
        className="relative max-w-lg w-full bg-cocoa text-milk rounded-3xl overflow-hidden shadow-2xl border-2 border-honey/40"
        onClick={(e) => e.stopPropagation()}
      >
        <div className="flex items-center justify-between px-6 py-4 border-b border-white/10">
          <h3 className="font-plush text-lg text-honey">
            {puppyName ? `${puppyName}'s Video` : 'Puppy Video'}
          </h3>
          <button
            onClick={onClose}
            className="w-8 h-8 rounded-full bg-white/10 hover:bg-white/20 text-white flex items-center justify-center transition-colors text-sm font-bold"
          >
            ✕
          </button>
        </div>
        <div className="p-3 bg-black aspect-[9/16] max-h-[75vh] flex items-center justify-center">
          <video
            src={videoUrl}
            controls
            autoPlay
            playsInline
            className="w-full h-full object-contain rounded-2xl"
          />
        </div>
        <div className="p-4 bg-cocoa text-center">
          <a
            href={`https://wa.me/971541676733?text=${encodeURIComponent(`Hi! I just watched the video for ${puppyName || 'this puppy'} and I'd love to know more!`)}`}
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex items-center justify-center gap-2 rounded-full bg-[#1e6f47] text-white px-6 py-2.5 font-semibold text-sm hover:bg-[#185938] transition-colors"
          >
            Ask about {puppyName || 'puppy'} on WhatsApp
          </a>
        </div>
      </div>
    </div>
  );
}

