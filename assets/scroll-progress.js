(function () {
  // ── Barra de progreso ──────────────────────────────────────────────────────
  var bar = document.createElement("div");
  bar.id = "scroll-progress-bar";
  document.body.prepend(bar);

  // ── Sección activa en navbar ───────────────────────────────────────────────
  var SECTION_IDS = ["inicio", "sobremi", "skills", "curriculum", "portfolio", "contacto"];
  var NAVBAR_H = 90;

  function getNavLinks() {
    return document.querySelectorAll("a.nav-link, a.mobile-nav-link");
  }

  function updateOnScroll() {
    // Progreso
    var scrollTop = window.scrollY;
    var docHeight = document.documentElement.scrollHeight - window.innerHeight;
    bar.style.width =
      (docHeight > 0 ? Math.min(100, (scrollTop / docHeight) * 100) : 0) + "%";

    // Sección activa: la que acaba de pasar el borde inferior del navbar
    var trigger = scrollTop + NAVBAR_H + 10;
    var active = null;
    SECTION_IDS.forEach(function (id) {
      var el = document.getElementById(id);
      if (el && el.offsetTop <= trigger) active = id;
    });

    if (active) {
      getNavLinks().forEach(function (link) {
        link.classList.toggle("active", link.getAttribute("href") === "#" + active);
      });
    }
  }

  function init() {
    window.addEventListener("scroll", updateOnScroll, { passive: true });
    updateOnScroll();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
