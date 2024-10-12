/** @type {import('tailwindcss').Config} */
module.exports = {
	darkMode: "media",
	content: ['./templates/**/*.html'],
	theme: {
	  extend: {
		fontFamily: {
		  sarabun: ["Sarabun"],
		  mitr: ["Mitr"],
		  prompt: ["Prompt"],
		}
	  },
	},
	plugins: [],
  }