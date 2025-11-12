/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./_layouts/**/*.html",
    "./_pages/**/*.{html,md}",
    "./_projects/**/*.{html,md}",
    "./_team/**/*.{html,md}",
    "./*.html",
    "./*.md"
  ],
  theme: {
    extend: {
      colors: {
        // VCH Brand Colors (preserved)
        'vch-green': '#8fbc3f',
        'vch-green-dark': '#5A8037',
        'vch-green-accessible': '#4A7023',
        'vch-yellow': '#F1C144',
        'vch-orange': '#F4A300',

        // Dark Theme Colors (Resuld-inspired)
        'vch-dark': '#1e1e1e',
        'vch-dark-lighter': '#2a2a2a',
        'vch-dark-card': '#252525',

        // Text Colors for Dark Theme
        'vch-text-light': '#ffffff',
        'vch-text-gray': '#b0b0b0',
        'vch-text-muted': '#808080',

        // Legacy (for compatibility)
        'vch-gray': '#333333',
        'vch-light-gray': '#666666',
        'vch-bg': '#F9F9F9'
      }
    }
  },
  plugins: []
}
