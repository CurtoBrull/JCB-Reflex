(function () {
  var observed = new WeakSet();

  var io = new IntersectionObserver(
    function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          io.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.12, rootMargin: "0px 0px -40px 0px" }
  );

  function attachObserver(el) {
    if (!observed.has(el)) {
      observed.add(el);
      io.observe(el);
    }
  }

  function scanAndObserve(root) {
    (root || document).querySelectorAll(".scroll-reveal").forEach(attachObserver);
  }

  // MutationObserver para detectar elementos renderizados por React
  var mo = new MutationObserver(function (mutations) {
    mutations.forEach(function (m) {
      m.addedNodes.forEach(function (node) {
        if (node.nodeType !== 1) return;
        if (node.classList && node.classList.contains("scroll-reveal")) {
          attachObserver(node);
        }
        if (node.querySelectorAll) scanAndObserve(node);
      });
    });
  });

  function init() {
    scanAndObserve(document);
    mo.observe(document.body, { childList: true, subtree: true });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
