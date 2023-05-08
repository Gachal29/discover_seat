module.exports = {
  variants: {
    extend: {
    },
  },
  content: [
    "./*.html",
    "../discover_seat/templates/**/*.html",
    "../discover_seat/**/forms.py",
    "../discover_seat/js/*.js"
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require("daisyui"),
  ],
  daisyui: {
  }
}