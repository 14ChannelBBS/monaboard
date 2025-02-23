document.addEventListener("DOMContentLoaded", () => {
  var select = document.getElementById("theme");

  if (
    select.value === "auto" &&
    window.matchMedia("(prefers-color-scheme: dark)").matches
  ) {
    document.documentElement.setAttribute("data-bs-theme", "dark");
  } else {
    document.documentElement.setAttribute("data-bs-theme", select.value);
  }

  select.onchange = function () {
    if (
      this.value === "auto" &&
      window.matchMedia("(prefers-color-scheme: dark)").matches
    ) {
      document.documentElement.setAttribute("data-bs-theme", "dark");
    } else {
      document.documentElement.setAttribute("data-bs-theme", this.value);
    }
  };
});
