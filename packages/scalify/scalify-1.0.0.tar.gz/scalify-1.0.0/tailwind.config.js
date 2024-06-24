/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./docs/**/*.{html,js}"],
  theme: {
    extend: {
      colors: {
        'scalify-blue': 'rgba(24, 21, 68)',
      },
    },
  },
}