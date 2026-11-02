import React, { useState, useEffect, useRef } from 'react';
import Header from './components/Header';
import Footer from './components/Footer';
import MobileActionBar from './components/MobileActionBar';
import VideoModal from './components/VideoModal';
import PageCurtain from './components/PageCurtain';
import RevealScope from './components/RevealScope';
import SmoothScroll from './components/SmoothScroll';
import PupJourney from './components/PupJourney';
import PawTrailCanvas from './components/PawTrailCanvas';
import useTeddyInteractivity from './hooks/useTeddyInteractivity';

// Pages
import HomePage from './pages/HomePage';
import PuppiesPage from './pages/PuppiesPage';
import PuppyDetailPage from './pages/PuppyDetailPage';
import HowItWorksPage from './pages/HowItWorksPage';
import HappyFamiliesPage from './pages/HappyFamiliesPage';
import GoneHomePage from './pages/GoneHomePage';
import FaqPage from './pages/FaqPage';
import ContactPage from './pages/ContactPage';

export default function App() {
  const [currentPath, setCurrentPath] = useState(window.location.pathname || '/');
  const [activeVideo, setActiveVideo] = useState({ url: null, name: '' });
  const [curtainState, setCurtainState] = useState('intro');
  const pendingNavRef = useRef(null);
  const timeoutsRef = useRef([]);

  // Enable rich interactive mascot animations (blinking, hearts, speech, tail)
  useTeddyInteractivity();

  const addTimeout = (fn, ms) => {
    const id = setTimeout(fn, ms);
    timeoutsRef.current.push(id);
    return id;
  };

  const clearTimeouts = () => {
    timeoutsRef.current.forEach(clearTimeout);
    timeoutsRef.current = [];
  };

  // Initial intro curtain animation on mount
  useEffect(() => {
    document.documentElement.dataset.curtain = 'intro';
    
    // Check prefers-reduced-motion
    if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      setCurtainState('idle');
      delete document.documentElement.dataset.curtain;
      window.dispatchEvent(new Event('tp:arrived'));
      return;
    }

    addTimeout(() => {
      window.dispatchEvent(new Event('tp:arrived'));
    }, 560);

    addTimeout(() => {
      setCurtainState('idle');
      delete document.documentElement.dataset.curtain;
    }, 1080);

    return () => clearTimeouts();
  }, []);

  // Popstate handling (back/forward)
  useEffect(() => {
    const handlePopState = () => {
      const newPath = window.location.pathname || '/';
      clearTimeouts();
      setCurtainState('snap');
      document.documentElement.dataset.curtain = 'snap';
      
      addTimeout(() => {
        setCurrentPath(newPath);
        window.scrollTo(0, 0);
        setCurtainState('lifting');
        document.documentElement.dataset.curtain = 'lifting';
        window.dispatchEvent(new Event('tp:arrived'));

        addTimeout(() => {
          setCurtainState('idle');
          delete document.documentElement.dataset.curtain;
        }, 460);
      }, 140);
    };

    window.addEventListener('popstate', handlePopState);
    return () => window.removeEventListener('popstate', handlePopState);
  }, []);

  // Smooth curtain navigation
  const navigate = (path) => {
    const targetUrl = new URL(path, window.location.href);
    const targetPath = targetUrl.pathname + targetUrl.search;

    if (targetUrl.pathname === window.location.pathname && targetUrl.search === window.location.search) {
      window.scrollTo({ top: 0, behavior: 'smooth' });
      return;
    }

    // If reduced motion, change immediately
    if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      window.history.pushState({}, '', targetPath);
      setCurrentPath(targetUrl.pathname);
      window.scrollTo(0, 0);
      window.dispatchEvent(new Event('tp:arrived'));
      return;
    }

    clearTimeouts();
    window.dispatchEvent(new Event('tp:navigate'));
    setCurtainState('covering');
    document.documentElement.dataset.curtain = 'covering';

    addTimeout(() => {
      setCurtainState('covered');
      document.documentElement.dataset.curtain = 'covered';

      window.history.pushState({}, '', targetPath);
      setCurrentPath(targetUrl.pathname);
      window.scrollTo(0, 0);

      addTimeout(() => {
        setCurtainState('lifting');
        document.documentElement.dataset.curtain = 'lifting';
        window.dispatchEvent(new Event('tp:arrived'));

        addTimeout(() => {
          setCurtainState('idle');
          delete document.documentElement.dataset.curtain;
        }, 460);
      }, 80);
    }, 300);
  };

  // Intercept all internal <a> link clicks
  useEffect(() => {
    const handleClick = (e) => {
      if (e.defaultPrevented || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) {
        return;
      }
      const anchor = e.target.closest('a[href]');
      if (!anchor) return;
      if (anchor.target && anchor.target !== '_self') return;
      if (anchor.hasAttribute('download') || anchor.dataset.noCurtain !== undefined) return;

      const href = anchor.getAttribute('href');
      if (!href || href.startsWith('#') || href.startsWith('mailto:') || href.startsWith('tel:') || href.startsWith('javascript:')) {
        return;
      }

      const url = new URL(anchor.href, window.location.href);
      if (url.origin !== window.location.origin) return;
      if (/^\/(admin|api|media|_next)(\/|$)/.test(url.pathname)) return;

      e.preventDefault();
      e.stopPropagation();
      navigate(url.pathname + url.search + url.hash);
    };

    document.addEventListener('click', handleClick, true);
    return () => document.removeEventListener('click', handleClick, true);
  }, []);

  const handleWatchVideo = (url, name) => {
    setActiveVideo({ url, name });
  };

  // Route matching
  const renderPage = () => {
    if (currentPath === '/') {
      return <HomePage navigate={navigate} onWatchVideo={handleWatchVideo} />;
    }
    if (currentPath === '/puppies') {
      return <PuppiesPage navigate={navigate} onWatchVideo={handleWatchVideo} />;
    }
    if (currentPath.startsWith('/puppies/')) {
      const slug = currentPath.replace('/puppies/', '').split('?')[0];
      return <PuppyDetailPage slug={slug} navigate={navigate} onWatchVideo={handleWatchVideo} />;
    }
    if (currentPath === '/how-it-works') {
      return <HowItWorksPage navigate={navigate} />;
    }
    if (currentPath === '/happy-families') {
      return <HappyFamiliesPage navigate={navigate} />;
    }
    if (currentPath === '/gone-home') {
      return <GoneHomePage navigate={navigate} />;
    }
    if (currentPath === '/faq') {
      return <FaqPage navigate={navigate} />;
    }
    if (currentPath === '/contact') {
      return <ContactPage navigate={navigate} />;
    }

    // Default fallback to HomePage
    return <HomePage navigate={navigate} onWatchVideo={handleWatchVideo} />;
  };

  return (
    <div className="min-h-screen flex flex-col bg-[#fffdf8] text-[#2a170e] selection:bg-[#f2be6b]/40">
      {/* Buttery Smooth Inertial Scroll */}
      <SmoothScroll />

      {/* Traveling Companion Puppy Scroll Animation (Home page only, matching original site) */}
      {currentPath === '/' && <PupJourney />}

      {/* Interactive Cursor Paw Print Trail */}
      <PawTrailCanvas />

      {/* Signature Animated Blanket Curtain */}
      <PageCurtain state={curtainState} />

      {/* Site Header */}
      <Header currentPath={currentPath} navigate={navigate} />

      {/* Main Page Content with Scroll Reveal Scope */}
      <main id="main" tabIndex="-1" className="relative pt-[var(--header-h)] outline-none flex-1 w-full">
        <RevealScope key={currentPath}>
          {renderPage()}
        </RevealScope>
      </main>

      {/* Site Footer */}
      <Footer navigate={navigate} />

      {/* Sticky Mobile Bar */}
      <MobileActionBar />

      {/* Video Lightbox Modal */}
      {activeVideo.url && (
        <VideoModal
          videoUrl={activeVideo.url}
          puppyName={activeVideo.name}
          onClose={() => setActiveVideo({ url: null, name: '' })}
        />
      )}
    </div>
  );
}
