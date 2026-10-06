/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        brand: {
          50: '#F0F5FA',
          100: '#E1EBF5',
          200: '#C2D7EC',
          500: '#1C5B96',
          600: '#0E3B68',
          800: '#0B2545',
          900: '#06162A',
        },
        ore: {
          amber: '#D97706',
          gold: '#F59E0B',
          bronze: '#B45309',
          dark: '#18181B',
        },
        cildark: '#0B132B',
        cilslate: '#1C2541',
      },
      fontFamily: {
        sans: ['"Plus Jakarta Sans"', 'sans-serif'],
        mono: ['"JetBrains Mono"', 'monospace'],
      },
    },
  },
  plugins: [],
}
