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
        'vch-green': '#7DB04D',
        'vch-green-dark': '#5A8037',
        'vch-yellow': '#F1C144',
        'vch-orange': '#F4A300',
        'vch-gray': '#333333',
        'vch-light-gray': '#666666',
        'vch-bg': '#F9F9F9'
      }
    }
  },
  plugins: []
}
