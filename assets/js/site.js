/* New Madison Development — small site script. Everything works without it; this adds the menu and motion. */
(function () {
  var doc = document.documentElement;
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Fade the headline in once fonts and first paint are ready.
  requestAnimationFrame(function () { requestAnimationFrame(function () { doc.classList.add('is-loaded'); }); });

  // Mobile menu
  var toggle = document.querySelector('.menu-toggle');
  if (toggle) {
    toggle.addEventListener('click', function () {
      var open = doc.classList.toggle('menu-open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && doc.classList.contains('menu-open')) {
        doc.classList.remove('menu-open');
        toggle.setAttribute('aria-expanded', 'false');
        toggle.focus();
      }
    });
  }

  // Header: thin rule once scrolled; slides away when scrolling down, returns when scrolling up.
  var header = document.querySelector('.site-header');
  var lastY = window.scrollY;
  var heroImg = document.querySelector('[data-parallax] img');
  var ticking = false;
  function onScroll() {
    var y = window.scrollY;
    if (header) {
      header.classList.toggle('is-scrolled', y > 8);
      var goingDown = y > lastY && y > 240;
      if (!doc.classList.contains('menu-open')) header.classList.toggle('is-hidden', goingDown);
    }
    if (heroImg && !reduceMotion) {
      var r = heroImg.parentElement.getBoundingClientRect();
      if (r.bottom > 0 && r.top < window.innerHeight) {
        var p = Math.min(Math.max(-r.top / r.height, 0), 1);
        heroImg.style.transform = 'scale(' + (1 + p * 0.08).toFixed(4) + ') translateY(' + (p * 4).toFixed(2) + '%)';
      }
    }
    lastY = y;
    ticking = false;
  }
  window.addEventListener('scroll', function () {
    if (!ticking) { requestAnimationFrame(onScroll); ticking = true; }
  }, { passive: true });
  onScroll();

  // Reveal blocks as they enter the viewport.
  var items = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && !reduceMotion) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) { entry.target.classList.add('is-in'); io.unobserve(entry.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    items.forEach(function (el) { io.observe(el); });
  } else {
    items.forEach(function (el) { el.classList.add('is-in'); });
  }

  // Map: highlight a pin and its list row together.
  document.querySelectorAll('[data-pin]').forEach(function (el) {
    var id = el.getAttribute('data-pin');
    function set(on) {
      document.querySelectorAll('[data-pin="' + id + '"]').forEach(function (m) { m.classList.toggle('is-active', on); });
    }
    el.addEventListener('mouseenter', function () { set(true); });
    el.addEventListener('mouseleave', function () { set(false); });
    el.addEventListener('focus', function () { set(true); });
    el.addEventListener('blur', function () { set(false); });
  });

  // Footer year
  document.querySelectorAll('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
