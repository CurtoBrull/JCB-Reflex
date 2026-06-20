(function () {
  var stored = localStorage.getItem("theme");
  var preferLight =
    window.matchMedia && window.matchMedia("(prefers-color-scheme: light)").matches;
  var isLight = stored === "light" || (!stored && preferLight);

  if (isLight) {
    document.documentElement.classList.add("light-theme");
    // Sincronizar icono cuando el DOM esté listo
    function syncIcon() {
      var s = document.getElementById("theme-icon-sun");
      var m = document.getElementById("theme-icon-moon");
      if (s) s.style.display = "inline";
      if (m) m.style.display = "none";
    }
    if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", syncIcon);
    } else {
      syncIcon();
      setTimeout(syncIcon, 300);
    }
  }
})();
