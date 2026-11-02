/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        cocoa: {
          DEFAULT: '#2a170e',
          soft: '#5a3a28',
        },
        milk: {
          DEFAULT: '#fffdf8',
        },
        honey: {
          DEFAULT: '#f2be6b',
          soft: '#fbe3b4',
        },
        toffee: {
          DEFAULT: '#c2622b',
          deep: '#a24a1a',
          ink: '#8e3f15',
        },
        sky: {
          DEFAULT: '#bfddf5',
          deep: '#2f6e9e',
        },
        blush: {
          DEFAULT: '#f9cdbf',
        }
      },
      fontFamily: {
        plush: ['Fraunces', 'Georgia', 'serif'],
        display: ['Fraunces', 'Georgia', 'serif'],
        sans: ['Figtree', 'system-ui', 'sans-serif'],
        scrawl: ['"Shantell Sans"', 'cursive'],
        hand: ['"Shantell Sans"', 'cursive'],
      }
    },
  },
  plugins: [],
}

