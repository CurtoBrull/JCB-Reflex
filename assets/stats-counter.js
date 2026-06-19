(function () {
  function easeOut(t) {
    return 1 - Math.pow(1 - t, 3);
  }

  // Resuelve el target numérico. Soporta "auto:YYYY-MM" para calcular años
  // transcurridos desde esa fecha (actualización automática sin re-deploy).
  function resolveTarget(el) {
    var raw = el.getAttribute("data-target") || "0";
    if (raw.indexOf("auto:") === 0) {
      var parts = raw.slice(5).split("-");
      var start = new Date(parseInt(parts[0], 10), parseInt(parts[1], 10) - 1, 1);
      var years = Math.floor((Date.now() - start) / (1000 * 60 * 60 * 24 * 365.25));
      el.setAttribute("data-target", String(years));
      return years;
    }
    return parseInt(raw, 10);
  }

  var animated = new Set();

  function animateCounter(el) {
    animated.add(el);
    var target = resolveTarget(el);
    var suffix = el.getAttribute("data-suffix") || "";
    var duration = 1800;
    var startTime = null;

    function step(timestamp) {
      if (!startTime) startTime = timestamp;
      var elapsed = Math.min(timestamp - startTime, duration);
      var value = Math.floor(easeOut(elapsed / duration) * target);
      el.textContent = value.toLocaleString("es-ES") + suffix;
      if (elapsed < duration) {
        requestAnimationFrame(step);
      } else {
        el.textContent = target.toLocaleString("es-ES") + suffix;
      }
    }

    requestAnimationFrame(step);
  }

  var io = new IntersectionObserver(
    function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          animateCounter(entry.target);
          io.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.2 }
  );

  function scan() {
    document.querySelectorAll(".stat-number[data-target]").forEach(function (el) {
      if (!animated.has(el)) {
        io.observe(el);
      }
    });
  }

  function init() {
    scan();
    // Fallbacks para contenido renderizado por React
    [300, 700, 1500].forEach(function (ms) {
      setTimeout(scan, ms);
    });
    // MutationObserver para cambios futuros del DOM
    new MutationObserver(scan).observe(document.body, {
      childList: true,
      subtree: true,
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
