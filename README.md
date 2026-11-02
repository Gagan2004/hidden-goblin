# TeddyPups U.A.E. — Complete Website Clone

A high-fidelity, pixel-accurate clone of [TeddyPups U.A.E.](https://puppy.instabizweb.com/), a boutique luxury teacup puppy service based in Downtown Dubai.

---

## 🐾 Overview

This project replicates the design, typography, warm artisanal aesthetic, responsive layouts, interactive widgets, and full puppy catalog of the original website. Every page, interaction, and media asset has been reproduced to match the reference site.

---

## ✨ Features & Pages

### 1. **Homepage (`/`)**
- **Hero Scene**: Warm radial sunshine glow, hand-drawn tagline with custom SVG wave doodles, plush headline typography, and action buttons.
- **Meet the Pups Showcase**: Real-time carousel of available puppies with circular avatars, breed badges, and hover animations.
- **Two Ways Home**: Interactive switcher comparing *Option 01 (Local Dubai Showroom)* and *Option 02 (Imported upon request)* with custom Dubai skyline postcard art.
- **Your Puppy Journey**: 4-step interactive timeline from inquiry to homecoming.
- **Why Families Trust Us**: The 3 Passport Promise stamps (Veterinary health check, purebred lineage pedigree, Dubai municipality compliance).
- **Happy Families Preview**: Polaroid gallery featuring real client testimonials.
- **Questions Answered**: Cork bulletin board accordion preview.
- **Ready to Meet CTA**: Warm honey-accented banner with direct WhatsApp launch.

### 2. **Available Puppies Catalog (`/puppies`)**
- Full catalog of **42 puppies** with authentic details (names, breeds, ages, genders, origins, prices, and media).
- **Real-Time Interactive Filtering**:
  - Filter by breed (*Maltipoo, Pomeranian, Poodle, Cavapoo, Shih Tzu, Bichon, Pomsky, Maltese*).
  - Filter by origin (*All Origins, In Dubai Showroom, From Korea / Abroad*).
  - Toggle filter: *▶ With video only*.
  - Instant live keyword search by puppy name, breed, or gender.
  - Active filter reset button and empty state handling.
- **Gone Home Showcase**: Dedicated archive section celebrating previously adopted puppies.

### 3. **Puppy Detail Pages (`/puppies/:slug`)**
- Individual profile pages for all 42 puppies.
- **Interactive Photo Gallery**: Main photo frame with rounded honey borders and thumbnail switcher.
- **Video Player Modal**: Video preview modal with video playback controls and WhatsApp inquiry button.
- **Puppy Passport Badges**: Microchip status, vaccinations, lineage verification, and Dubai delivery guarantees.
- **4-Step Adoption Timeline**: Interactive workflow tailored to the puppy's origin (Local vs Imported).
- **Interactive Inquiry Letter**: Pre-filled form with instant validation and confirmation animations.
- **Related Puppies Carousel**: Curated recommendations of other available puppies.

### 4. **How It Works (`/how-it-works`)**
- Full breakdown of both adoption routes (Local Showroom & Direct Flight Import).
- 4-step visual journey with flight path illustration and numbered trail markers.
- Passport stamps and veterinary guarantees checklist.

### 5. **Happy Families Testimonials (`/happy-families`)**
- Complete showcase of **64 real customer polaroids**.
- Realistic washi tape styling, rotated angles, and handwritten captions.
- Filter by breed (*Maltipoo, Pomeranian, Poodle, etc.*).
- Fullscreen Lightbox modal to inspect photos and captions up close.

### 6. **Gone Home Showcase (`/gone-home`)**
- **26 Vintage Boarding Passes**: Custom boarding ticket design with perforated stubs, departure-to-home routes (e.g. *Seoul ICN → Dubai DXB*), flight numbers, and puppy portraits.

### 7. **Questions & Answers (`/faq`)**
- Realistic cork bulletin board aesthetic with pinned paper notes and colored pushpins.
- Real-time search filter (*"Sniff out a question"*).
- Expandable accordion notes for all 9 key topics (health guarantee, airport collection, vaccinations, Dubai showroom visits, etc.).

### 8. **Visit & Contact (`/contact`)**
- **Showroom Info Card**: Downtown Dubai boutique details, striped awning illustration, arched puppy window, and Google Maps link.
- **Handwritten Letterform**: Vintage paper letter with inline dashed blanks (`my name is ____, you can reach me on ____`), postal stamp doodle, interactive submission, and mail delivery confirmation animation.

### 9. **Navigation & Global Elements**
- **Header**: Fixed blur header with scalloped hemline SVG pattern, active paw print indicator (`🐾`), and WhatsApp CTA.
- **Mobile Drawer Menu**: Fullscreen animated `<dialog>` drawer menu with handwritten *"where to, friend?"* greeting.
- **Mobile Action Bar**: Fixed bottom navigation bar on mobile viewports (<768px) with quick WhatsApp and phone call triggers.
- **Artisanal Footer**: *"Home, at last."* footer featuring an animated puppy in a basket SVG, night sky moon & stars, sitemap navigation, and social links.

---

## 🛠️ Tech Stack & Design System

- **Framework**: [React 19](https://react.dev/) + [Vite 6](https://vitejs.dev/)
- **Styling**: [Tailwind CSS 3](https://tailwindcss.com/)
- **Typography**:
  - `Fraunces` — Luxurious serif plush display heading font
  - `Figtree` — Clean, legible modern sans-serif body font
  - `Shantell Sans` — Playful handwritten scrawl font
- **Color Palette**:
  - Cocoa: `#2a170e` (Deep espresso typography & borders)
  - Milk: `#fffdf8` (Warm cream background)
  - Honey: `#f2be6b` / `#fbe3b4` (Golden accents & paper cards)
  - Toffee: `#c2622b` / `#a24a1a` (Primary action buttons & stamps)
  - Sky: `#bfddf5` (Air travel accents)

---

## 🚀 Getting Started

### Prerequisites
- Node.js (v18 or higher recommended)
- npm or yarn

### Installation
```bash
# Clone or navigate to the repository
cd insta_biz

# Install dependencies
npm install
```

### Running Locally
```bash
# Start Vite development server
npm run dev
```
Open your browser and navigate to `http://localhost:5173/`.

### Production Build & Preview
```bash
# Build optimized production bundle
npm run build

# Preview production build locally
npm run preview
```
The preview server will be accessible at `http://localhost:4173/`.

---

## 📱 Responsive Verification

The application is thoroughly verified across desktop (1440px), tablet (768px), and mobile viewports (390px, e.g. iPhone 14/15/16).
Screenshot captures of all pages and interactive states are stored in `screenshots_clone/` and `screenshots_clone/mobile/`.

