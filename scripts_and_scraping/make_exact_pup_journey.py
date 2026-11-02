import re

# Read parts
with open('scripts_and_scraping/teddy_svg_jsx.txt', 'r', encoding='utf-8') as f:
    svg_jsx = f.read()

paw_path = "M32 30.5c-7.6 0-15.6 8.3-15.6 15.5 0 5.4 4.2 8.3 9.2 8.3 2.6 0 4.5-1.1 6.4-1.1s3.8 1.1 6.4 1.1c5 0 9.2-2.9 9.2-8.3 0-7.2-8-15.5-15.6-15.5zM14.6 22.3c-3 .1-5.6 3.3-5.6 7s2.6 6.9 5.6 6.9 5.6-3.2 5.6-6.9-2.6-7-5.6-7zM24.2 9.3c-3 0-5.6 3.3-5.6 7.3s2.5 7.3 5.6 7.3 5.6-3.3 5.6-7.3-2.5-7.3-5.6-7.3zM39.8 9.3c-3.1 0-5.6 3.3-5.6 7.3s2.5 7.3 5.6 7.3 5.6-3.3 5.6-7.3-2.5-7.3-5.6-7.3zM49.4 22.3c-3 0-5.6 3.3-5.6 7s2.6 6.9 5.6 6.9 5.6-3.2 5.6-6.9-2.6-7-5.6-7z"

script_content = f'''import React, {{ useEffect, useRef }} from 'react';

// --- Teddy Character Math & Curves ---
function genCurve(cx, cy, rx, ry, bumps, amp, startAngle = -Math.PI / 2, rotDeg = 0) {{
  const rot = (rotDeg * Math.PI) / 180;
  const pt = (angle, offset) => {{
    const x = Math.cos(angle) * (rx + offset);
    const y = Math.sin(angle) * (ry + (ry / rx) * offset);
    return `${{(cx + x * Math.cos(rot) - y * Math.sin(rot)).toFixed(1)}} ${{(
      cy +
      x * Math.sin(rot) +
      y * Math.cos(rot)
    ).toFixed(1)}}`;
  }};
  let d = '';
  for (let i = 0; i < bumps; i++) {{
    const a1 = startAngle + (i / bumps) * Math.PI * 2;
    const a2 = startAngle + ((i + 1) / bumps) * Math.PI * 2;
    const mid = (a1 + a2) / 2;
    d += `${{i === 0 ? `M${{pt(a1, 0)}}` : ''}}Q${{pt(mid, 2.1 * amp)}} ${{pt(a2, 0)}}`;
  }}
  return `${{d}}Z`;
}}

const P_BODY_ORIGIN = [196, 206];
const P_HEAD_ORIGIN = [212, 100];
const P_SHOULDER_N = [186, 194];
const P_SHOULDER_F = [168, 192];
const P_HIP_N = [110, 194];
const P_HIP_F = [94, 192];
const P_TAIL_BASE = [84, 150];
const P_EAR_L = [174, 82];
const P_EAR_R = [250, 82];

const PATHS = {{
  body: genCurve(140, 170, 64, 36, 15, 3.4, 0.95 * Math.PI),
  chest: genCurve(192, 166, 30, 32, 9, 3.2, 0.6 * Math.PI),
  tail: genCurve(70, 126, 17, 16, 9, 3.2),
  tailStem: 'M86 152 C80 146 76 140 74 136',
  haunch: genCurve(110, 204, 30, 24, 10, 3.2, Math.PI),
  haunchPaw:
    'M112 214 C126 212 142 214 146 221 C148 226 144 229 136 229 L116 229 C108 229 104 224 106 219 Z',
  head: genCurve(212, 100, 51, 46, 16, 3.6),
  topknot: genCurve(212, 52, 17, 12, 8, 2.9, Math.PI),
  earL: genCurve(170, 112, 19, 34, 10, 3.2, -Math.PI / 2, 12),
  earR: genCurve(254, 112, 19, 34, 10, 3.2, -Math.PI / 2, -12),
  muzzle:
    'M188 120 C188 106 200 100 212 100 C224 100 236 106 236 120 C236 133 225 140 212 140 C199 140 188 133 188 120 Z',
  nose: 'M204.5 111.5 Q212 107.2 219.5 111.5 Q218.2 118.4 212 120 Q205.8 118.4 204.5 111.5 Z',
  mouth:
    'M212 120 V124.5 M212 124.5 Q207.2 129.6 202.8 125.2 M212 124.5 Q216.8 129.6 221.2 125.2',
  mouthOpen: 'M203 126 Q212 122 221 126 Q219 138 212 139 Q205 138 203 126 Z',
  tongue: 'M207.6 127.4 Q212 136.6 216.4 127.4 Z',
  collar: 'M178 146 Q212 162 246 146 L246 154 Q212 170 178 154 Z',
  tag: 'M212 160 C212 156 206 155 206 159.4 C206 163 212 166.6 212 168.4 C212 166.6 218 163 218 159.4 C218 155 212 156 212 160 Z',
  ledgePaws:
    'M175 159 C175 148 181 142 190 142 C199 142 205 148 205 159 Z M219 159 C219 148 225 142 234 142 C243 142 249 148 249 159 Z',
  ledgeToes: 'M186 153 v-4.5 M194 153 v-4.5 M230 153 v-4.5 M238 153 v-4.5',
  shadow: {{ cx: 150, cy: 230, rx: 92, ry: 7 }},
}};

function genLeg(w, h) {{
  const half = w / 2;
  return `M${{-half}} -14 C${{-half}} 4 -12 ${{h - 18}} -12 ${{h - 9}} C-12 ${{h - 2}} -7 ${{
    h
  }} 0 ${{h}} C9 ${{h}} 13 ${{h - 3}} 13 ${{h - 9}} C13 ${{h - 18}} ${{half}} 4 ${{half}} -14`;
}}

const LEGS = {{
  front: genLeg(24, 228 - P_SHOULDER_N[1]),
  frontFar: genLeg(22, 228 - P_SHOULDER_F[1]),
  back: genLeg(30, 228 - P_HIP_N[1]),
  backFar: genLeg(28, 228 - P_HIP_F[1]),
}};

const BASE_POSE = {{
  bodyRot: 0,
  bodyX: 0,
  bodyY: 0,
  stretch: 1,
  headX: 0,
  headY: 0,
  headRot: 0,
  earL: 0,
  earR: 0,
  tail: 0,
  fn: 0,
  ff: 0,
  bn: 0,
  bf: 0,
  sit: 0,
  eyes: 1,
  happy: 0,
  tongue: 0,
  mouth: 0,
  front: 0,
}};

const POSES = {{
  stand: BASE_POSE,
  walk: {{ ...BASE_POSE, tail: -6, tongue: 1 }},
  sit: {{ ...BASE_POSE, bodyRot: -24, bodyY: -2, headX: -10, headY: -6, tail: 34, sit: 1, tongue: 1 }},
  peek: {{ ...BASE_POSE, headY: 4, earL: -6, earR: 6, tail: -20, front: 1, tongue: 1 }},
  snug: {{ ...BASE_POSE, headY: 9, headRot: 4, earL: 3, earR: -3, tail: -20, front: 1, tongue: 0 }},
  lie: {{
    ...BASE_POSE,
    bodyRot: -5,
    bodyY: 22,
    headX: 12,
    headY: 40,
    headRot: 3,
    fn: -84,
    ff: -80,
    sit: 1,
    tail: 58,
    tongue: 0,
  }},
  sleep: {{
    ...BASE_POSE,
    bodyRot: -5,
    bodyY: 22,
    headX: 14,
    headY: 44,
    headRot: -8,
    fn: -84,
    ff: -80,
    sit: 1,
    tail: 64,
    eyes: 0,
    earL: 4,
    earR: -4,
  }},
  settle: {{
    ...BASE_POSE,
    bodyRot: -5,
    bodyY: 22,
    headX: 10,
    headY: 16,
    fn: -84,
    ff: -80,
    sit: 1,
    tail: 40,
    tongue: 1,
  }},
  hop: {{
    ...BASE_POSE,
    bodyRot: -9,
    stretch: 1.06,
    headY: -6,
    fn: -42,
    ff: -32,
    bn: 40,
    bf: 30,
    earL: -26,
    earR: 26,
    tail: -24,
    tongue: 1,
  }},
  sniff: {{ ...BASE_POSE, bodyRot: 7, headX: 16, headY: 32, headRot: 9, tail: -14, fn: 6, ff: 4 }},
  bow: {{
    ...BASE_POSE,
    bodyRot: 15,
    bodyY: 2,
    headX: 14,
    headY: 30,
    fn: -58,
    ff: -52,
    tail: -32,
    happy: 1,
    tongue: 1,
  }},
  beg: {{
    ...BASE_POSE,
    bodyRot: -36,
    bodyY: -6,
    headX: -18,
    headY: -18,
    sit: 1,
    fn: -70,
    ff: -64,
    tail: 30,
    happy: 1,
    tongue: 1,
  }},
}};

const POSE_KEYS = Object.keys(BASE_POSE);

function lerpPose(p1, p2, t) {{
  const res = {{ ...p1 }};
  for (const k of POSE_KEYS) {{
    res[k] = p1[k] + (p2[k] - p1[k]) * t;
  }}
  return res;
}}

const round2 = (num) => Math.round(100 * num) / 100;
const rotStr = (deg, [x, y]) => `rotate(${{round2(deg)}} ${{x}} ${{y}})`;

function computeFrame(pose, state) {{
  const phaseSin = Math.sin(state.phase);
  const phaseSinOpp = Math.sin(state.phase + Math.PI);
  const legAmp = 20 + 10 * state.stride;
  const bobbing = (1 - Math.cos(2 * state.phase)) / 2;
  const isMoving = state.stride > 0.01 ? 1 : 0;
  const idleBreathe = Math.sin(2.4 * state.time) * (1 - isMoving);

  const bodyY = pose.bodyY - bobbing * (2.5 + 4 * state.stride) * isMoving + 0.6 * idleBreathe;
  const bodyRot = pose.bodyRot + 1.6 * Math.sin(state.phase) * isMoving;
  const invBodyRot = -pose.bodyRot;

  const wagAmp = 5 + 17 * state.wag;
  const wagFreq = 1.2 + 2.6 * state.wag;
  const tailRot = pose.tail + Math.sin(state.time * wagFreq * Math.PI * 2) * wagAmp;

  const headBob =
    -((1 - Math.cos(2 * state.phase - 0.7)) / 2) * (2 + 3 * state.stride) * isMoving + 0.9 * idleBreathe;

  return {{
    body: `translate(${{round2(pose.bodyX)}} ${{round2(bodyY)}}) ${{rotStr(
      bodyRot,
      P_BODY_ORIGIN
    )}} translate(${{P_BODY_ORIGIN[0]}} 0) scale(${{round2(pose.stretch)}} 1) translate(${{
      -P_BODY_ORIGIN[0]
    }} 0)`,
    fn: `translate(${{P_SHOULDER_N[0]}} ${{P_SHOULDER_N[1]}}) rotate(${{round2(
      pose.fn + invBodyRot + phaseSin * legAmp * isMoving
    )}})`,
    ff: `translate(${{P_SHOULDER_F[0]}} ${{P_SHOULDER_F[1]}}) rotate(${{round2(
      pose.ff + invBodyRot + phaseSinOpp * legAmp * isMoving
    )}})`,
    bn: `translate(${{P_HIP_N[0]}} ${{P_HIP_N[1]}}) rotate(${{round2(
      pose.bn + phaseSinOpp * legAmp * isMoving
    )}})`,
    bf: `translate(${{P_HIP_F[0]}} ${{P_HIP_F[1]}}) rotate(${{round2(
      pose.bf + phaseSin * legAmp * isMoving
    )}})`,
    tail: rotStr(tailRot, P_TAIL_BASE),
    haunch: `translate(0 ${{round2(-0.06 * pose.bodyRot)}})`,
    head: `translate(${{round2(pose.headX)}} ${{round2(pose.headY + headBob)}}) ${{rotStr(
      pose.headRot + 1.4 * Math.sin(state.phase) * isMoving,
      P_HEAD_ORIGIN
    )}}`,
    earL: rotStr(pose.earL + state.ear + 4 * Math.sin(2 * state.phase) * isMoving, P_EAR_L),
    earR: rotStr(pose.earR - state.ear - 4 * Math.sin(2 * state.phase) * isMoving, P_EAR_R),
    eyes: `translate(${{round2(3.4 * state.gazeX)}} ${{round2(2.6 * state.gazeY)}})`,
    blink: `translate(0 ${{round2(98 * state.blink * 0.92)}}) scale(1 ${{round2(
      1 - 0.92 * state.blink
    )}})`,
    openEyes: round2(Math.max(0, pose.eyes - pose.happy)),
    happyEyes: round2(Math.min(pose.happy, pose.eyes)),
    shutEyes: round2(1 - pose.eyes),
    tongue: round2(pose.tongue * (1 - pose.mouth)),
    mouth: round2(pose.mouth),
    backLegs: round2(1 - pose.sit),
    haunchOpacity: round2(pose.sit * (1 - pose.front)),
    side: round2(1 - pose.front),
    ledge: round2(pose.front),
    shadow: `translate(${{round2(0.6 * pose.bodyX)}} 0) scale(${{round2(1 - 0.05 * bobbing * isMoving)}} 1)`,
    shadowOpacity: round2(0.12 * (1 - pose.front)),
  }};
}}

const TRANSFORM_MAP = [
  ['root', 'transform', 'root'],
  ['shadow', 'transform', 'shadow'],
  ['shadow', 'opacity', 'shadowOpacity'],
  ['body', 'transform', 'body'],
  ['body', 'opacity', 'side'],
  ['bf', 'transform', 'bf'],
  ['bf', 'opacity', 'backLegs'],
  ['bn', 'transform', 'bn'],
  ['bn', 'opacity', 'backLegs'],
  ['ff', 'transform', 'ff'],
  ['fn', 'transform', 'fn'],
  ['tail', 'transform', 'tail'],
  ['haunch', 'transform', 'haunch'],
  ['haunch', 'opacity', 'haunchOpacity'],
  ['head', 'transform', 'head'],
  ['earL', 'transform', 'earL'],
  ['earR', 'transform', 'earR'],
  ['eyes', 'transform', 'eyes'],
  ['open', 'opacity', 'openEyes'],
  ['blink', 'transform', 'blink'],
  ['happy', 'opacity', 'happyEyes'],
  ['shut', 'opacity', 'shutEyes'],
  ['tongue', 'opacity', 'tongue'],
  ['mouth', 'opacity', 'mouth'],
  ['ledge', 'opacity', 'ledge'],
];

const expStep = (dt, tau) => 1 - Math.exp(-dt / tau);
const clampVal = (val, min = -1, max = 1) => Math.max(min, Math.min(max, val));

class PupController {{
  constructor(svg, initialPose = 'sit', facing = 1) {{
    this.svg = svg;
    this.els = new Map();
    this.written = new Map();
    this.m = {{ phase: 0, stride: 0, time: 0, wag: 0.35, gazeX: 0, gazeY: 0, blink: 0, ear: 0 }};
    this.strideTarget = 0;
    this.wagTarget = 0.35;
    this.gazeTarget = {{ x: 0, y: 0 }};
    this.tilt = 0;
    this.tiltTarget = 0;
    this.earV = 0;
    this.nextBlink = 1.2;
    this.blinkAt = -1;
    this.woofUntil = 0;
    this.bounce = 0;
    this.bounceV = 0;
    this.offset = 0;
    this.offsetTarget = 0;
    this.pet = 0;
    this.petTarget = 0;
    this.turn = 0.07;
    this.lean = 0;

    svg.querySelectorAll('[data-p]').forEach((el) => {{
      this.els.set(el.dataset.p, el);
    }});

    this.pose = {{ ...(POSES[initialPose] || POSES.sit) }};
    this.target = this.pose;
    this.facing = facing;
    this.facingTarget = facing;
  }}

  setPose(pose) {{
    this.target = typeof pose === 'string' ? POSES[pose] || POSES.stand : pose;
  }}

  jump(pose, facing) {{
    this.pose = {{ ...(POSES[pose] || POSES.stand) }};
    this.target = this.pose;
    if (facing) this.facing = this.facingTarget = facing;
  }}

  face(dir, turn = 0.07) {{
    this.facingTarget = dir;
    this.turn = turn;
  }}

  get facingDir() {{
    return this.facingTarget;
  }}

  stride(val) {{
    this.strideTarget = clampVal(val, 0, 1);
  }}

  advance(dist) {{
    this.m.phase += (dist / 46) * Math.PI;
  }}

  walkedTo(dist) {{
    this.m.phase = (dist / 46) * Math.PI;
  }}

  wag(val) {{
    this.wagTarget = clampVal(val, 0, 1);
  }}

  cock(deg) {{
    this.tiltTarget = deg;
  }}

  lookAt(target) {{
    if (!target) {{
      this.gazeTarget = {{ x: 0, y: 0 }};
      return;
    }}
    const rect = this.svg.getBoundingClientRect();
    const eyeX = this.facingTarget > 0 ? P_HEAD_ORIGIN[0] : 300 - P_HEAD_ORIGIN[0];
    const originX = rect.left + (eyeX / 300) * rect.width;
    const originY = rect.top + (98 / 240) * rect.height;
    const dx = target.x - originX;
    const dy = target.y - originY;
    const dist = Math.hypot(dx, dy) || 1;
    const factor = Math.min(1, dist / 160);
    this.gazeTarget = {{
      x: (dx / dist) * factor * this.facingTarget,
      y: (dy / dist) * factor,
    }};
  }}

  woof(time) {{
    this.woofUntil = time + 0.34;
    this.bounceV = -150;
    this.earV += 260;
  }}

  jolt(mult = 1) {{
    this.earV += 220 * mult;
  }}

  hop(mult = 1) {{
    this.bounceV = -230 * mult;
    this.earV += 200 * mult;
  }}

  yawn(time, dur = 0.9) {{
    this.woofUntil = time + dur;
  }}

  dash(val) {{
    this.offsetTarget = val;
  }}

  petting(bool) {{
    this.petTarget = bool ? 1 : 0;
  }}

  reset() {{
    this.offsetTarget = 0;
    this.tiltTarget = 0;
    this.petTarget = 0;
  }}

  tick(dt, time) {{
    dt = Math.min(dt, 0.05);
    const s = this.m;
    s.time = time;

    this.pose = lerpPose(this.pose, this.target, expStep(dt, 0.16));
    this.facing += (this.facingTarget - this.facing) * expStep(dt, this.turn);

    s.stride += (this.strideTarget - s.stride) * expStep(dt, 0.12);
    if (s.stride < 0.012 && this.strideTarget === 0) s.stride = 0;

    s.wag += (this.wagTarget - s.wag) * expStep(dt, 0.4);
    s.gazeX += (this.gazeTarget.x - s.gazeX) * expStep(dt, 0.07);
    s.gazeY += (this.gazeTarget.y - s.gazeY) * expStep(dt, 0.07);

    this.tilt += (this.tiltTarget + 3 * s.gazeX - this.tilt) * expStep(dt, 0.18);
    this.earV += (-150 * s.ear - 10 * this.earV) * dt;
    s.ear = clampVal(s.ear + this.earV * dt, -28, 28);

    this.bounceV += (-260 * this.bounce - 16 * this.bounceV) * dt;
    this.bounce += this.bounceV * dt;

    const prevOffset = this.offset;
    this.offset += (this.offsetTarget - this.offset) * expStep(dt, 0.2);
    if (Math.abs(this.offsetTarget - this.offset) < 0.05) this.offset = this.offsetTarget;
    const deltaOff = Math.abs(this.offset - prevOffset);
    if (deltaOff) this.advance(deltaOff);

    const speed = dt > 0 ? Math.min(1, deltaOff / dt / 180) : 0;
    this.pet += (this.petTarget - this.pet) * expStep(dt, 0.15);

    if (time > this.nextBlink && this.pose.eyes > 0.6) {{
      this.blinkAt = time;
      this.nextBlink = time + 2.2 + 3.8 * Math.random();
      if (Math.random() < 0.18) this.nextBlink = time + 0.32;
    }}

    const blinkPhase = (time - this.blinkAt) / 0.15;
    s.blink = blinkPhase >= 0 && blinkPhase <= 1 ? Math.sin(blinkPhase * Math.PI) : 0;

    const framePose = {{
      ...this.pose,
      headRot: this.pose.headRot + this.tilt,
      bodyRot: this.pose.bodyRot + this.lean,
      bodyY: this.pose.bodyY + this.bounce,
      headY: this.pose.headY + 1.15 * this.bounce,
      mouth: time < this.woofUntil ? 1 : this.pose.mouth,
      happy: Math.max(this.pose.happy, this.pet),
    }};

    const frame = computeFrame(framePose, speed > s.stride ? {{ ...s, stride: speed }} : s);
    const facingSign = Math.abs(this.facing) < 0.02 ? 0.02 * Math.sign(this.facing || 1) : this.facing;
    const rootTransform = `translate(${{this.offset.toFixed(1)}} 0) translate(${{150}} 0) scale(${{facingSign.toFixed(
      3
    )}} 1) translate(${{-150}} 0)`;

    for (const [part, attr, prop] of TRANSFORM_MAP) {{
      const el = this.els.get(part);
      if (!el) continue;
      const val = prop === 'root' ? rootTransform : String(frame[prop]);
      const key = `${{part}}:${{attr}}`;
      if (this.written.get(key) !== val) {{
        el.setAttribute(attr, val);
        this.written.set(key, val);
      }}
    }}
  }}
}}

// --- Curve & Journey Math Helpers ---
const PUP_CENTER = {{ x: 150, y: 228 }};
const PUP_BOX = [48, 30, 288, 236];

const clamp01 = (v) => Math.min(1, Math.max(0, v));
const smooth3 = (v) => v * v * (3 - 2 * v);
const smoothstepClamped = (e0, e1, x) => (e1 === e0 ? (x >= e1 ? 1 : 0) : smooth3(clamp01((x - e0) / (e1 - e0))));
const lerpNum = (a, b, t) => a + (b - a) * t;

const softMin = (e, t, a) => {{
  const s = (e - t) / a;
  return s > 20 ? e : t + a * Math.log1p(Math.exp(s));
}};
const softMax = (e, t, a) => -softMin(-e, -t, a);

function clampToSafe(x, y, scale, box, safe, margin = 8) {{
  const leftOff = (PUP_CENTER.x - box[0]) * scale;
  const rightOff = (box[2] - PUP_CENTER.x) * scale;
  const topOff = (PUP_CENTER.y - box[1]) * scale;
  const botOff = (box[3] - PUP_CENTER.y) * scale;
  let finalX;
  if (safe.right - safe.left > leftOff + rightOff) {{
    finalX = softMax(softMin(x, safe.left + leftOff, margin), safe.right - rightOff, margin);
  }} else {{
    finalX = (safe.left + safe.right) / 2 - (rightOff - leftOff) / 2;
  }}
  let finalY;
  if (safe.bottom - safe.top > topOff + botOff) {{
    finalY = softMax(softMin(y, safe.top + topOff, margin), safe.bottom - botOff, margin);
  }} else {{
    finalY = safe.bottom - botOff;
  }}
  return {{ x: finalX, y: finalY }};
}}

const lerpBox = (b1, b2, t) => [
  lerpNum(b1[0], b2[0], t),
  lerpNum(b1[1], b2[1], t),
  lerpNum(b1[2], b2[2], t),
  lerpNum(b1[3], b2[3], t),
];

const evalBezier = (p0, c1, c2, p1, t) => {{
  const mt = 1 - t;
  const mt2 = mt * mt;
  const mt3 = mt2 * mt;
  const t2 = t * t;
  const t3 = t2 * t;
  return {{
    x: mt3 * p0.x + 3 * mt2 * t * c1.x + 3 * mt * t2 * c2.x + t3 * p1.x,
    y: mt3 * p0.y + 3 * mt2 * t * c1.y + 3 * mt * t2 * c2.y + t3 * p1.y,
  }};
}};

function findHoldIndex(holds, scrollY) {{
  if (!holds.length || scrollY <= holds[0][1]) return {{ k: 0, t: 0 }};
  for (let i = 0; i < holds.length - 1; i++) {{
    const s = holds[i][1];
    const nextStart = holds[i + 1][0];
    if (scrollY < nextStart) return {{ k: i, t: clamp01((scrollY - s) / Math.max(1, nextStart - s)) }};
    if (scrollY <= holds[i + 1][1]) return {{ k: i + 1, t: 0 }};
  }}
  return {{ k: holds.length - 1, t: 0 }};
}}

function getStopPosition(stop, scrollY) {{
  const tr = stop.track;
  let trackY;
  if (tr.kind === 'page') trackY = tr.top - scrollY;
  else if (tr.kind === 'screen') trackY = tr.top;
  else if (scrollY < tr.from) trackY = tr.top - (scrollY - tr.from);
  else if (scrollY > tr.to) trackY = tr.top - (scrollY - tr.to);
  else trackY = tr.top;
  return {{
    x: stop.x + PUP_CENTER.x * stop.s,
    y: trackY + PUP_CENTER.y * stop.s,
  }};
}}

export default function PupJourney() {{
  const layerRef = useRef(null);
  const actorRef = useRef(null);
  const bodyRef = useRef(null);
  const bubbleRef = useRef(null);
  const bubbleAtRef = useRef(null);
  const printsRef = useRef(null);
  const probeRef = useRef(null);

  useEffect(() => {{
    const prefersReducedMotion =
      window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (prefersReducedMotion || window.innerWidth < 1024) {{
      return;
    }}

    const layer = layerRef.current;
    const actor = actorRef.current;
    const body = bodyRef.current;
    const bubble = bubbleRef.current;
    const bubbleAt = bubbleAtRef.current;
    const printsContainer = printsRef.current;

    if (!layer || !actor || !body || !printsContainer) return;

    const svg = body.querySelector('svg');
    if (!svg) return;

    const prints = Array.from(printsContainer.children);
    let printIdx = 0;

    // Initialize the real PupController on the SVG!
    const controller = new PupController(svg, 'peek', 1);

    document.documentElement.dataset.pup = 'live';
    layer.hidden = false;

    let rafId;
    let B = null;
    let K = performance.now() / 1000;
    let lastScrollY = window.scrollY;
    let lastMoveTime = performance.now() / 1000;
    let stopIdx = -1;
    let lastStopIdx = -1;
    let bubbleUntil = 0;
    let walkAccum = 0;
    let prevPos = null;
    let lookTarget = null;

    const say = (text, dur = 1.6) => {{
      if (!bubble) return;
      bubble.textContent = text;
      bubble.dataset.show = 'true';
      bubbleUntil = performance.now() / 1000 + dur;
    }};

    const spawnHearts = () => {{
      const rect = actor.getBoundingClientRect();
      for (let i = 0; i < 5; i++) {{
        const heart = document.createElement('span');
        heart.className = 'pup-heart';
        heart.textContent = '♥';
        heart.style.left = `${{rect.width * 0.5}}px`;
        heart.style.top = `${{rect.height * 0.25}}px`;
        actor.appendChild(heart);
        const offsetX = (Math.random() - 0.5) * 80;
        const offsetY = -60 - Math.random() * 50;
        heart
          .animate(
            [
              {{ transform: 'translate(-50%, 0) scale(0.4)', opacity: 0 }},
              {{ opacity: 1, offset: 0.2 }},
              {{
                transform: `translate(calc(-50% + ${{offsetX.toFixed(0)}}px), ${{offsetY.toFixed(0)}}px) scale(1.15)`,
                opacity: 0,
              }},
            ],
            {{ duration: 1150 + 100 * i, delay: 75 * i, easing: 'cubic-bezier(.2,.7,.3,1)', fill: 'backwards' }}
          )
          .finished.then(
            () => heart.remove(),
            () => heart.remove()
          );
      }}
    }};

    const handleActorClick = () => {{
      const actions = ['woof', 'peekaboo', 'love', 'sneeze', 'hop'];
      const act = actions[Math.floor(Math.random() * actions.length)];
      if (act === 'woof') {{
        controller.woof(performance.now() / 1000);
        say('woof! ♡');
      }} else if (act === 'love') {{
        controller.hop(0.8);
        controller.wag(1);
        say('I like you! ♡');
        spawnHearts();
      }} else if (act === 'peekaboo') {{
        controller.setPose('peek');
        controller.jolt(1.2);
        say('peekaboo!');
      }} else if (act === 'sneeze') {{
        controller.jolt(1.4);
        controller.yawn(performance.now() / 1000, 0.4);
        say('*achoo!*');
      }} else {{
        controller.hop(1.2);
        say('wheee!');
      }}
    }};

    actor.addEventListener('click', handleActorClick);

    // Track pointer for gaze
    const handlePointerMove = (e) => {{
      if (e.pointerType === 'mouse') {{
        controller.lookAt({{ x: e.clientX, y: e.clientY }});
      }}
    }};
    window.addEventListener('pointermove', handlePointerMove, {{ passive: true }});

    // Build Stops & Holds
    const computeStops = () => {{
      const clientW = document.documentElement.clientWidth;
      const headerH = document.getElementById('site-header')?.offsetHeight || 76;
      const safe = {{
        left: 10,
        top: headerH + 10,
        right: clientW - 10,
        bottom: window.innerHeight - 10,
      }};

      const stopEls = Array.from(document.querySelectorAll('[data-pup-stop]')).filter(
        (el) => el.getClientRects().length > 0
      );

      const stops = [];
      const meta = [];
      const holds = [];

      stopEls.forEach((el) => {{
        const rect = el.getBoundingClientRect();
        const pose = el.dataset.pose || 'sit';
        const act = el.dataset.act || '';
        const scale = (rect.width / 300) * (act === 'basket' ? 1 : 1.12);
        const centerOffset = pose === 'peek' ? {{ x: PUP_CENTER.x, y: 159 }} : PUP_CENTER;

        // Sticky detection
        let stickyParent = null;
        for (let p = el.parentElement; p && p !== document.body; p = p.parentElement) {{
          if (getComputedStyle(p).position === 'sticky') {{
            stickyParent = p;
            break;
          }}
        }}

        let track;
        if (!stickyParent) {{
          track = {{ kind: 'page', top: rect.top + window.scrollY }};
        }} else {{
          const stickyTop = parseFloat(getComputedStyle(stickyParent).top) || 0;
          const offsetInside = rect.top - stickyParent.getBoundingClientRect().top;
          track = {{ kind: 'pin', top: stickyTop + offsetInside, from: 0, to: 1000 }};
        }}

        const stop = {{
          x: rect.left + centerOffset.x * ((rect.width / 300) - scale),
          track,
          s: scale,
          behind: el.dataset.behind === 'true',
          sink: 0,
          box: PUP_BOX,
        }};

        const scene = el.closest('[data-pup-scene]');
        stops.push(stop);
        meta.push({{
          scene,
          pose,
          facing: el.dataset.facing === 'left' ? -1 : 1,
          act,
          looks: scene ? Array.from(scene.querySelectorAll('[data-pup-friend], [data-pup-look]')) : [],
        }});

        // Hold range
        const holdY = track.top - (safe.top + 0.45 * (safe.bottom - safe.top));
        holds.push([holdY - 140, holdY + 140]);
      }});

      // Adjust holds
      if (holds.length > 0) {{
        holds[0][0] = -Infinity;
        holds[holds.length - 1][1] = Infinity;
        for (let i = 0; i < holds.length - 1; i++) {{
          if (holds[i + 1][0] < holds[i][1]) {{
            const mid = (holds[i][1] + holds[i + 1][0]) / 2;
            holds[i][1] = mid;
            holds[i + 1][0] = mid;
          }}
        }}
      }}

      B = {{ stops, meta, holds, safe }};
    }};

    computeStops();
    window.addEventListener('resize', computeStops);

    const tick = () => {{
      const now = performance.now() / 1000;
      const dt = Math.min(0.05, now - K);
      K = now;

      const scrollY = window.scrollY;
      const deltaY = scrollY - lastScrollY;
      lastScrollY = scrollY;

      if (Math.abs(deltaY) > 0.5) {{
        lastMoveTime = now;
      }}

      if (B && B.stops.length >= 2) {{
        const {{ k, t }} = findHoldIndex(B.holds, scrollY);
        stopIdx = k;

        const isAtHold = t === 0;

        let curX, curY, curScale, curFront, isAirborne;

        if (isAtHold || k >= B.stops.length - 1) {{
          // At stop
          const stop = B.stops[k];
          const m = B.meta[k];
          const p = getStopPosition(stop, scrollY);
          const clamped = clampToSafe(p.x, p.y, stop.s, stop.box, B.safe);

          curX = clamped.x;
          curY = clamped.y;
          curScale = stop.s;
          curFront = !stop.behind;
          isAirborne = false;

          if (lastStopIdx !== k) {{
            lastStopIdx = k;
            controller.setPose(m.pose);
            controller.face(m.facing, 0.14);
            controller.stride(0);
            controller.wag(m.act === 'basket' ? 0.3 : 0.7);
            controller.jolt(0.4);

            // Look at scene element
            if (m.looks.length > 0) {{
              const friend = m.looks[0];
              const r = friend.getBoundingClientRect();
              lookTarget = {{ x: r.left + r.width / 2, y: r.top + r.height / 2, until: now + 1.6 }};
            }}
          }}
        }} else {{
          // Between stops: evaluate Bezier curve
          lastStopIdx = -1;
          const stop0 = B.stops[k];
          const stop1 = B.stops[k + 1];
          const h0 = B.holds[k][1];
          const h1 = B.holds[k + 1][0];

          const p0 = getStopPosition(stop0, h0);
          const p1 = getStopPosition(stop1, h1);

          const dx = p1.x - p0.x;
          const dy = p1.y - p0.y;
          const dist = Math.hypot(dx, dy);

          const c1 = {{ x: p0.x + (dx >= 0 ? 1 : -1) * Math.max(0.45 * Math.abs(dx), 0), y: p0.y }};
          const c2 = {{ x: p1.x - (dx >= 0 ? 1 : -1) * Math.max(0.45 * Math.abs(dx), 0), y: p1.y }};

          // Quintic smoothstep
          const w = t * t * t * (t * (6 * t - 15) + 10);
          const curvePt = evalBezier(p0, c1, c2, p1, w);

          curScale = lerpNum(stop0.s, stop1.s, smooth3(clamp01(t / 0.65)));
          let arcY = curvePt.y;

          // Emerging from behind quilt arc
          if (stop0.behind && t < 0.36) {{
            arcY -= Math.sin((t / 0.36) * Math.PI) * Math.min(64 * stop0.s, 72);
            isAirborne = t < 0.32;
          }} else if (stop1.behind && t > 0.68) {{
            arcY -= Math.sin(((t - 0.68) / 0.32) * Math.PI) * Math.min(56 * stop1.s, 60);
            isAirborne = true;
          }} else {{
            isAirborne = false;
          }}

          curFront = !(stop0.behind && t < 0.12 || stop1.behind && t > 0.92);

          const clamped = clampToSafe(
            curvePt.x,
            arcY,
            curScale,
            t < 0.5 ? lerpBox(stop0.box, PUP_BOX, t) : lerpBox(PUP_BOX, stop1.box, t),
            B.safe
          );

          curX = clamped.x;
          curY = clamped.y;

          // Motion tracking
          if (prevPos) {{
            const stepDist = Math.hypot(curX - prevPos.x, curY - prevPos.y);
            walkAccum += stepDist;
            controller.walkedTo(walkAccum / Math.max(0.05, curScale));

            if (Math.abs(curX - prevPos.x) > 0.6) {{
              controller.face(curX > prevPos.x ? 1 : -1, 0.16);
            }}

            // Paw print drop
            if (prints.length > 0 && stepDist > 4 && Math.random() < 0.35 && !isAirborne) {{
              const p = prints[printIdx++ % prints.length];
              const footX = curX + (controller.facingDir > 0 ? 140 : 60);
              const footY = curY + scrollY + 140;
              p.style.transform = `translate(${{footX.toFixed(0)}}px, ${{footY.toFixed(0)}}px) scale(${{curScale.toFixed(
                2
              )}})`;
              p.animate(
                [
                  {{ opacity: 0 }},
                  {{ opacity: 0.45, offset: 0.08 }},
                  {{ opacity: 0.45, offset: 0.5 }},
                  {{ opacity: 0 }},
                ],
                {{ duration: 2600, easing: 'ease-out' }}
              );
            }}
          }}

          if (isAirborne) {{
            controller.setPose('hop');
            controller.stride(0);
          }} else if (Math.abs(deltaY) > 0.4) {{
            controller.setPose('walk');
            controller.stride(1);
          }} else {{
            controller.setPose('stand');
            controller.stride(0);
          }}
        }}

        prevPos = {{ x: curX, y: curY }};

        // Idle speech bubble if paused scrolling
        const timeSinceMove = now - lastMoveTime;
        if (timeSinceMove > 2.6 && scrollY > 300 && timeSinceMove - dt <= 2.6) {{
          say('coming?');
        }}

        // Bubble hide
        if (now > bubbleUntil && bubble.dataset.show === 'true') {{
          bubble.dataset.show = 'false';
        }}

        // Position actor
        const actorX = curX - PUP_CENTER.x * curScale;
        const actorY = curY - PUP_CENTER.y * curScale;
        actor.style.transform = `translate3d(${{actorX.toFixed(2)}}px, ${{actorY.toFixed(2)}}px, 0)`;
        body.style.transform = `scale(${{curScale.toFixed(4)}})`;
        layer.dataset.front = String(curFront);

        // Update scene datasets (here and visited)
        B.meta.forEach((m, idx) => {{
          if (m.scene) {{
            m.scene.dataset.here = String(isAtHold && idx === k);
            m.scene.dataset.visited = String(idx <= k);
          }}
        }});

        // LookAt target
        if (lookTarget && lookTarget.until > now) {{
          controller.lookAt(lookTarget);
        }}
      }}

      controller.tick(dt, now);
      rafId = requestAnimationFrame(tick);
    }};

    rafId = requestAnimationFrame(tick);

    return () => {{
      cancelAnimationFrame(rafId);
      delete document.documentElement.dataset.pup;
      if (layer) layer.hidden = true;
      actor.removeEventListener('click', handleActorClick);
      window.removeEventListener('pointermove', handlePointerMove);
      window.removeEventListener('resize', computeStops);
    }};
  }}, []);

  return (
    <>
      {{/* Probe */}}
      <div ref={{probeRef}} aria-hidden="true" className="pup-probe" />

      {{/* Floating Paw Prints */}}
      <div ref={{printsRef}} aria-hidden="true" className="pup-prints">
        {{Array.from({{ length: 24 }}, (_, a) => (
          <svg key={{a}} viewBox="0 0 64 64">
            <path d="{paw_path}" />
          </svg>
        ))}}
      </div>

      {{/* Floating Pup Companion Layer */}}
      <div ref={{layerRef}} aria-hidden="true" className="pup-layer" hidden data-front="true">
        <div ref={{actorRef}} className="pup-actor">
          <div ref={{bodyRef}} className="pup-actor__body">
            {svg_jsx}
          </div>
          <span ref={{bubbleAtRef}} className="pup-bubble-at">
            <span ref={{bubbleRef}} className="pup-bubble" data-show="false" />
          </span>
        </div>
      </div>
    </>
  );
}}
'''

with open('src/components/PupJourney.jsx', 'w', encoding='utf-8') as f:
    f.write(script_content)

print('Generated exact PupJourney.jsx successfully! Length:', len(script_content))

