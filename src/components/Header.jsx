import React, { useState, useEffect, useRef } from 'react';

export default function Header({ currentPath, navigate }) {
  const [scrolled, setScrolled] = useState(false);
  const dialogRef = useRef(null);

  useEffect(() => {
    const onScroll = () => {
      setScrolled(window.scrollY > 20);
    };
    window.addEventListener('scroll', onScroll);
    return () => window.removeEventListener('scroll', onScroll);
  }, []);

  const closeMenu = () => {
    const dialog = dialogRef.current;
    if (!dialog || !dialog.open) return;
    dialog.dataset.closing = 'true';
    let closed = false;
    const onEnd = () => {
      if (closed) return;
      closed = true;
      dialog.removeEventListener('animationend', onEnd);
      delete dialog.dataset.closing;
      dialog.close();
    };
    dialog.addEventListener('animationend', onEnd);
    setTimeout(onEnd, 450);
  };

  const navItems = [
    { label: 'Home', path: '/' },
    { label: 'Puppies', path: '/puppies' },
    { label: 'Happy families', path: '/happy-families' },
    { label: 'How it works', path: '/how-it-works' },
    { label: 'FAQ', path: '/faq' },
    { label: 'Visit & contact', path: '/contact' },
  ];

  const handleNav = (path) => {
    closeMenu();
    navigate(path);
  };

  return (
    <>
      <header
        id="site-header"
        className="tp-header fixed inset-x-0 top-0 z-50 w-full"
        data-scrolled={scrolled ? 'true' : 'false'}
        data-hidden="false"
        {...(currentPath === '/' ? { 'data-home': 'true' } : {})}
      >
        <div className="tp-header__bar gutter">
          {/* Brand Logo */}
          <a
            href="/"
            onClick={(e) => {
              e.preventDefault();
              handleNav('/');
            }}
            className="tp-header__brand"
            aria-label="TeddyPups U.A.E. — home"
          >
            <img
              src="/brand/logo.png"
              alt="TeddyPups Logo"
              className="tp-header__logo rounded-full object-cover"
              width="56"
              height="56"
            />
            <span className="font-plush tp-header__name">
              TeddyPups
            </span>
          </a>

          {/* Desktop Navigation */}
          <nav aria-label="Main" className="tp-header__nav">
            <ul>
              {navItems.map((item) => {
                const isActive =
                  currentPath === item.path ||
                  (item.path !== '/' && currentPath.startsWith(item.path));
                return (
                  <li key={item.path}>
                    <a
                      href={item.path}
                      onClick={(e) => {
                        e.preventDefault();
                        handleNav(item.path);
                      }}
                      className="tp-nav-link"
                      data-active={isActive ? 'true' : 'false'}
                      aria-current={isActive ? 'page' : undefined}
                    >
                      <span>{item.label}</span>
                      <svg
                        viewBox="0 0 64 64"
                        className="tp-nav-link__paw"
                        aria-hidden="true"
                        fill="currentColor"
                      >
                        <path d="M32 30.5c-7.6 0-15.6 8.3-15.6 15.5 0 5.4 4.2 8.3 9.2 8.3 2.6 0 4.5-1.1 6.4-1.1s3.8 1.1 6.4 1.1c5 0 9.2-2.9 9.2-8.3 0-7.2-8-15.5-15.6-15.5zM19.28 26.71C21.07 30.08 20.42 33.92 17.84 35.29C15.25 36.67 11.71 35.05 9.92 31.69C8.13 28.32 8.78 24.48 11.36 23.11C13.95 21.73 17.49 23.35 19.28 26.71ZM29.62 15.64C30.32 19.62 28.46 23.26 25.47 23.79C22.48 24.32 19.48 21.53 18.78 17.56C18.08 13.58 19.94 9.94 22.93 9.41C25.92 8.88 28.92 11.67 29.62 15.64ZM45.22 17.56C44.52 21.53 41.52 24.32 38.53 23.79C35.54 23.26 33.68 19.62 34.38 15.64C35.08 11.67 38.08 8.88 41.07 9.41C44.06 9.94 45.92 13.58 45.22 17.56ZM54.08 31.69C52.29 35.05 48.75 36.67 46.16 35.29C43.58 33.92 42.93 30.08 44.72 26.71C46.51 23.35 50.05 21.73 52.64 23.11C55.22 24.48 55.87 28.32 54.08 31.69Z" />
                      </svg>
                    </a>
                  </li>
                );
              })}
            </ul>
          </nav>

          {/* Right Action */}
          <div className="tp-header__end">
            <a
              href="https://wa.me/971541676733?text=Hi%20TeddyPups!%20I'd%20love%20to%20know%20more%20about%20your%20puppies."
              target="_blank"
              rel="noopener noreferrer"
              className="btn btn-whatsapp tp-header__wa"
            >
              WhatsApp us
            </a>

            {/* Mobile / Tablet Menu Button */}
            <button
              onClick={() => dialogRef.current?.showModal()}
              className="inline-flex h-10 items-center gap-2 rounded-full border-2 border-cocoa bg-milk px-4 text-[0.95rem] font-semibold lg:hidden shadow-sm"
              type="button"
              aria-haspopup="dialog"
            >
              <svg viewBox="0 0 64 64" className="size-4 text-toffee" aria-hidden="true" fill="currentColor">
                <path d="M32 30.5c-7.6 0-15.6 8.3-15.6 15.5 0 5.4 4.2 8.3 9.2 8.3 2.6 0 4.5-1.1 6.4-1.1s3.8 1.1 6.4 1.1c5 0 9.2-2.9 9.2-8.3 0-7.2-8-15.5-15.6-15.5zM19.28 26.71C21.07 30.08 20.42 33.92 17.84 35.29C15.25 36.67 11.71 35.05 9.92 31.69C8.13 28.32 8.78 24.48 11.36 23.11C13.95 21.73 17.49 23.35 19.28 26.71ZM29.62 15.64C30.32 19.62 28.46 23.26 25.47 23.79C22.48 24.32 19.48 21.53 18.78 17.56C18.08 13.58 19.94 9.94 22.93 9.41C25.92 8.88 28.92 11.67 29.62 15.64ZM45.22 17.56C44.52 21.53 41.52 24.32 38.53 23.79C35.54 23.26 33.68 19.62 34.38 15.64C35.08 11.67 38.08 8.88 41.07 9.41C44.06 9.94 45.92 13.58 45.22 17.56ZM54.08 31.69C52.29 35.05 48.75 36.67 46.16 35.29C43.58 33.92 42.93 30.08 44.72 26.71C46.51 23.35 50.05 21.73 52.64 23.11C55.22 24.48 55.87 28.32 54.08 31.69Z" />
              </svg>
              <span>Menu</span>
            </button>
          </div>
        </div>

        {/* Scalloped Header Hem Border */}
        <svg
          aria-hidden="true"
          className="tp-header__hem"
          width="100%"
          height="14"
          preserveAspectRatio="none"
        >
          <defs>
            <pattern height="14" id="tp-hem" patternUnits="userSpaceOnUse" width="44">
              <path className="tp-header__hem-fill fill-milk" d="M0 0H44V2A22 11 0 0 1 0 2Z" />
              <path className="tp-header__hem-line stroke-cocoa/20 fill-none" d="M0 2A22 11 0 0 0 44 2" />
            </pattern>
          </defs>
          <rect fill="url(#tp-hem)" height="14" width="100%" />
        </svg>
      </header>

      {/* Mobile Drawer / Dialog Menu */}
      <dialog
        ref={dialogRef}
        aria-label="Site menu"
        className="tp-menu m-0 h-dvh max-h-none w-screen max-w-none bg-honey p-0 text-cocoa backdrop:bg-cocoa/40"
        onClick={(e) => e.target === dialogRef.current && closeMenu()}
        onCancel={(e) => {
          e.preventDefault();
          closeMenu();
        }}
        onClose={(e) => delete e.currentTarget.dataset.closing}
      >
        <div className="flex h-full flex-col gutter pb-[calc(1.5rem+env(safe-area-inset-bottom))] pt-5">
          {/* Top Bar */}
          <div className="flex items-center justify-between">
            <span className="font-scrawl text-lg">where to, friend?</span>
            <button
              type="button"
              onClick={closeMenu}
              className="h-11 rounded-full bg-cocoa px-5 font-semibold text-milk"
            >
              Close
            </button>
          </div>

          {/* Nav Links */}
          <nav aria-label="Mobile" className="mt-10 flex-1">
            <ul className="space-y-1">
              {navItems.map((item) => {
                const isActive =
                  currentPath === item.path ||
                  (item.path !== '/' && currentPath.startsWith(item.path));
                return (
                  <li key={item.path}>
                    <a
                      href={item.path}
                      onClick={(e) => {
                        e.preventDefault();
                        handleNav(item.path);
                      }}
                      className="tp-menu-link font-plush block py-2 text-[clamp(2.4rem,11vw,3.4rem)] leading-tight text-cocoa transition-colors"
                      data-active={isActive ? 'true' : 'false'}
                    >
                      {item.label}
                    </a>
                  </li>
                );
              })}
            </ul>
          </nav>

          {/* Bottom Contact Details */}
          <div className="space-y-3 pt-6 border-t border-cocoa/15">
            <a
              href="https://wa.me/971541676733?text=Hi%20TeddyPups!%20I'd%20love%20to%20know%20more%20about%20your%20puppies."
              target="_blank"
              rel="noopener noreferrer"
              className="btn btn-whatsapp w-full justify-center"
            >
              WhatsApp us
            </a>
            <p className="text-center text-sm font-semibold text-cocoa-soft">
              Downtown Dubai, UAE
            </p>
          </div>
        </div>
      </dialog>
    </>
  );
}
