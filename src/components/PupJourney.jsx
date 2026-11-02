import React, { useEffect, useRef } from 'react';



// --- Constants & Color Tokens ---

const INK = '#2a170e';

const HONEY = '#f2be6b';

const HONEY_DARK = '#e4a352';

const CREAM = '#fbe3b4';

const COLLAR = '#a24a1a';

const BLUSH = '#f9b9a6';

const PUP_W = 300;

const PUP_H = 240;

const PUP_CENTER = { x: 150, y: 228 };

const PUP_BOX = [48, 30, 288, 236];



const POSE_BOXES = {

  sit: [50, 26, 284, 234],

  peek: [148, 34, 280, 163],

  snug: [148, 40, 280, 163],

  bow: [58, 56, 292, 236],

};

const getBox = (pose) => POSE_BOXES[pose] || PUP_BOX;



function genCurve(cx, cy, rx, ry, bumps, amp, startAngle = -Math.PI / 2, rotDeg = 0) {

  const rot = (rotDeg * Math.PI) / 180;

  const pt = (angle, offset) => {

    const x = Math.cos(angle) * (rx + offset);

    const y = Math.sin(angle) * (ry + (ry / rx) * offset);

    return `${(cx + x * Math.cos(rot) - y * Math.sin(rot)).toFixed(1)} ${(

      cy +

      x * Math.sin(rot) +

      y * Math.cos(rot)

    ).toFixed(1)}`;

  };

  let d = '';

  for (let i = 0; i < bumps; i++) {

    const a1 = startAngle + (i / bumps) * Math.PI * 2;

    const a2 = startAngle + ((i + 1) / bumps) * Math.PI * 2;

    const mid = (a1 + a2) / 2;

    d += `${i === 0 ? `M${pt(a1, 0)}` : ''}Q${pt(mid, 2.1 * amp)} ${pt(a2, 0)}`;

  }

  return `${d}Z`;

}



const P_BODY_ORIGIN = [196, 206];

const P_HEAD_ORIGIN = [212, 100];

const P_SHOULDER_N = [186, 194];

const P_SHOULDER_F = [168, 192];

const P_HIP_N = [110, 194];

const P_HIP_F = [94, 192];

const P_TAIL_BASE = [84, 150];

const P_EAR_L = [174, 82];

const P_EAR_R = [250, 82];



const PATHS = {

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

  shadow: { cx: 150, cy: 230, rx: 92, ry: 7 },

};



function genLeg(w, h) {

  const half = w / 2;

  return `M${-half} -14 C${-half} 4 -12 ${h - 18} -12 ${h - 9} C-12 ${h - 2} -7 ${

    h

  } 0 ${h} C9 ${h} 13 ${h - 3} 13 ${h - 9} C13 ${h - 18} ${half} 4 ${half} -14`;

}



const LEGS = {

  front: genLeg(24, 228 - P_SHOULDER_N[1]),

  frontFar: genLeg(22, 228 - P_SHOULDER_F[1]),

  back: genLeg(30, 228 - P_HIP_N[1]),

  backFar: genLeg(28, 228 - P_HIP_F[1]),

};



const BASE_POSE = {

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

};



const POSES = {

  stand: BASE_POSE,

  walk: { ...BASE_POSE, tail: -6, tongue: 1 },

  sit: { ...BASE_POSE, bodyRot: -24, bodyY: -2, headX: -10, headY: -6, tail: 34, sit: 1, tongue: 1 },

  peek: { ...BASE_POSE, headY: 4, earL: -6, earR: 6, tail: -20, front: 1, tongue: 1 },

  snug: { ...BASE_POSE, headY: 9, headRot: 4, earL: 3, earR: -3, tail: -20, front: 1, tongue: 0 },

  lie: {

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

  },

  sleep: {

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

  },

  settle: {

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

  },

  hop: {

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

  },

  sniff: { ...BASE_POSE, bodyRot: 7, headX: 16, headY: 32, headRot: 9, tail: -14, fn: 6, ff: 4 },

  bow: {

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

  },

  beg: {

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

  },

};



const POSE_KEYS = Object.keys(BASE_POSE);



function lerpPose(p1, p2, t) {

  const res = { ...p1 };

  for (const k of POSE_KEYS) {

    res[k] = p1[k] + (p2[k] - p1[k]) * t;

  }

  return res;

}



const round2 = (num) => Math.round(100 * num) / 100;

const rotStr = (deg, [x, y]) => `rotate(${round2(deg)} ${x} ${y})`;



function computeFrame(pose, state) {

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



  return {

    body: `translate(${round2(pose.bodyX)} ${round2(bodyY)}) ${rotStr(

      bodyRot,

      P_BODY_ORIGIN

    )} translate(${P_BODY_ORIGIN[0]} 0) scale(${round2(pose.stretch)} 1) translate(${

      -P_BODY_ORIGIN[0]

    } 0)`,

    fn: `translate(${P_SHOULDER_N[0]} ${P_SHOULDER_N[1]}) rotate(${round2(

      pose.fn + invBodyRot + phaseSin * legAmp * isMoving

    )})`,

    ff: `translate(${P_SHOULDER_F[0]} ${P_SHOULDER_F[1]}) rotate(${round2(

      pose.ff + invBodyRot + phaseSinOpp * legAmp * isMoving

    )})`,

    bn: `translate(${P_HIP_N[0]} ${P_HIP_N[1]}) rotate(${round2(

      pose.bn + phaseSinOpp * legAmp * isMoving

    )})`,

    bf: `translate(${P_HIP_F[0]} ${P_HIP_F[1]}) rotate(${round2(

      pose.bf + phaseSin * legAmp * isMoving

    )})`,

    tail: rotStr(tailRot, P_TAIL_BASE),

    haunch: `translate(0 ${round2(-0.06 * pose.bodyRot)})`,

    head: `translate(${round2(pose.headX)} ${round2(pose.headY + headBob)}) ${rotStr(

      pose.headRot + 1.4 * Math.sin(state.phase) * isMoving,

      P_HEAD_ORIGIN

    )}`,

    earL: rotStr(pose.earL + state.ear + 4 * Math.sin(2 * state.phase) * isMoving, P_EAR_L),

    earR: rotStr(pose.earR - state.ear - 4 * Math.sin(2 * state.phase) * isMoving, P_EAR_R),

    eyes: `translate(${round2(3.4 * state.gazeX)} ${round2(2.6 * state.gazeY)})`,

    blink: `translate(0 ${round2(98 * state.blink * 0.92)}) scale(1 ${round2(

      1 - 0.92 * state.blink

    )})`,

    openEyes: round2(Math.max(0, pose.eyes - pose.happy)),

    happyEyes: round2(Math.min(pose.happy, pose.eyes)),

    shutEyes: round2(1 - pose.eyes),

    tongue: round2(pose.tongue * (1 - pose.mouth)),

    mouth: round2(pose.mouth),

    backLegs: round2(1 - pose.sit),

    haunchOpacity: round2(pose.sit * (1 - pose.front)),

    side: round2(1 - pose.front),

    ledge: round2(pose.front),

    shadow: `translate(${round2(0.6 * pose.bodyX)} 0) scale(${round2(1 - 0.05 * bobbing * isMoving)} 1)`,

    shadowOpacity: round2(0.12 * (1 - pose.front)),

  };

}



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



class PupController {

  constructor(svg, initialPose = 'sit', facing = 1) {

    this.svg = svg;

    this.els = new Map();

    this.written = new Map();

    this.m = { phase: 0, stride: 0, time: 0, wag: 0.35, gazeX: 0, gazeY: 0, blink: 0, ear: 0 };

    this.strideTarget = 0;

    this.wagTarget = 0.35;

    this.gazeTarget = { x: 0, y: 0 };

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



    svg.querySelectorAll('[data-p]').forEach((el) => {

      this.els.set(el.dataset.p, el);

    });



    this.pose = { ...(POSES[initialPose] || POSES.sit) };

    this.target = this.pose;

    this.facing = facing;

    this.facingTarget = facing;

  }



  setPose(pose) {

    this.target = typeof pose === 'string' ? POSES[pose] || POSES.stand : pose;

  }



  jump(pose, facing) {

    this.pose = { ...(POSES[pose] || POSES.stand) };

    this.target = this.pose;

    if (facing) this.facing = this.facingTarget = facing;

  }



  face(dir, turn = 0.07) {

    this.facingTarget = dir;

    this.turn = turn;

  }



  get facingDir() {

    return this.facingTarget;

  }



  stride(val) {

    this.strideTarget = clampVal(val, 0, 1);

  }



  advance(dist) {

    this.m.phase += (dist / 46) * Math.PI;

  }



  walkedTo(dist) {

    this.m.phase = (dist / 46) * Math.PI;

  }



  wag(val) {

    this.wagTarget = clampVal(val, 0, 1);

  }



  cock(deg) {

    this.tiltTarget = deg;

  }



  lookAt(target) {

    if (!target) {

      this.gazeTarget = { x: 0, y: 0 };

      return;

    }

    const rect = this.svg.getBoundingClientRect();

    const eyeX = this.facingTarget > 0 ? P_HEAD_ORIGIN[0] : PUP_W - P_HEAD_ORIGIN[0];

    const originX = rect.left + (eyeX / PUP_W) * rect.width;

    const originY = rect.top + (98 / PUP_H) * rect.height;

    const dx = target.x - originX;

    const dy = target.y - originY;

    const dist = Math.hypot(dx, dy) || 1;

    const factor = Math.min(1, dist / 160);

    this.gazeTarget = {

      x: (dx / dist) * factor * this.facingTarget,

      y: (dy / dist) * factor,

    };

  }



  woof(time) {

    this.woofUntil = time + 0.34;

    this.bounceV = -150;

    this.earV += 260;

  }



  jolt(mult = 1) {

    this.earV += 220 * mult;

  }



  hop(mult = 1) {

    this.bounceV = -230 * mult;

    this.earV += 200 * mult;

  }



  yawn(time, dur = 0.9) {

    this.woofUntil = time + dur;

  }



  dash(val) {

    this.offsetTarget = val;

  }



  petting(bool) {

    this.petTarget = bool ? 1 : 0;

  }



  reset() {

    this.offsetTarget = 0;

    this.tiltTarget = 0;

    this.petTarget = 0;

  }



  tick(dt, time) {

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



    if (time > this.nextBlink && this.pose.eyes > 0.6) {

      this.blinkAt = time;

      this.nextBlink = time + 2.2 + 3.8 * Math.random();

      if (Math.random() < 0.18) this.nextBlink = time + 0.32;

    }



    const blinkPhase = (time - this.blinkAt) / 0.15;

    s.blink = blinkPhase >= 0 && blinkPhase <= 1 ? Math.sin(blinkPhase * Math.PI) : 0;



    const framePose = {

      ...this.pose,

      headRot: this.pose.headRot + this.tilt,

      bodyRot: this.pose.bodyRot + this.lean,

      bodyY: this.pose.bodyY + this.bounce,

      headY: this.pose.headY + 1.15 * this.bounce,

      mouth: time < this.woofUntil ? 1 : this.pose.mouth,

      happy: Math.max(this.pose.happy, this.pet),

    };



    const frame = computeFrame(framePose, speed > s.stride ? { ...s, stride: speed } : s);

    const facingSign = Math.abs(this.facing) < 0.02 ? 0.02 * Math.sign(this.facing || 1) : this.facing;

    const rootTransform = `translate(${this.offset.toFixed(1)} 0) translate(${150} 0) scale(${facingSign.toFixed(

      3

    )} 1) translate(${-150} 0)`;



    for (const [part, attr, prop] of TRANSFORM_MAP) {

      const el = this.els.get(part);

      if (!el) continue;

      const val = prop === 'root' ? rootTransform : String(frame[prop]);

      const key = `${part}:${attr}`;

      if (this.written.get(key) !== val) {

        el.setAttribute(attr, val);

        this.written.set(key, val);

      }

    }

  }

}



// --- Interaction Actions ---

const flipDir = (d) => (d === 1 ? -1 : 1);

const ACTIONS_LIST = ['woof', 'spin', 'beg', 'bow', 'hop', 'love', 'tilt', 'sneeze'];



const ACTIONS = {

  woof: ({ d, say }, a) => [

    [a, (t) => (d.woof(t), say('woof!'))],

    [a + 0.42, (t) => (d.woof(t), say('woof woof!'))],

  ],

  spin: ({ d, rest, facing, say }, i) => [

    [i, () => (d.setPose('stand'), d.hop(0.5))],

    [i + 0.14, () => d.face(flipDir(facing))],

    [i + 0.38, () => d.face(facing)],

    [i + 0.62, () => d.face(flipDir(facing))],

    [i + 0.86, () => (d.face(facing), say('wheee!'))],

    [i + 1.3, () => d.setPose(rest)],

  ],

  beg: ({ d, rest, say }, s) => [

    [s, () => (d.setPose('beg'), d.wag(1), say('treat, please?', 1.7))],

    [s + 1.9, () => (d.setPose(rest), d.wag(0.7))],

  ],

  bow: ({ d, rest, say }, s) => [

    [s, () => (d.setPose('bow'), d.wag(1), say('play?', 1.5))],

    [s + 1.8, () => (d.setPose(rest), d.wag(0.7))],

  ],

  hop: ({ d, rest }, s) => [

    [s, () => (d.setPose('hop'), d.hop(1.35))],

    [s + 0.36, () => d.setPose(rest)],

    [s + 0.62, () => (d.setPose('hop'), d.hop(0.8))],

    [s + 0.98, () => d.setPose(rest)],

  ],

  love: ({ d, rest, say, hearts }, i) => [

    [i, () => (d.setPose({ ...rest, happy: 1, tongue: 1 }), d.wag(1), hearts(), say('I like you!', 1.5))],

    [i + 1.9, () => (d.setPose(rest), d.wag(0.7))],

  ],

  tilt: ({ d, say }, a) => [

    [a, () => (d.cock(-14), say('hm?'))],

    [a + 0.8, () => d.cock(12)],

    [a + 1.6, () => d.cock(0)],

  ],

  sneeze: ({ d, say }, a) => [

    [a, () => d.cock(-8)],

    [a + 0.32, (t) => (d.cock(10), d.jolt(1.4), d.hop(0.35), d.yawn(t, 0.22), say('achoo!'))],

    [a + 0.8, () => d.cock(0)],

  ],

  zoomies: ({ d, rest, facing, say }, i) => [

    [i, () => (d.setPose('walk'), d.wag(1), say('zoomies!', 2))],

    [i + 0.05, () => (d.face(1), d.dash(70))],

    [i + 0.5, () => (d.face(-1), d.dash(-70))],

    [i + 0.98, () => (d.face(1), d.dash(50))],

    [i + 1.4, () => (d.face(-1), d.dash(-30))],

    [i + 1.78, () => (d.face(1), d.dash(0))],

    [i + 2.25, () => (d.face(facing), d.setPose(rest), d.wag(0.7))],

  ],

  peekaboo: ({ d, say }, s) => [

    [s, () => d.setPose({ ...POSES.peek, headY: 120 })],

    [s + 0.55, () => (d.setPose('peek'), d.jolt(1.2), say('peekaboo!'))],

  ],

  wake: ({ d, rest, say }, i) => [

    [i, (t) => (d.setPose('settle'), d.yawn(t, 0.9), say('*yaaawn*'))],

    [i + 1.25, () => (d.setPose({ ...POSES.settle, happy: 1 }), d.wag(0.8), say('five more minutes…', 1.6))],

    [i + 3.1, () => (d.setPose(rest), d.wag(0), say('zzz', 2))],

  ],

};



function spawnHearts(container, x, y) {

  for (let s = 0; s < 5; s++) {

    const heart = document.createElement('span');

    heart.className = 'pup-heart';

    heart.textContent = '♥';

    heart.style.left = `${x}px`;

    heart.style.top = `${y}px`;

    container.appendChild(heart);

    const offsetX = (Math.random() - 0.5) * 90;

    const offsetY = -70 - 60 * Math.random();

    heart

      .animate(

        [

          { transform: 'translate(-50%, 0) scale(0.4)', opacity: 0 },

          { opacity: 1, offset: 0.2 },

          {

            transform: `translate(calc(-50% + ${offsetX.toFixed(0)}px), ${offsetY.toFixed(0)}px) scale(1.1)`,

            opacity: 0,

          },

        ],

        {

          duration: 1150 + 110 * s,

          delay: 80 * s,

          easing: 'cubic-bezier(.2,.7,.3,1)',

          fill: 'backwards',

        }

      )

      .finished.then(

        () => heart.remove(),

        () => heart.remove()

      );

  }

}



let actionPool = [];

function chooseAction(last, combo) {

  if (combo >= 4) return 'zoomies';

  if (!actionPool.length) {

    actionPool = ACTIONS_LIST.filter((a) => a !== last).sort(() => Math.random() - 0.5);

  }

  return actionPool.pop() || 'woof';

}



// --- Curve & Journey Math Helpers ---

const clamp01 = (v) => Math.min(1, Math.max(0, v));

const smooth3 = (v) => v * v * (3 - 2 * v);

const smoothstepClamped = (e0, e1, x) => (e1 === e0 ? +(x >= e1) : smooth3(clamp01((x - e0) / (e1 - e0))));

const lerpNum = (a, b, t) => a + (b - a) * t;



const softMin = (e, t, a) => {

  const s = (e - t) / a;

  return s > 20 ? e : t + a * Math.log1p(Math.exp(s));

};

const softMax = (e, t, a) => -softMin(-e, -t, a);



function clampToSafe(x, y, scale, box, safe, margin = 8) {

  const leftOff = (PUP_CENTER.x - box[0]) * scale;

  const rightOff = (box[2] - PUP_CENTER.x) * scale;

  const topOff = (PUP_CENTER.y - box[1]) * scale;

  const botOff = (box[3] - PUP_CENTER.y) * scale;

  let finalX;

  if (safe.right - safe.left > leftOff + rightOff) {

    finalX = softMax(softMin(x, safe.left + leftOff, margin), safe.right - rightOff, margin);

  } else {

    finalX = (safe.left + safe.right) / 2 - (rightOff - leftOff) / 2;

  }

  let finalY;

  if (safe.bottom - safe.top > topOff + botOff) {

    finalY = softMax(softMin(y, safe.top + topOff, margin), safe.bottom - botOff, margin);

  } else {

    finalY = safe.bottom - botOff;

  }

  return { x: finalX, y: finalY };

}



const lerpBox = (b1, b2, t) => [

  lerpNum(b1[0], b2[0], t),

  lerpNum(b1[1], b2[1], t),

  lerpNum(b1[2], b2[2], t),

  lerpNum(b1[3], b2[3], t),

];



const evalBezier = (p0, c1, c2, p1, t) => {

  const mt = 1 - t;

  const mt2 = mt * mt;

  const mt3 = mt2 * mt;

  const t2 = t * t;

  const t3 = t2 * t;

  return {

    x: mt3 * p0.x + 3 * mt2 * t * c1.x + 3 * mt * t2 * c2.x + t3 * p1.x,

    y: mt3 * p0.y + 3 * mt2 * t * c1.y + 3 * mt * t2 * c2.y + t3 * p1.y,

  };

};



function getStopPosition(stop, scrollY) {

  const tr = stop.track;

  let trackY;

  if (tr.kind === 'page') trackY = tr.top - scrollY;

  else if (tr.kind === 'screen') trackY = tr.top;

  else if (scrollY < tr.from) trackY = tr.top - (scrollY - tr.from);

  else if (scrollY > tr.to) trackY = tr.top - (scrollY - tr.to);

  else trackY = tr.top;

  return {

    x: stop.x + PUP_CENTER.x * stop.s,

    y: trackY + PUP_CENTER.y * stop.s,

  };

}



function findHoldIndex(holds, scrollY) {

  if (!holds.length || scrollY <= holds[0][1]) return { k: 0, t: 0 };

  for (let i = 0; i < holds.length - 1; i++) {

    const s = holds[i][1];

    const nextStart = holds[i + 1][0];

    if (scrollY < nextStart) return { k: i, t: clamp01((scrollY - s) / Math.max(1, nextStart - s)) };

    if (scrollY <= holds[i + 1][1]) return { k: i + 1, t: 0 };

  }

  return { k: holds.length - 1, t: 0 };

}



function adjustHolds(rawHolds, travelDists, scrollMax) {

  const getDist = (i) => (typeof travelDists === 'number' ? travelDists : travelDists[i] ?? 0);

  const holds = rawHolds.map((h) => (h[0] <= h[1] ? [h[0], h[1]] : [(h[0] + h[1]) / 2, (h[0] + h[1]) / 2]));

  if (!holds.length) return holds;

  holds[0][0] = -Infinity;

  const lastHold = holds[holds.length - 1];

  lastHold[1] = Infinity;

  lastHold[0] = Math.min(lastHold[0], scrollMax - 1);



  for (let i = 0; i < holds.length - 1; i++) {

    const cur = holds[i];

    const next = holds[i + 1];

    if (next[0] < cur[1]) {

      const mid = (cur[1] + next[0]) / 2;

      cur[1] = Math.max(cur[0], mid);

      next[0] = Math.min(next[1], mid);

      if (next[0] < cur[1]) next[0] = cur[1];

    }

    let deficit = getDist(i) - (next[0] - cur[1]);

    if (deficit > 0) {

      const trimCur = Math.min(deficit / 2, cur[1] - cur[0]);

      const trimNext = Math.min(deficit / 2, next[1] - next[0]);

      cur[1] -= trimCur;

      next[0] += trimNext;

      deficit -= trimCur + trimNext;

      const extraNext = Math.min(deficit, next[1] - next[0]);

      next[0] += extraNext;

      deficit -= extraNext;

      if (deficit > 0) {

        cur[1] -= Math.min(deficit, cur[1] - cur[0]);

      }

    }

  }

  for (const h of holds) {

    if (h[1] < h[0]) h[1] = h[0];

  }

  return holds;

}



const SET_DATA = (el, key, val) => {

  if (el.dataset[key] !== val) el.dataset[key] = val;

};



export default function PupJourney() {

  const layerRef = useRef(null);

  const actorRef = useRef(null);

  const bodyRef = useRef(null);

  const bubbleRef = useRef(null);

  const bubbleAtRef = useRef(null);

  const printsRef = useRef(null);

  const probeRef = useRef(null);



  useEffect(() => {

    const prefersReducedMotion =

      window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    if (prefersReducedMotion) {
      return;
    }



    const layer = layerRef.current;

    const actor = actorRef.current;

    const body = bodyRef.current;

    const bubble = bubbleRef.current;

    const bubbleAt = bubbleAtRef.current;

    const printsContainer = printsRef.current;

    const probe = probeRef.current;



    if (!layer || !actor || !body || !printsContainer || !probe) return;



    const svg = body.querySelector('svg');

    if (!svg) return;



    const printEls = Array.from(printsContainer.children);

    let printIdx = 0;



    let B = null;

    let F = null;

    let isLive = false;

    let rafId;



    let bubbleUntil = 0;

    const say = (text, time, dur = 1.4) => {

      if (!bubble) return;

      bubble.textContent = text;

      bubble.dataset.show = 'true';

      bubbleUntil = time + dur;

    };



    let pointerTarget = null;

    let lookTarget = null;



    const onPointerMove = (e) => {

      if (e.pointerType === 'mouse') {

        pointerTarget = { x: e.clientX, y: e.clientY, t: performance.now() / 1000 };

      }

    };



    const onPupCue = (e) => {

      const d = e.detail;

      const curScene = holdingStopIdx >= 0 ? B?.meta[holdingStopIdx]?.scene : null;

      if (!curScene || (d.look && !curScene.contains(d.look))) return;

      const now = performance.now() / 1000;

      if (d.look) {

        lookTarget = { el: d.look, until: now + (d.secs ?? 1.6) };

      }

      if (d.say) say(d.say, now);

    };



    const onFocusIn = (e) => {

      const t = e.target;

      if (t instanceof HTMLElement && t.matches('a, button, input, textarea, select, summary')) {

        lookTarget = { el: t, until: performance.now() / 1000 + 1.4 };

      }

    };



    let K = performance.now() / 1000;

    let prevScrollY = window.scrollY;

    let prevLoc = null;

    let curState = null;

    const inertia = { x: 0, y: 0, s: 0 };

    let stationaryTime = 0;

    let holdingStopIdx = -1;

    let stopArrivalTime = 0;

    let lastMoveTime = performance.now() / 1000;

    let actionQueue = [];

    let lastLookIdx = -1;

    let prevTreadmillLeft = null;

    let treadmillIdle = 0;

    let lastPawPrintStop = -1;

    let lastPawPrintIdx = 0;

    let basketWakeTime = 0;

    let lastScrollActionTime = performance.now() / 1000;

    let scrollDir = 1;

    let wasPaused = false;

    let walkAccum = 0;



    let efPos = null;
    let prevWhatsAppTop = 0;
    let layerOffsetY = 0;
    let mobileWalkDist = 0;

    const getScreenBottom = () => {
      const wa = document.querySelector('[data-whatsapp-bar]');
      const rect = wa && wa.getClientRects().length ? wa.getBoundingClientRect() : null;
      return rect && rect.height ? rect.top : window.innerHeight - 6;
    };

    const buildLayout = () => {
      const isMobile = window.matchMedia('(max-width: 767px), (pointer: coarse) and (max-height: 519px)').matches;
      const clientW = document.documentElement.clientWidth;
      const s = probe.getBoundingClientRect().height || window.innerHeight;
      const siteHeader = document.getElementById('site-header');
      const headerH = siteHeader?.offsetHeight ?? 76;
      const whatsappBar = document.querySelector('[data-whatsapp-bar]');
      const whatsappH = whatsappBar?.getClientRects().length ? whatsappBar.getBoundingClientRect().height : 0;
      const safe = {
        left: 10,
        top: headerH + 10,
        right: clientW - 10,
        bottom: s - 10 - whatsappH,
      };
      const mainEl = document.getElementById('main');
      const stops = [];
      const meta = [];
      const rawHolds = [];

      const addStop = (el) => {
        const rect = el.getBoundingClientRect();
        const pose = el.dataset.pose || 'sit';
        const act = el.dataset.act ?? '';
        const scaleBase = rect.width / 300;
        const scale = act === 'basket' || isMobile ? scaleBase : 1.12 * scaleBase;
        const centerOff = pose === 'peek' ? { x: PUP_CENTER.x, y: 159 } : PUP_CENTER;

        // Sticky track detection
        let stickyParent = null;
        for (let p = el.parentElement; p && p !== document.body; p = p.parentElement) {
          if (getComputedStyle(p).position === 'sticky') {
            stickyParent = p;
            break;
          }
        }

        let track;
        if (!stickyParent) {
          track = { kind: 'page', top: rect.top + window.scrollY };
        } else {
          const stickyTop = parseFloat(getComputedStyle(stickyParent).top) || 0;
          const offsetInside = rect.top - stickyParent.getBoundingClientRect().top;
          const prevPos = stickyParent.style.position;
          stickyParent.style.position = 'relative';
          const stickyRect = stickyParent.getBoundingClientRect();
          const stickyParentParent = stickyParent.parentElement;
          const parentBot =
            stickyParentParent.getBoundingClientRect().bottom -
            (parseFloat(getComputedStyle(stickyParentParent).paddingBottom) || 0);
          stickyParent.style.position = prevPos;
          const pinFrom = stickyRect.top + window.scrollY - stickyTop;
          const pinTo = parentBot + window.scrollY - stickyRect.height - stickyTop;
          if (pinTo <= pinFrom) {
            track = { kind: 'page', top: stickyRect.top + window.scrollY + offsetInside };
          } else {
            track = { kind: 'pin', top: stickyTop + offsetInside, from: pinFrom, to: pinTo };
          }
        }

        if (track.kind !== 'screen') {
          track.top += centerOff.y * (scaleBase - scale);
        }

        const stopObj = {
          x: rect.left + centerOff.x * (scaleBase - scale),
          track,
          s: scale,
          behind: el.dataset.behind === 'true',
          sink: 0,
          box: getBox(pose),
        };

        const scene = el.closest('[data-pup-scene]');
        stops.push(stopObj);
        meta.push({
          scene,
          pose,
          facing: el.dataset.facing === 'left' ? -1 : 1,
          act,
          looks: scene ? Array.from(scene.querySelectorAll('[data-pup-look]')) : [],
          track: act === 'treadmill' ? scene?.querySelector('[data-treadmill]') ?? null : null,
        });

        // Compute hold bounds
        const holdRatios = isMobile ? [0.6, 0.86] : [0.42, 0.78];
        let holdRange;
        if (track.kind === 'pin') {
          holdRange = [track.from, track.to];
        } else {
          const sTop = track.top;
          const n = sTop + stopObj.box[1] * stopObj.s;
          const l = sTop + stopObj.box[3] * stopObj.s;
          const r = (n + l) / 2;
          const vpH = safe.bottom - safe.top;
          let o = r - (safe.top + holdRatios[1] * vpH);
          let d = r - (safe.top + holdRatios[0] * vpH);
          o = Math.max(o, l - safe.bottom);
          d = Math.min(d, n - safe.top);
          if (o > d) o = d = r - (safe.top + vpH / 2);
          holdRange = [o, d];
        }

        if (!isMobile && scene && track.kind === 'page' && act !== 'basket' && act !== 'peekaboo') {
          const vpH = safe.bottom - safe.top;
          const sceneTop = scene.getBoundingClientRect().top + window.scrollY - safe.top + 0.08 * vpH;
          const a = track.top + stopObj.box[3] * stopObj.s - safe.bottom;
          if (holdRange[1] > sceneTop) {
            const sVal = Math.max(sceneTop, a + 0.12 * vpH);
            holdRange = [Math.max(a, sVal - Math.max(holdRange[1] - holdRange[0], 0.2 * vpH)), sVal];
          }
        }
        rawHolds.push(holdRange);
      };

      const stopEls = Array.from(document.querySelectorAll('[data-pup-stop]')).filter(
        (el) => el.getClientRects().length > 0
      );

      if (isMobile) {
        const laneStops = stopEls.filter((el) => el.dataset.lane === 'true');
        const firstStop = laneStops[0];
        const lastStop = laneStops.length > 1 ? laneStops[laneStops.length - 1] : undefined;
        if (firstStop) addStop(firstStop);

        const firstScene = meta[0]?.scene ?? null;
        const scenes = Array.from(document.querySelectorAll('#main [data-pup-scene]')).filter(
          (el) => el !== firstScene && el.getClientRects().length > 0
        );

        const dScale = Math.min(0.62, Math.max(0.5, clientW / 650));
        const peekBox = getBox('peek');
        const sinkVal = PUP_CENTER.y - 159;

        scenes.forEach((sceneEl, idx) => {
          const isEven = idx % 2 === 0;
          const stopX = isEven
            ? safe.left + 2 - peekBox[0] * dScale
            : safe.right - 2 - peekBox[2] * dScale;

          stops.push({
            x: stopX,
            track: { kind: 'screen', top: 0 },
            s: dScale,
            behind: false,
            sink: sinkVal,
            box: peekBox,
          });

          meta.push({
            scene: sceneEl,
            pose: 'peek',
            facing: isEven ? 1 : -1,
            act: 'lane',
            looks: [],
            track: null,
          });

          const sRect = sceneEl.getBoundingClientRect();
          const fromHold = sRect.top + window.scrollY - 0.42 * s;
          const toHold = sRect.bottom + window.scrollY - 0.58 * s;
          rawHolds.push(fromHold <= toHold ? [fromHold, toHold] : [(fromHold + toHold) / 2, (fromHold + toHold) / 2]);
        });

        if (lastStop) addStop(lastStop);
      } else {
        stopEls.forEach(addStop);
      }

      const maxScroll = document.documentElement.scrollHeight - window.innerHeight;
      const travelDists = stops.slice(1).map((cur, i) => {
        const prev = stops[i];
        const lH = (0.78 - 0.42) * s;
        const rMin = (isMobile ? 0.32 : 0.5) * s;
        return Math.min(
          1.4 * s,
          Math.max(rMin, 1.15 * Math.hypot(Math.abs(cur.x + PUP_CENTER.x * cur.s - (prev.x + PUP_CENTER.x * prev.s)), lH))
        );
      });

      return {
        lane: isMobile,
        stops,
        meta,
        holds: adjustHolds(rawHolds, travelDists, maxScroll),
        blend: 0.12 * s,
        mainTop: mainEl ? mainEl.getBoundingClientRect().top + window.scrollY : 0,
        safe,
      };
    };

    const evalJourney = (layout, scrollY) => {
      const { stops, holds, blend } = layout;

      if (layout.lane) {
        const screenBottom = getScreenBottom();
        for (const stop of stops) {
          if (stop.track.kind === 'screen') {
            stop.track.top = screenBottom - 159 * stop.s;
          }
        }
      }

      const clientW = document.documentElement.clientWidth;
      const siteHeader = document.getElementById('site-header');
      const headerTop = (siteHeader?.offsetHeight ?? 76) + 10;
      let evalSafe;
      if (layout.lane) {
        evalSafe = { left: 10, top: headerTop, right: clientW - 10, bottom: getScreenBottom() + 40 };
      } else {
        const wa = document.querySelector('[data-whatsapp-bar]');
        const waTop = wa?.getClientRects().length ? wa.getBoundingClientRect().top : window.innerHeight;
        evalSafe = { left: 10, top: headerTop, right: clientW - 10, bottom: Math.min(window.innerHeight, waTop) - 10 };
      }

      const { k: P, t: B } = findHoldIndex(holds, scrollY);
      if (B <= 0 || P >= stops.length - 1) {
        const n = stops[P];
        const p = getStopPosition(n, scrollY);
        const r = clampToSafe(p.x, p.y, n.s, n.box, evalSafe);
        return {
          x: r.x,
          y: r.y,
          s: n.s,
          front: !n.behind,
          airborne: false,
          k: P,
          t: 0,
          walked: 0,
        };
      }

      const r = stops[P];
      const i = stops[P + 1];
      const o = holds[P][1];
      const d = holds[P + 1][0];
      const g = Math.max(1, d - o);
      const v = clamp01((scrollY - o) / g);
      const k = getStopPosition(r, o);
      const _ = getStopPosition(i, d);

      const p0 = { x: k.x, y: k.y - (r.sink || 0) * r.s };
      const p1 = { x: _.x, y: _.y - (i.sink || 0) * i.s };

      // Bezier control points
      const dx = p1.x - p0.x;
      const nW = evalSafe.right - evalSafe.left;
      const lW = Math.max(0.45 * Math.abs(dx), 0);
      const dirX = dx >= 0 ? 1 : -1;
      let c1 = { x: p0.x + dirX * lW, y: p0.y };
      let c2 = { x: p1.x - dirX * lW, y: p1.y };
      const dMin = 0.14 * nW;
      if (Math.abs(dx) < dMin) {
        const sign = (p0.x + p1.x) / 2 < (evalSafe.left + evalSafe.right) / 2 ? 1 : -1;
        const off = sign * (dMin - Math.abs(dx)) * 0.9;
        c1 = { x: c1.x + off, y: lerpNum(p0.y, p1.y, 0.2) };
        c2 = { x: c2.x + off, y: lerpNum(p0.y, p1.y, 0.8) };
      }
      const clampPt = (pt) => ({
        x: Math.min(evalSafe.right, Math.max(evalSafe.left, pt.x)),
        y: Math.min(evalSafe.bottom, Math.max(evalSafe.top, pt.y)),
      });
      const bez = { p0, c1: clampPt(c1), c2: clampPt(c2), p1 };

      // Quintic smoothstep
      const w = v * v * v * (v * (6 * v - 15) + 10);
      const M = evalBezier(bez.p0, bez.c1, bez.c2, bez.p1, w);
      const E = lerpNum(r.s, i.s, smooth3(clamp01(v / 0.65)));

      const R = Math.min(0.3, Math.max(0.06, blend / g));
      const S = 1 - smoothstepClamped(0, R, v);
      const T_blend = smoothstepClamped(1 - R, 1, v);
      let L = M.y + S * (getStopPosition(r, scrollY).y - k.y) + T_blend * (getStopPosition(i, scrollY).y - _.y);
      const C = M.x;

      L += (r.sink || 0) * r.s * (1 - smoothstepClamped(0, 0.22, v)) + (i.sink || 0) * i.s * smoothstepClamped(0.78, 1, v);

      let A = false;
      if (r.behind && v < 0.36) {
        L -= Math.sin((v / 0.36) * Math.PI) * Math.min(64 * r.s, 72);
        A = v < 0.32;
      }
      if (i.behind && v > 0.68) {
        L -= Math.sin(((v - 0.68) / 0.32) * Math.PI) * Math.min(56 * i.s, 60);
        A = true;
      }
      if (r.sink && v < 0.2) {
        A = true;
      }

      const isFront = !(r.behind && v < 0.12 || i.behind && v > 0.92);

      const rBoxTrans = smoothstepClamped(0, r.sink ? 0.22 : r.behind ? 0.36 : 0.06, v);
      const iBoxTrans = smoothstepClamped(i.sink ? 0.78 : i.behind ? 0.68 : 0.94, 1, v);
      const clamped = clampToSafe(
        C,
        L,
        E,
        v < 0.5
          ? lerpBox(r.box, PUP_BOX, rBoxTrans)
          : lerpBox(PUP_BOX, i.box, iBoxTrans),
        evalSafe
      );

      // Walked distance along bezier arc
      let walked = 0;
      let sPt = bez.p0;
      const nSteps = Math.max(1, Math.ceil(32 * clamp01(w)));
      for (let step = 1; step <= nSteps; step++) {
        const curPt = evalBezier(bez.p0, bez.c1, bez.c2, bez.p1, (step / nSteps) * clamp01(w));
        walked += Math.hypot(curPt.x - sPt.x, curPt.y - sPt.y);
        sPt = curPt;
      }

      return {
        x: clamped.x,
        y: clamped.y,
        s: E,
        front: isFront,
        airborne: A,
        k: P,
        t: v,
        walked,
      };
    };

        const actionContext = (metaObj) => ({

      d: F,

      rest: POSES[metaObj.pose] || POSES.sit,

      facing: metaObj.facing,

      say: (txt, dur = 1.4) => say(txt, performance.now() / 1000, dur),

      hearts: () => {

        if (!curState) return;

        const heartX = curState.x - PUP_CENTER.x * curState.s + (F.facingDir > 0 ? 212 : PUP_W - 212) * curState.s;

        const heartY = curState.y - (PUP_CENTER.y - 40) * curState.s;

        spawnHearts(actor, heartX, heartY);

      },

    });



    let comboClicks = 0;

    let lastClickTime = 0;

    let lastActionName = null;



    const handleActorClick = () => {

      if (!F || !B) return;

      const now = performance.now() / 1000;

      comboClicks = now - lastClickTime < 0.7 ? comboClicks + 1 : 1;

      lastClickTime = now;

      lastMoveTime = now;



      if (holdingStopIdx < 0) {

        // While walking between stops

        const m = B.meta[Math.max(0, curState?.k ?? 0)];

        const actName = ['jump', 'woof', 'love', 'sneeze'][Math.floor(Math.random() * 4)];

        lastActionName = actName;

        const ctx = actionContext(m);

        if (actName === 'jump') {

          actionQueue = [

            [now, () => (F.hop(1.35), ctx.say(['wheee!', 'boing!', 'yip!'][Math.floor(Math.random() * 3)]))],

            [now + 0.5, () => F.hop(0.7)],

          ];

        } else if (actName === 'woof') {

          actionQueue = [

            [now, (t) => (F.woof(t), ctx.say('woof!'))],

            [now + 0.4, (t) => F.woof(t)],

          ];

        } else if (actName === 'love') {

          actionQueue = [

            [

              now,

              () => {

                F.wag(1);

                F.hop(0.5);

                ctx.hearts();

                ctx.say('I like you!');

              },

            ],

          ];

        } else {

          actionQueue = [

            [

              now,

              (t) => {

                F.jolt(1.4);

                F.hop(0.4);

                F.yawn(t, 0.22);

                ctx.say('achoo!');

              },

            ],

          ];

        }

        return;

      }



      // At stop

      const m = B.meta[holdingStopIdx];

      let chosen = chooseAction(lastActionName, comboClicks);

      lastActionName = chosen;

      F.reset();

      const fn = ACTIONS[chosen];

      if (fn) {

        actionQueue = fn(actionContext(m), now);

      }

    };



    const handlePointerEnter = (e) => {

      if (e.pointerType === 'mouse' && F && holdingStopIdx >= 0) {

        F.petting(true);

        F.wag(1);

      }

    };



    const handlePointerLeave = () => {

      if (F) {

        F.petting(false);

        if (holdingStopIdx >= 0) {

          F.wag(B?.meta[holdingStopIdx]?.act === 'basket' ? 0.3 : 0.7);

        }

      }

    };



    const initJourney = () => {

      if (isLive) return;

      const layout = buildLayout();

      if (layout.stops.length < 2) return;

      B = layout;

      isLive = true;

      document.documentElement.dataset.pup = layout.lane ? 'lane' : 'live';

      layer.hidden = false;



      const firstMeta = layout.meta[0];

      F = new PupController(svg, firstMeta.pose, firstMeta.facing);

      prevScrollY = window.scrollY;

      prevLoc = null;

      lastScrollActionTime = K = performance.now() / 1000;

      wasPaused = false;



      const startState = evalJourney(layout, window.scrollY);

      if (startState.k === 0 && startState.t === 0 && firstMeta.act === 'peekaboo') {

        holdingStopIdx = 0;

        stopArrivalTime = K;

        const initialPeek = { ...POSES.peek, headY: 120 };

        const friends = firstMeta.scene?.querySelectorAll('[data-pup-friend]') ?? [];

        const f0 = friends[0];

        const f1 = friends[friends.length - 1];

        actionQueue = [

          [K + 0.1, () => F.setPose(initialPeek)],

          [K + 0.7, (t) => (F.setPose('peek'), F.jolt(1.2), say('peekaboo!', t, 1.6))],

          [K + 1.5, (t) => f0 && (lookTarget = { el: f0, until: t + 0.8 })],

          [K + 2.3, (t) => f1 && (lookTarget = { el: f1, until: t + 0.8 })],

          [K + 3.1, () => ((lookTarget = null), F.wag(1))],

        ];

      } else {

        holdingStopIdx = -1;

      }



      window.addEventListener('pointermove', onPointerMove, { passive: true });

      window.addEventListener('pup:cue', onPupCue);

      window.addEventListener('focusin', onFocusIn);

      actor.addEventListener('click', handleActorClick);

      actor.addEventListener('pointerenter', handlePointerEnter);

      actor.addEventListener('pointerleave', handlePointerLeave);

    };



    const tick = () => {

      if (!B || !F) {

        rafId = requestAnimationFrame(tick);

        return;

      }



      const now = performance.now() / 1000;

      const dt = Math.min(0.05, now - K);

      K = now;



      const curScroll = window.scrollY;

      const scrollDelta = curScroll - prevScrollY;

      prevScrollY = curScroll;



      if (Math.abs(scrollDelta) > 0.5) {

        lastScrollActionTime = now;

        scrollDir = scrollDelta > 0 ? 1 : -1;

      }



      // Process queued actions

      while (actionQueue.length && actionQueue[0][0] <= now) {

        actionQueue.shift()[1](now);

      }



      // Snap scroll position if paused mid-transition
      let activeScroll = curScroll;
      if (now - lastScrollActionTime > 0.25) {
        const { k: s, t: n } = findHoldIndex(B.holds, curScroll);
        if (n > 0 && s < B.stops.length - 1) {
          const r0 = B.stops[s];
          const r1 = B.stops[s + 1];
          const iBound = r0.sink ? 0.22 : (r0.behind ? 0.36 : 0);
          const oBound = r1.sink ? 0.78 : (r1.behind ? 0.68 : 1);
          let snapN = n;
          if (n < iBound) {
            snapN = n < iBound / 2 ? 0 : iBound;
          } else if (n > oBound) {
            snapN = n > (1 + oBound) / 2 ? 1 : oBound;
          }
          if (snapN !== n) {
            activeScroll = B.holds[s][1] + snapN * (B.holds[s + 1][0] - B.holds[s][1]);
          }
        }
      }



      const v = evalJourney(B, activeScroll);



      // Check screen to screen transition in mobile lane mode
      const isScreenToScreen = B.lane && (() => {
        const curStop = B.stops[v.k];
        const nextStop = v.t > 0 ? B.stops[v.k + 1] : curStop;
        return curStop.track.kind === 'screen' && nextStop?.track.kind === 'screen';
      })();

      // Inertia decay
      const damp = Math.exp(-dt / 0.28);
      inertia.x *= damp;
      inertia.y *= damp;
      inertia.s *= damp;
      if (Math.abs(inertia.x) < 0.05 && Math.abs(inertia.y) < 0.05) {
        inertia.x = inertia.y = 0;
      }

      const isSnapping = activeScroll !== curScroll;
      if (isSnapping !== wasPaused && prevLoc && !isScreenToScreen) {
        inertia.x = prevLoc.x - v.x;
        inertia.y = prevLoc.y - v.y;
      }
      wasPaused = isSnapping;

      const finalScale = v.s + inertia.s;
      let finalX = v.x + inertia.x;
      let finalY = v.y + inertia.y;

      const currentM = B.lane ? getScreenBottom() : 0;
      let isSettled = true;

      if (isScreenToScreen) {
        if (!efPos) {
          efPos = prevLoc ? { x: prevLoc.x, y: prevLoc.y - prevWhatsAppTop } : { x: finalX, y: finalY - currentM };
        }
        const smoothRate = 1 - Math.exp(-dt / 0.14);
        efPos.x += (finalX - efPos.x) * smoothRate;
        efPos.y += (finalY - currentM - efPos.y) * smoothRate;
        isSettled = Math.hypot(finalX - efPos.x, finalY - currentM - efPos.y) < 1.5;
        finalX = efPos.x;
        finalY = currentM + efPos.y;
      } else {
        if (efPos) {
          inertia.x = (prevLoc?.x ?? finalX) - v.x;
          inertia.y = (prevLoc?.y ?? finalY) - v.y;
          finalX = v.x + inertia.x;
          finalY = v.y + inertia.y;
          efPos = null;
        }
      }
      prevWhatsAppTop = currentM;

      curState = { ...v, x: finalX, y: finalY, s: finalScale };
      SET_DATA(layer, 'anchor', isScreenToScreen ? 'bottom' : 'top');
      layerOffsetY = isScreenToScreen ? (layer.getBoundingClientRect().top || 0) : 0;

      const isHolding = v.t === 0 && isSettled;

      const curStopIdx = v.k;



      if (isHolding) {

        // AT STOP

        if (holdingStopIdx !== curStopIdx) {

          const stopMeta = B.meta[curStopIdx];

          actionQueue = [];

          lookTarget = null;

          holdingStopIdx = curStopIdx;

          stopArrivalTime = now;

          lastMoveTime = now;

          prevTreadmillLeft = null;

          F.reset();

          F.setPose(stopMeta.pose);

          F.face(stopMeta.facing, 0.14);

          F.stride(0);

          F.wag(stopMeta.act === 'basket' ? 0.3 : 0.7);

          F.jolt(0.4);

          basketWakeTime = now + 2.4;

        }



        const m = B.meta[curStopIdx];



        // Treadmill tracking for showroom doors

        if (m.track && !actionQueue.length) {

          const trackLeft = m.track.getBoundingClientRect().left;

          const leftDelta = prevTreadmillLeft === null ? 0 : trackLeft - prevTreadmillLeft;

          prevTreadmillLeft = trackLeft;

          F.walkedTo(-trackLeft / finalScale);

          if (Math.abs(leftDelta) > 0.15) {

            treadmillIdle = 0;

            F.setPose('walk');

            F.stride(1);

            F.face(leftDelta < 0 ? 1 : -1, 0.16);

          } else {

            treadmillIdle += dt;

            if (treadmillIdle > 0.25) {

              F.setPose('stand');

              F.stride(0);

            }

          }

        }



        // Tilt idle

        if (m.act === 'tilt' && !actionQueue.length && now - stopArrivalTime > 1.2) {

          const sinVal = Math.sin(0.9 * now);

          F.cock(sinVal > 0.35 ? 13 : sinVal < -0.35 ? -10 : 0);

        }



        // Basket idle yawns / jolts

        if (m.act === 'basket' && !actionQueue.length && now > basketWakeTime) {

          basketWakeTime = now + 4.5 + 3 * Math.random();

          if (Math.random() < 0.7) {

            F.jolt(0.55);

          } else {

            F.yawn(now, 0.7);

          }

        }



        // Look at scene items

        const isInteracting = (lookTarget && lookTarget.until > now) || (pointerTarget && now - pointerTarget.t < 2.5);

        if (m.looks.length && !isInteracting && now - stopArrivalTime > 0.8 && now - lastLookIdx > 1.7) {

          lastLookIdx = now;

          const nextIdx = (lastPawPrintIdx = (lastPawPrintIdx + 1) % (m.looks.length + 1));

          if (nextIdx < m.looks.length) {

            lookTarget = { el: m.looks[nextIdx], until: now + 1.4 };

          }

        }



        if (Math.abs(scrollDelta) > 0.5) {

          lastMoveTime = now;

        }



        // Idle after 9s of pause

        if (!actionQueue.length && !m.track && m.act !== 'basket' && now - lastMoveTime > 9) {

          lastMoveTime = now;

          if (Math.random() < 0.55) {

            actionQueue = ACTIONS.tilt(actionContext(m), now);

          } else {

            actionQueue = [

              [now, () => F.wag(1)],

              [now + 2.4, () => F.wag(0.7)],

            ];

          }

        }

      } else {

        // TRAVELING BETWEEN STOPS

        if (holdingStopIdx !== -1) {

          holdingStopIdx = -1;

          actionQueue = [];

          F.reset();

        }



        const movedDist = prevLoc ? Math.hypot(finalX - prevLoc.x, finalY - prevLoc.y) : 0;

        stationaryTime = movedDist > 0.25 ? 0 : stationaryTime + dt;



        let isAirborne = v.airborne;
        if (B.lane && v.t > 0) {
          const curS = B.stops[curStopIdx];
          const nxtS = B.stops[curStopIdx + 1];
          if (curS?.sink && v.t < 0.22) {
            isAirborne = scrollDir > 0;
          } else if (nxtS?.sink && v.t > 0.78) {
            isAirborne = scrollDir < 0;
          }
        }

        if (isAirborne) {
          F.setPose('hop');
          F.stride(0);
        } else if (stationaryTime > 0.3) {
          F.setPose('stand');
          F.stride(0);
          if (stationaryTime > 2.6 && stationaryTime - dt <= 2.6) {
            say('coming?', now);
          }
        } else {
          F.setPose('walk');
          F.stride(1);
        }

        if (isScreenToScreen) {
          mobileWalkDist += movedDist;
        }
        F.walkedTo((isScreenToScreen ? mobileWalkDist : v.walked) / Math.max(0.05, finalScale));

        if (prevLoc) {
          const dX = finalX - prevLoc.x;
          if (Math.abs(dX) > 0.6 && Math.abs(dX) > 0.35 * Math.abs(finalY - prevLoc.y)) {
            F.face(dX > 0 ? 1 : -1, 0.16);
          }
        }

        // Paw print drops every 34px of walked distance!
        const printStep = Math.floor(v.walked / (34 * finalScale));
        if (!B.lane && lastPawPrintStop === curStopIdx && printStep !== lastPawPrintIdx && !v.airborne && prevLoc) {

          const isFar = 1 & printStep;

          const legOff = isFar ? 186 : 110;

          const bLeft = finalX - PUP_CENTER.x * finalScale;

          const bTop = finalY - PUP_CENTER.y * finalScale;

          const pX = bLeft + (F.facingDir > 0 ? legOff : PUP_W - legOff) * finalScale;

          const pY = bTop + 226 * finalScale + curScroll - B.mainTop + (isFar ? -4 : 4) * finalScale;

          const ang = Math.atan2(finalY - prevLoc.y + scrollDelta, finalX - prevLoc.x) + Math.PI / 2;

          const pSize = 14 * Math.max(0.75, 1.5 * finalScale);

          const prEl = printEls[printIdx++ % printEls.length];

          if (prEl) {

            prEl.style.transform = `translate(${(pX - pSize / 2).toFixed(1)}px, ${(pY - pSize / 2).toFixed(

              1

            )}px) rotate(${ang.toFixed(3)}rad)`;

            prEl.style.width = prEl.style.height = `${pSize.toFixed(1)}px`;

            prEl.animate(

              [

                { opacity: 0 },

                { opacity: 0.45, offset: 0.08 },

                { opacity: 0.45, offset: 0.5 },

                { opacity: 0 },

              ],

              { duration: 2600, easing: 'ease-out' }

            );

          }

        }

        lastPawPrintStop = curStopIdx;

        lastPawPrintIdx = printStep;

      }



      prevLoc = { x: finalX, y: finalY };



      // Update scene dataset

      const curT = v.t;

      B.meta.forEach((metaObj, idx) => {

        if (metaObj.scene) {

          SET_DATA(metaObj.scene, 'here', String(isHolding && idx === curStopIdx));

          SET_DATA(metaObj.scene, 'visited', String(idx <= curStopIdx || (idx === curStopIdx + 1 && curT > 0.92)));

        }

      });



      // Update gaze

      if (lookTarget && lookTarget.until > now && lookTarget.el) {

        const r = lookTarget.el.getBoundingClientRect();

        F.lookAt({ x: r.left + r.width / 2, y: r.top + r.height / 2 });

      } else if (pointerTarget && now - pointerTarget.t < 2.5) {

        F.lookAt(pointerTarget);

      } else {

        F.lookAt(null);

      }



      // Actor transform

      actor.style.transform = `translate3d(${(finalX - PUP_CENTER.x * finalScale).toFixed(2)}px, ${(
        finalY - PUP_CENTER.y * finalScale - layerOffsetY
      ).toFixed(2)}px, 0)`;

      body.style.transform = `scale(${finalScale.toFixed(4)})`;

      SET_DATA(layer, 'front', String(v.front));

      SET_DATA(actor, 'holding', String(isHolding));



      // Bubble position

      if (bubble.dataset.show === 'true') {

        if (now > bubbleUntil) {

          bubble.dataset.show = 'false';

        }

        const bX = (F.facingDir > 0 ? 214 : PUP_W - 214) * finalScale;

        bubbleAt.style.transform = `translate(${bX.toFixed(1)}px, ${(30 * finalScale).toFixed(1)}px)`;

      }



      F.tick(dt, now);

      rafId = requestAnimationFrame(tick);

    };



    initJourney();

    rafId = requestAnimationFrame(tick);



    let resizeTimer;

    const onResize = () => {

      clearTimeout(resizeTimer);

      resizeTimer = setTimeout(() => {

        if (!isLive || !B) return;

        const layout = buildLayout();

        if (layout.stops.length < 2) return;

        const oldState = curState;
        const wasLane = B.lane;
        B = layout;
        document.documentElement.dataset.pup = layout.lane ? 'lane' : 'live';
        if (wasLane !== layout.lane) {
          holdingStopIdx = -1;
        }
        if (oldState) {
          const newState = evalJourney(layout, window.scrollY);
          inertia.x = oldState.x - newState.x;
          inertia.y = oldState.y - newState.y;
          inertia.s = oldState.s - newState.s;
        }

      }, 120);

    };



    const ro = new ResizeObserver(onResize);

    ro.observe(document.body);

    window.addEventListener('resize', onResize);

    window.addEventListener('load', onResize);

    document.fonts?.ready?.then(onResize);



    return () => {

      cancelAnimationFrame(rafId);

      clearTimeout(resizeTimer);

      ro.disconnect();

      delete document.documentElement.dataset.pup;

      if (layer) layer.hidden = true;

      delete layer.dataset.anchor;

      B?.meta.forEach((m) => {

        if (m.scene) {

          delete m.scene.dataset.here;

          delete m.scene.dataset.visited;

        }

      });

      window.removeEventListener('pointermove', onPointerMove);

      window.removeEventListener('pup:cue', onPupCue);

      window.removeEventListener('focusin', onFocusIn);

      actor.removeEventListener('click', handleActorClick);

      actor.removeEventListener('pointerenter', handlePointerEnter);

      actor.removeEventListener('pointerleave', handlePointerLeave);

      window.removeEventListener('resize', onResize);

      window.removeEventListener('load', onResize);

    };

  }, []);



  return (

    <>

      {/* Probe */}

      <div ref={probeRef} aria-hidden="true" className="pup-probe" />



      {/* Floating Paw Prints */}

      <div ref={printsRef} aria-hidden="true" className="pup-prints">

        {Array.from({ length: 24 }, (_, a) => (

          <svg key={a} viewBox="0 0 64 64">

            <path d="M32 30.5c-7.6 0-15.6 8.3-15.6 15.5 0 5.4 4.2 8.3 9.2 8.3 2.6 0 4.5-1.1 6.4-1.1s3.8 1.1 6.4 1.1c5 0 9.2-2.9 9.2-8.3 0-7.2-8-15.5-15.6-15.5zM14.6 22.3c-3 .1-5.6 3.3-5.6 7s2.6 6.9 5.6 6.9 5.6-3.2 5.6-6.9-2.6-7-5.6-7zM24.2 9.3c-3 0-5.6 3.3-5.6 7.3s2.5 7.3 5.6 7.3 5.6-3.3 5.6-7.3-2.5-7.3-5.6-7.3zM39.8 9.3c-3.1 0-5.6 3.3-5.6 7.3s2.5 7.3 5.6 7.3 5.6-3.3 5.6-7.3-2.5-7.3-5.6-7.3zM49.4 22.3c-3 0-5.6 3.3-5.6 7s2.6 6.9 5.6 6.9 5.6-3.2 5.6-6.9-2.6-7-5.6-7z" />

          </svg>

        ))}

      </div>



      {/* Floating Pup Companion Layer */}

      <div ref={layerRef} aria-hidden="true" className="pup-layer" hidden data-front="true">

        <div ref={actorRef} className="pup-actor">

          <div ref={bodyRef} className="pup-actor__body">

            <svg

              aria-label="Teddy, the TeddyPups puppy, peeking over the quilt"

              focusable="false"

              role="img"

              style={{ overflow: 'visible' }}

              viewBox="0 0 300 240"

            >

              <g data-p="root">

                <ellipse

                  cx="150"

                  cy="230"

                  data-p="shadow"

                  fill="#2a170e"

                  opacity="0"

                  rx="92"

                  ry="7"

                  style={{ transformBox: 'fill-box', transformOrigin: 'center center' }}

                  transform="translate(0 0) scale(1 1)"

                />

                <g

                  data-p="body"

                  opacity="0"

                  transform="translate(0 0) rotate(0 196 206) translate(196 0) scale(1 1) translate(-196 0)"

                >

                  <g data-p="bf" opacity="1" transform="translate(94 192) rotate(0)">

                    <path

                      d="M-14 -14 C-14 4 -12 18 -12 27 C-12 34 -7 36 0 36 C9 36 13 33 13 27 C13 18 14 4 14 -14Z"

                      fill="#e4a352"

                    />

                    <path

                      d="M-14 -14 C-14 4 -12 18 -12 27 C-12 34 -7 36 0 36 C9 36 13 33 13 27 C13 18 14 4 14 -14"

                      fill="none"

                      stroke="#2a170e"

                      strokeLinecap="round"

                      strokeLinejoin="round"

                      strokeWidth="3.4"

                    />

                    <path

                      d="M-3.5 29 v5 M4.5 29 v5"

                      fill="none"

                      stroke="#2a170e"

                      strokeLinecap="round"

                      strokeLinejoin="round"

                      strokeWidth="2.4"

                    />

                  </g>

                  <g data-p="ff" transform="translate(168 192) rotate(0)">

                    <path

                      d="M-11 -14 C-11 4 -12 18 -12 27 C-12 34 -7 36 0 36 C9 36 13 33 13 27 C13 18 11 4 11 -14Z"

                      fill="#e4a352"

                    />

                    <path

                      d="M-11 -14 C-11 4 -12 18 -12 27 C-12 34 -7 36 0 36 C9 36 13 33 13 27 C13 18 11 4 11 -14"

                      fill="none"

                      stroke="#2a170e"

                      strokeLinecap="round"

                      strokeLinejoin="round"

                      strokeWidth="3.4"

                    />

                    <path

                      d="M-3.5 29 v5 M4.5 29 v5"

                      fill="none"

                      stroke="#2a170e"

                      strokeLinecap="round"

                      strokeLinejoin="round"

                      strokeWidth="2.4"

                    />

                  </g>

                  <g data-p="tail" transform="rotate(-20 84 150)">

                    <path

                      d="M86 152 C80 146 76 140 74 136"

                      fill="none"

                      stroke="#2a170e"

                      strokeLinecap="round"

                      strokeLinejoin="round"

                      strokeWidth="9"

                    />

                    <path

                      d="M86 152 C80 146 76 140 74 136"

                      fill="none"

                      stroke="#f2be6b"

                      strokeLinecap="round"

                      strokeWidth="4"

                    />

                    <path

                      d="M70.0 110.0Q78.1 105.0 80.9 113.7Q90.5 114.8 86.7 123.2Q93.4 129.9 84.7 134.0Q85.2 143.1 75.8 141.0Q70.0 148.3 64.2 141.0Q54.8 143.1 55.3 134.0Q46.6 129.9 53.3 123.2Q49.5 114.8 59.1 113.7Q61.9 105.0 70.0 110.0Z"

                      fill="#f2be6b"

                      stroke="#2a170e"

                      strokeLinecap="round"

                      strokeLinejoin="round"

                      strokeWidth="3.4"

                    />

                  </g>

                  <g data-p="bn" opacity="1" transform="translate(110 194) rotate(0)">

                    <path

                      d="M-15 -14 C-15 4 -12 16 -12 25 C-12 32 -7 34 0 34 C9 34 13 31 13 25 C13 16 15 4 15 -14Z"

                      fill="#f2be6b"

                    />

                    <path

                      d="M-15 -14 C-15 4 -12 16 -12 25 C-12 32 -7 34 0 34 C9 34 13 31 13 25 C13 16 15 4 15 -14"

                      fill="none"

                      stroke="#2a170e"

                      strokeLinecap="round"

                      strokeLinejoin="round"

                      strokeWidth="3.4"

                    />

                    <path

                      d="M-3.5 27 v5 M4.5 27 v5"

                      fill="none"

                      stroke="#2a170e"

                      strokeLinecap="round"

                      strokeLinejoin="round"

                      strokeWidth="2.4"

                    />

                  </g>

                  <path

                    d="M76.8 175.6Q69.0 167.9 78.2 160.7Q76.6 151.8 90.3 147.3Q95.2 138.9 110.9 137.9Q121.6 131.3 136.7 134.0Q151.1 130.5 162.9 136.4Q178.7 136.4 185.3 144.5Q199.7 148.2 199.7 157.1Q210.3 163.7 203.9 171.9Q208.7 180.4 197.0 186.3Q195.3 195.2 180.3 198.0Q172.3 205.7 156.6 204.8Q143.7 210.0 130.0 205.6Q114.5 207.4 105.1 200.2Q89.7 198.3 86.3 189.6Q73.6 184.3 76.8 175.6Z"

                    fill="#f2be6b"

                    stroke="#2a170e"

                    strokeLinecap="round"

                    strokeLinejoin="round"

                    strokeWidth="3.4"

                  />

                  <path

                    d="M182.7 196.4Q169.4 196.9 166.6 183.0Q156.1 174.1 162.3 161.5Q159.6 147.6 171.9 142.2Q178.2 129.7 191.0 134.0Q203.3 128.7 210.5 140.8Q223.1 145.2 221.3 159.3Q228.4 171.5 218.5 181.0Q216.6 195.1 203.2 195.7Q193.3 205.1 182.7 196.4Z"

                    fill="#f2be6b"

                    stroke="#2a170e"

                    strokeLinecap="round"

                    strokeLinejoin="round"

                    strokeWidth="3.4"

                  />

                  <g data-p="fn" transform="translate(186 194) rotate(0)">

                    <path

                      d="M-12 -14 C-12 4 -12 16 -12 25 C-12 32 -7 34 0 34 C9 34 13 31 13 25 C13 16 12 4 12 -14Z"

                      fill="#f2be6b"

                    />

                    <path

                      d="M-12 -14 C-12 4 -12 16 -12 25 C-12 32 -7 34 0 34 C9 34 13 31 13 25 C13 16 12 4 12 -14"

                      fill="none"

                      stroke="#2a170e"

                      strokeLinecap="round"

                      strokeLinejoin="round"

                      strokeWidth="3.4"

                    />

                    <path

                      d="M-3.5 27 v5 M4.5 27 v5"

                      fill="none"

                      stroke="#2a170e"

                      strokeLinecap="round"

                      strokeLinejoin="round"

                      strokeWidth="2.4"

                    />

                  </g>

                </g>

                <g data-p="haunch" opacity="0" transform="translate(0 0)">

                  <path

                    d="M80.0 204.0Q75.1 194.9 85.7 189.9Q88.4 180.2 100.7 181.2Q110.0 174.6 119.3 181.2Q131.6 180.2 134.3 189.9Q144.9 194.9 140.0 204.0Q144.9 213.1 134.3 218.1Q131.6 227.8 119.3 226.8Q110.0 233.4 100.7 226.8Q88.4 227.8 85.7 218.1Q75.1 213.1 80.0 204.0Z"

                    fill="#f2be6b"

                    stroke="#2a170e"

                    strokeLinecap="round"

                    strokeLinejoin="round"

                    strokeWidth="3.4"

                  />

                  <path

                    d="M112 214 C126 212 142 214 146 221 C148 226 144 229 136 229 L116 229 C108 229 104 224 106 219 Z"

                    fill="#f2be6b"

                    stroke="#2a170e"

                    strokeLinecap="round"

                    strokeLinejoin="round"

                    strokeWidth="3.4"

                  />

                  <path

                    d="M132 222v5M139 222v5"

                    fill="none"

                    stroke="#2a170e"

                    strokeLinecap="round"

                    strokeLinejoin="round"

                    strokeWidth="2.4"

                  />

                </g>

                <g data-p="head" transform="translate(0 4) rotate(0 212 100)">

                  <path

                    d="M178 146 Q212 162 246 146 L246 154 Q212 170 178 154 Z"

                    fill="#a24a1a"

                    stroke="#2a170e"

                    strokeLinecap="round"

                    strokeLinejoin="round"

                    strokeWidth="3"

                  />

                  <path

                    d="M212 160 C212 156 206 155 206 159.4 C206 163 212 166.6 212 168.4 C212 166.6 218 163 218 159.4 C218 155 212 156 212 160 Z"

                    fill="#fbe3b4"

                    stroke="#2a170e"

                    strokeLinecap="round"

                    strokeLinejoin="round"

                    strokeWidth="2.4"

                  />

                  <path

                    d="M177.1 78.7Q186.9 70.8 186.6 87.4Q196.0 89.9 189.9 105.5Q195.2 117.3 185.5 126.0Q184.7 142.8 175.2 141.2Q168.7 156.5 162.9 145.3Q153.1 153.2 153.4 136.6Q144.0 134.1 150.1 118.5Q144.8 106.7 154.5 98.0Q155.3 81.2 164.8 82.8Q171.3 67.5 177.1 78.7Z"

                    data-p="earL"

                    fill="#e4a352"

                    stroke="#2a170e"

                    strokeLinecap="round"

                    strokeLinejoin="round"

                    strokeWidth="3.4"

                    transform="rotate(-6 174 82)"

                  />

                  <path

                    d="M246.9 78.7Q252.7 67.5 259.2 82.8Q268.7 81.2 269.5 98.0Q279.2 106.7 273.9 118.5Q280.0 134.1 270.6 136.6Q270.9 153.2 261.1 145.3Q255.3 156.5 248.8 141.2Q239.3 142.8 238.5 126.0Q228.8 117.3 234.1 105.5Q228.0 89.9 237.4 87.4Q237.1 70.8 246.9 78.7Z"

                    data-p="earR"

                    fill="#e4a352"

                    stroke="#2a170e"

                    strokeLinecap="round"

                    strokeLinejoin="round"

                    strokeWidth="3.4"

                    transform="rotate(6 250 82)"

                  />

                  <path

                    d="M212.0 54.0Q223.4 48.2 231.5 57.5Q244.5 56.1 248.1 67.5Q260.7 70.7 259.1 82.4Q269.4 89.7 263.0 100.0Q269.4 110.3 259.1 117.6Q260.7 129.3 248.1 132.5Q244.5 143.9 231.5 142.5Q223.4 151.8 212.0 146.0Q200.6 151.8 192.5 142.5Q179.5 143.9 175.9 132.5Q163.3 129.3 164.9 117.6Q154.6 110.3 161.0 100.0Q154.6 89.7 164.9 82.4Q163.3 70.7 175.9 67.5Q179.5 56.1 192.5 57.5Q200.6 48.2 212.0 54.0Z"

                    fill="#f2be6b"

                    stroke="#2a170e"

                    strokeLinecap="round"

                    strokeLinejoin="round"

                    strokeWidth="3.4"

                  />

                  <path

                    d="M195.0 52.0Q190.7 45.8 200.0 43.5Q203.2 36.9 212.0 40.0Q220.8 36.9 224.0 43.5Q233.3 45.8 229.0 52.0Q233.3 58.2 224.0 60.5Q220.8 67.1 212.0 64.0Q203.2 67.1 200.0 60.5Q190.7 58.2 195.0 52.0Z"

                    fill="#f2be6b"

                    stroke="#2a170e"

                    strokeLinecap="round"

                    strokeLinejoin="round"

                    strokeWidth="3"

                  />

                  <path

                    d="M188 120 C188 106 200 100 212 100 C224 100 236 106 236 120 C236 133 225 140 212 140 C199 140 188 133 188 120 Z"

                    fill="#fbe3b4"

                  />

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

                  <path

                    d="M186.5 101 Q194 91.5 201.5 101 M222.5 101 Q230 91.5 237.5 101"

                    data-p="happy"

                    fill="none"

                    opacity="0"

                    stroke="#2a170e"

                    strokeLinecap="round"

                    strokeLinejoin="round"

                    strokeWidth="3.4"

                  />

                  <path

                    d="M186.5 97 Q194 103.5 201.5 97 M222.5 97 Q230 103.5 237.5 97"

                    data-p="shut"

                    fill="none"

                    opacity="0"

                    stroke="#2a170e"

                    strokeLinecap="round"

                    strokeLinejoin="round"

                    strokeWidth="3.4"

                  />

                  <path

                    d="M204.5 111.5 Q212 107.2 219.5 111.5 Q218.2 118.4 212 120 Q205.8 118.4 204.5 111.5 Z"

                    fill="#2a170e"

                  />

                  <path

                    d="M212 120 V124.5 M212 124.5 Q207.2 129.6 202.8 125.2 M212 124.5 Q216.8 129.6 221.2 125.2"

                    fill="none"

                    stroke="#2a170e"

                    strokeLinecap="round"

                    strokeLinejoin="round"

                    strokeWidth="3"

                  />

                  <path

                    d="M207.6 127.4 Q212 136.6 216.4 127.4 Z"

                    data-p="tongue"

                    fill="#e98c8c"

                    opacity="1"

                    stroke="#2a170e"

                    strokeLinejoin="round"

                    strokeWidth="2.2"

                  />

                  <g data-p="mouth" opacity="0">

                    <path

                      d="M203 126 Q212 122 221 126 Q219 138 212 139 Q205 138 203 126 Z"

                      fill="#6b2a1c"

                      stroke="#2a170e"

                      strokeLinecap="round"

                      strokeLinejoin="round"

                      strokeWidth="2.6"

                    />

                    <path

                      d="M206.5 133.5 Q212 130 217.5 133.5 Q215 138 212 138 Q209 138 206.5 133.5 Z"

                      fill="#e98c8c"

                    />

                  </g>

                </g>

                <g data-p="ledge" opacity="1">

                  <path

                    d="M175 159 C175 148 181 142 190 142 C199 142 205 148 205 159 Z M219 159 C219 148 225 142 234 142 C243 142 249 148 249 159 Z"

                    fill="#f2be6b"

                    stroke="#2a170e"

                    strokeLinecap="round"

                    strokeLinejoin="round"

                    strokeWidth="3.4"

                  />

                  <path

                    d="M186 153 v-4.5 M194 153 v-4.5 M230 153 v-4.5 M238 153 v-4.5"

                    fill="none"

                    stroke="#2a170e"

                    strokeLinecap="round"

                    strokeLinejoin="round"

                    strokeWidth="2.4"

                  />

                </g>

              </g>

            </svg>

          </div>

          <span ref={bubbleAtRef} className="pup-bubble-at">

            <span ref={bubbleRef} className="pup-bubble" data-show="false" />

          </span>

        </div>

      </div>

    </>

  );

}

