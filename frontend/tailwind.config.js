/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ['./index.html', './src/**/*.{js,jsx,ts,tsx}'], 
    theme: {
      extend: {
        fontFamily: {
          allura: ['Allura', 'cursive'], // Add Allura font
        },
      },
    },
    plugins: [],
  };
  