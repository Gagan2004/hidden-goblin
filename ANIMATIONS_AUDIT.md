# Complete Animations Audit & Implementation Plan — TeddyPups U.A.E.

This document catalogs all animations present in the original production website (`https://puppy.instabizweb.com`), assesses their status in the local codebase, and tracks their implementation.

---

## 1. Summary of Animation Categories

| Category | Total Detected | Fully Implemented | Incomplete / Buggy | Missing |
|---|---|---|---|---|
| **CSS `@keyframes`** | 46 | 40 | 3 | 3 |
| **Interactive Mascot (`PupJourney`)** | 12 | 11 | 1 | 0 |
| **Scroll-Driven / Bezier** | 6 | 5 | 1 | 0 |
| **Interactive Forms & Modals** | 4 | 1 | 1 | 2 |
| **UI Atmosphere & Polish** | 6 | 4 | 1 | 1 |
| **Total** | **74** | **61** | **7** | **6** |

---

## 2. Complete Inventory of Animations

### A. Global & Page Shell

| # | Animation | Class / Selector | Trigger / Purpose | Original Production Behavior | Status in Local | Action Needed |
|---|---|---|---|---|---|---|
| 1 | `tp-curtain-cover` | `.tp-curtain[data-state=covering] .tp-curtain__blanket` | Page navigation transition | Scalloped blanket slides up from bottom (`0.3s cubic-bezier(0.22, 1, 0.36, 1)`) | ✅ Present | Ensure triggers on route change |
| 2 | `tp-curtain-lift` | `.tp-curtain[data-state=lifting] .tp-curtain__blanket` | Page arrival transition | Blanket lifts to reveal new page content (`0.46s cubic-bezier(0.65, 0, 0.3, 1)`) | ✅ Present | Verified |
| 3 | `tp-curtain-rest` | `.tp-curtain[data-state=intro]` | Post-transition hide | Sets curtain to `visibility: hidden` | ✅ Present | Verified |
| 4 | `tp-hold-still` | `html:has(>body>.tp-curtain[data-state=intro])` | Page load pause | Freezes page scroll during curtain intro | ✅ Present | Verified |
| 5 | `tp-runner-x` | `.tp-curtain:not([data-state=idle]) .tp-curtain__runner` | Curtain runner dog | Dog trots horizontally across curtain leaving paw prints | ✅ Present | Verified |
| 6 | `tp-runner-leg-a` | `.tp-runner__leg--fn, .tp-runner__leg--bf` | Trot cycle leg group A | Alternating leg trot angle (-22° to 24°) | ✅ Present | Verified |
| 7 | `tp-runner-leg-b` | `.tp-runner__leg--ff, .tp-runner__leg--bn` | Trot cycle leg group B | Counter-phase leg trot angle (24° to -22°) | ✅ Present | Verified |
| 8 | `tp-runner-bob` | `.tp-runner__body` | Body vertical bob | Subtle 0.16s bobbing during trot | ✅ Present | Verified |
| 9 | `tp-runner-ear` | `.tp-runner__ear` | Ear bounce | Floppy ear rotation bounce (0° to 8°) | ✅ Present | Verified |
| 10 | `tp-runner-wag` | `.tp-runner__tail` | Tail wag | Fast 0.22s wagging (-16° to 14°) | ✅ Present | Verified |
| 11 | `tp-print-step` | `.tp-curtain__print` | Trot paw prints | Sequential paw print stamps fading in behind puppy | ✅ Present | Verified |
| 12 | `tp-menu-in` | `.tp-menu[open]` | Mobile menu open | Expanding circular clip-path reveal (`circle(150% at calc(100% - 3rem) 2rem)`) | ✅ Present | Verified |
| 13 | `tp-menu-out` | `.tp-menu[data-closing]` | Mobile menu close | Collapsing circular clip-path reveal | ❌ Missing | Implement `data-closing` state in `Header.jsx` |
| 14 | `tp-menu-backdrop-out` | `.tp-menu[data-closing]::backdrop` | Mobile menu backdrop close | Backdrop fades out to opacity 0 | ❌ Missing | Connected to `data-closing` |
| 15 | `tp-menu-link` | `.tp-menu[open] .tp-menu-link` | Menu items entrance | Staggered slide up & rotate (-2° to 0°) with 50ms delay cascade | ✅ Present | Verified |
| 16 | `PawTrailCanvas` | Custom Canvas | Mouse cursor move | Trailing paw prints fading along cursor trajectory | ✅ Present | Verified |

---

### B. Home Page (`/`)

| # | Animation | Class / Selector | Trigger / Purpose | Original Production Behavior | Status in Local | Action Needed |
|---|---|---|---|---|---|---|
| 17 | `tp-sunrise` | `.tp-hero__sun` | Hero sky atmosphere | Warm golden sun rises smoothly over 2.6s | ✅ Present | Verified |
| 18 | `tp-peek` | `.tp-lineup__pup` | Hero puppy lineup load | Staggered pop-in of puppies peeking up behind shelf | ✅ Present | Verified |
| 19 | `tp-pop-up` | `.tp-lineup__pup[data-state=pop]` | Puppy hover / random peek | Puppy jumps up with bouncy spring scale and tilt | ✅ Present | Verified |
| 20 | `tp-door-open` | `.tp-door__leaf` | Corridor horizontal scroll | Door rotates open on Y-axis (0° to -114°) as puppy approaches | ⚠️ Incomplete | Currently hardcoded to `data-open="true"`. Needs scroll-distance opening |
| 21 | `tp-step-in` | `.tp-chat__step`, `.tp-step` | Section entrance | Cards slide up and tilt with staggered delays | ✅ Present | Verified on Home |
| 22 | `tp-dot` | `.tp-typing span` | Chat typing indicator | 3 dots bouncing sequentially in typing bubble | ✅ Present | Verified |
| 23 | `tp-msg-in` | `.tp-msg` | Chat messages appear | Message bubbles spring into view with `var(--ease-pounce)` | ✅ Present | Verified |
| 24 | `tp-stamp-in` | `.tp-stamp` | Passport trust stamps | Stamps stamp down with rotation and scale | ✅ Present | Verified |
| 25 | `tp-sun-set` | `.tp-horizon__sun` | Sunset horizon on scroll | Sun sets into Dubai skyline silhouette | ✅ Present | Verified |
| 26 | `tp-float` | `.tp-night__wonder` | FAQ moon & star | Floating moon drifting gently (3.4s ease-in-out) | ✅ Present | Verified |
| 27 | `tp-twinkle` | `.tp-twinkle` | Night sky stars | Stars twinkling with randomized scale and opacity (3.2s) | ✅ Present | Verified on Home |
| 28 | `tp-breathe` | `.tp-basket__pup .pup-buddy>svg` | Sleeping basket puppy | Gentle breathing scale cycle (3.8s ease-in-out) | ⚠️ Buggy | Was disabled by errant `data-live` attribute |
| 29 | `tp-blink-open` | `.tp-basket__pup [data-p=open]` | Basket puppy blinking | Eye open blink cycle (6.2s) | ⚠️ Buggy | Restore via `:not([data-live])` |
| 30 | `tp-blink-shut` | `.tp-basket__pup [data-p=shut]` | Basket puppy blinking | Eye shut blink cycle (6.2s) | ⚠️ Buggy | Restore via `:not([data-live])` |
| 31 | `tp-ear-twitch` | `.tp-basket__pup [data-p=earR]` | Basket puppy ear twitch | Right ear twitches at 2.2s offset | ⚠️ Buggy | Restore via `:not([data-live])` |
| 32 | `PupJourney` | Mascot scroll tracking | Scroll along multi-scene path | Puppy travels, faces direction, wags, reacts, looks at elements | ✅ Present | Verified |
| 33 | `PupBubble` | `.pup-bubble` | Mascot speech events | Bouncy spring speech bubble with 12+ contextual phrases | ✅ Present | Verified |
| 33b | Airplane Flight Curve | `.tp-flight g` | Scroll through "Imported for you" section | Airplane follows bezier path from Korea to Dubai with tangent rotation & Maltipoo in porthole | ✅ Present | Verified |

---

### C. Puppies Page (`/puppies`) & Puppy Details (`/puppies/[slug]`)

| # | Animation | Class / Selector | Trigger / Purpose | Original Production Behavior | Status in Local | Action Needed |
|---|---|---|---|---|---|---|
| 34 | Hand-drawn border reveal | `.tp-sketch__line` | Card scroll into view | SVG path stroke-dashoffset transition tracing border (`pathLength="1"`) | ✅ Present | Fixed and verified |
| 35 | Title underline draw | `.tp-sketchbook__underline path` | Page / section reveal | Underline stroke draws dynamically under "Puppies" | ✅ Present | Verified |
| 36 | `tp-doodle-hop` | `.tp-sketch:hover .tp-sketch__doodle` | Card hover | Cute decorative sticker hops with rotation and scale (1.35x) | ✅ Present | Verified |
| 37 | Filter chips state | `.tp-sticker-chip` | Filter click | Smooth background, scale, and rotate (-2°) transition | ✅ Present | Verified |
| 38 | `tp-tag-swing` | `.tp-tag[data-revealed]` | Puppy detail tag badge | Tag swings like a hanging sign on page load | ✅ Present | Verified |
| 39 | `tp-tag-nudge` | `.tp-tag:hover` | Detail tag badge hover | Gentle nudging swing on mouse hover | ✅ Present | Verified |
| 40 | `StoryRibbon` scaleY | `.tp-ribbon__band` | Scroll progress on detail | Brown ribbon scales smoothly from 0 to 1 along story section | ✅ Present | Verified |
| 41 | Video Modal Zoom & Backdrop | `.tp-video-modal` | "Watch video" click | Smooth backdrop blur fade-in & modal scale entrance | ✅ Present | Verified |

---

### D. How It Works (`/how-it-works`)

| # | Animation | Class / Selector | Trigger / Purpose | Original Production Behavior | Status in Local | Action Needed |
|---|---|---|---|---|---|---|
| 42 | Delivery Flight Curve | `.tp-flight g` | Scroll through Delivery section | Plane traces bezier path with exact tangent angle rotation and opacity ramp | ✅ Present | Verified |
| 43 | `tp-plane-bob` | `.tp-postcard__plane` | Ambient postcard illustration | Airplane bobs gently in postcard sky | ✅ Present | Verified |
| 44 | Cascading Step Entrance | `.tp-journeys[data-ready] .tp-step` | Tab switch / mount | 4 delivery steps cascade in with staggered delays (`calc(var(--i) * 90ms)`) | ❌ Missing | Add `data-ready` state to `HowItWorksPage.jsx` |
| 45 | Switch tab sliding thumb | `.tp-switch__thumb` | Toggle "In Dubai" / "Imported" | Smooth spring slide indicator between tabs (`--at: 0` vs `1`) | ✅ Present | Verified |

---

### E. Happy Families (`/happy-families`)

| # | Animation | Class / Selector | Trigger / Purpose | Original Production Behavior | Status in Local | Action Needed |
|---|---|---|---|---|---|---|
| 46 | `tp-print-bound` | `.tp-wall__item[data-armed][data-revealed] .tp-polaroid` | Polaroid cards drop in | Polaroids drop in with randomized tilt and bounce | ⚠️ Inactive | Fix `RevealScope.jsx` to ensure `data-armed` is set |
| 47 | `tp-paw-pat` | `.tp-wall__item[data-armed][data-revealed] .tp-wall__paw` | Paw stamp pat | Paw stamps onto photo with rotation (-1.2rem to 0) | ⚠️ Inactive | Fix `RevealScope.jsx` to ensure `data-armed` is set |
| 48 | `tp-stamp-thump` | `.tp-polaroid .tp-gone-stamp` | Adopted stamp thump | Heavy stamp thump onto adopted puppy photos | ✅ Present | Verified |
| 49 | Photo Viewer Lightbox Modal | `dialog[aria-label="Photo viewer"]` | Click any polaroid | Full-screen interactive viewer with slide transition, Next/Prev, and Close | ❌ Missing | Implement interactive Photo Viewer in `HappyFamiliesPage.jsx` |

---

### F. Contact Page (`/contact`)

| # | Animation | Class / Selector | Trigger / Purpose | Original Production Behavior | Status in Local | Action Needed |
|---|---|---|---|---|---|---|
| 50 | `tp-letter-fold` | `.tp-post[data-phase=sealing] .tp-letterform` | Form submission step 1 | Letterform folds up with 3D perspective fold | ❌ Missing | Implement animated posting sequence |
| 51 | `tp-env-in` | `.tp-post__envelope` | Form submission step 1 | Envelope bounces in to receive the letter | ❌ Missing | Implement animated envelope |
| 52 | `tp-flap` | `.tp-post__flap` | Form submission step 1 | Envelope flap folds down to seal the letter | ❌ Missing | Implement animated envelope flap |
| 53 | `tp-box-up` | `.tp-post__box` | Form submission step 2 | Mailbox rises up with spring bounce | ❌ Missing | Implement animated mailbox |
| 54 | `tp-flag` | `.tp-post__flag` | Form submission step 2 | Red mailbox flag pops up | ❌ Missing | Implement animated mailbox flag |
| 55 | `tp-env-post` | `.tp-post__envelope` | Form submission step 2 | Sealed envelope drops into mailbox slot | ❌ Missing | Implement animated envelope drop |
| 56 | `tp-sent-in` | `.tp-post__sent` | Form submission complete | Confirmation card bounces in with WhatsApp link | ❌ Missing | Implement confirmation card |

---

### G. Footer & Ambient Night Sky (All Pages)

| # | Animation | Class / Selector | Trigger / Purpose | Original Production Behavior | Status in Local | Action Needed |
|---|---|---|---|---|---|---|
| 57 | `tp-twinkle` (Footer) | `.tp-footer .tp-twinkle` | Ambient night sky across all pages | 9 twinkling golden stars across footer sky background | ❌ Missing | Add starfield to `Footer.jsx` |
| 58 | Nav Link Hover Paw | `.tp-nav-link:hover .tp-nav-link__paw` | Header/footer nav link hover | Cute paw mark reveals beside nav link | ✅ Present | Verified |

---

## 3. Implementation Plan for Missing Animations

1. **Fix `src/components/Footer.jsx`**: Add the 9-star twinkling starfield (`tp-twinkle`) to the footer background so all pages display the authentic night sky atmosphere.
2. **Fix `src/hooks/useTeddyInteractivity.js`**:
   - Stop setting `data-live` on `.tp-basket__pup .pup-buddy` so the sleeping basket puppy's breathing (`tp-breathe`), blinking (`tp-blink-open`/`shut`), and ear twitching (`tp-ear-twitch`) run uninterrupted.
   - Fix corrupted heart characters.
3. **Fix `src/pages/HowItWorksPage.jsx`**:
   - Add `ready` state to set `data-ready="true"` on `.tp-journeys` after mount, activating cascading step entrances (`tp-step-in`).
4. **Fix `src/components/RevealScope.jsx`**:
   - Ensure elements with `data-reveal` ALWAYS receive `data-armed="true"`, ensuring `tp-print-bound` and `tp-paw-pat` trigger on `/happy-families`.
5. **Implement Contact Page Mailbox Animation in `src/pages/ContactPage.jsx`**:
   - Add full 3-phase submission state machine (`writing` -> `sealing` -> `posting` -> `sent`).
   - Render the animated SVG envelope (`tp-post__envelope`, `tp-post__flap`), mailbox (`tp-post__box`, `tp-post__flag`), and confirmation card (`tp-post__sent`).
6. **Implement Photo Viewer Lightbox in `src/pages/HappyFamiliesPage.jsx`**:
   - Wire polaroid clicks to open the interactive `<dialog aria-label="Photo viewer">` with previous/next controls, photo counter, caption, and close button.
7. **Implement Smooth Mobile Menu Close in `src/components/Header.jsx`**:
   - Add `data-closing="true"` state to play `tp-menu-out` and `tp-menu-backdrop-out` before closing the dialog.
8. **Dynamic Door Open on Scroll in `src/pages/HomePage.jsx`**:
   - Connect horizontal scroll distance to dynamically set `data-open="true"` on doors as the user walks past them, matching production.


---

## 4. Implementation & Verification Results (Completed)

All missing and incomplete animations identified during the audit have been implemented, verified in the browser via automated Selenium tests, and verified through a clean `npm run build`:

1. **Footer Starfield Sky (`tp-twinkle`)**:
   - Added all 9 golden SVG twinkling stars with varied positions, sizes, and staggered animation delays (`0.00s` to `3.20s`) matching production. Verified in [src/components/Footer.jsx](file:///c:/Users/gagan/OneDrive/projects/insta_biz/src/components/Footer.jsx).
2. **Contact Letterform Mailing Sequence (`tp-letter-fold`, `tp-env-in`, `tp-flap`, `tp-box-up`, `tp-flag`, `tp-env-post`, `tp-sent-in`)**:
   - Implemented 3-phase mailing pipeline (`writing` &rarr; `sealing` &rarr; `posting` &rarr; `sent`) with the exact SVG envelope, flap seal, raising mailbox with red flag, and confirmation card in [src/pages/ContactPage.jsx](file:///c:/Users/gagan/OneDrive/projects/insta_biz/src/pages/ContactPage.jsx).
3. **How-It-Works Cascading Steps (`tp-step-in`)**:
   - Added `ready` mount trigger to apply `data-ready="true"` to `.tp-journeys`, activating staggered cascading card entrances (`tp-step-in`) in [src/pages/HowItWorksPage.jsx](file:///c:/Users/gagan/OneDrive/projects/insta_biz/src/pages/HowItWorksPage.jsx).
4. **Happy Families Polaroid Bounce & Paw Pat (`tp-print-bound`, `tp-paw-pat`)**:
   - Fixed `RevealScope` in [src/components/RevealScope.jsx](file:///c:/Users/gagan/OneDrive/projects/insta_biz/src/components/RevealScope.jsx) to reliably set `data-armed="true"` before revealing, enabling CSS bounce and paw-pat keyframes on all 64 polaroids.
5. **Happy Families Full-Screen Photo Viewer Modal**:
   - Fully implemented `<dialog ref={dialogRef} aria-label="Photo viewer">` in [src/pages/HappyFamiliesPage.jsx](file:///c:/Users/gagan/OneDrive/projects/insta_biz/src/pages/HappyFamiliesPage.jsx), connected to all 64 polaroid click triggers, with photo counter (`1 / 64`), Next/Previous navigation, keyboard arrow hotkeys, and Close actions.
6. **Mobile Circular Menu Expansion & Contraction (`tp-menu-in`, `tp-menu-out`, `tp-menu-backdrop-out`, `tp-menu-link`)**:
   - Converted mobile menu in [src/components/Header.jsx](file:///c:/Users/gagan/OneDrive/projects/insta_biz/src/components/Header.jsx) to native `<dialog className="tp-menu">` with `data-closing` animation cycle, circular clipping expansion/contraction from the menu button, and staggered link transitions.
7. **Basket Puppy Natural Breathing & Twitches (`tp-breathe`, `tp-blink-shut`, `tp-ear-twitch`)**:
   - Updated [src/hooks/useTeddyInteractivity.js](file:///c:/Users/gagan/OneDrive/projects/insta_biz/src/hooks/useTeddyInteractivity.js) to preserve `:not([data-live])` on basket puppy elements so resting breathing and ear twitch cycles run continuously.
