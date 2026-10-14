/**
 * Estante de casos — scroll horizontal anclado con GSAP + ScrollTrigger.
 *
 * La sección se ancla (pin) mientras el riel se desplaza en horizontal, y el
 * índice + la barra de progreso siguen el scroll.
 *
 * Estrategia de carga:
 * - GSAP se pide por CDN **solo cuando la sección se acerca a pantalla**
 *   (IntersectionObserver con rootMargin), así no pesa en la carga inicial.
 * - Si no hay red, falla la carga o el usuario pide menos movimiento, la
 *   sección queda como carrusel horizontal con snap (CSS). Nunca se rompe.
 * - En <=1024px no se inicializa: ahí manda el carrusel táctil.
 *
 * TODO (slice vendor): descargar gsap.min.js + ScrollTrigger.min.js a
 * config/static/vendor/gsap/ y servirlos nosotros, en vez de CDN.
 */
(function () {
  'use strict';

  const VERSION = '3.15.0';
  const SOURCES = [
    'https://cdn.jsdelivr.net/npm/gsap@' + VERSION + '/dist/gsap.min.js',
    'https://cdn.jsdelivr.net/npm/gsap@' + VERSION + '/dist/ScrollTrigger.min.js',
  ];

  function load(src) {
    return new Promise(function (resolve, reject) {
      const script = document.createElement('script');
      script.src = src;
      script.async = false;
      script.onload = resolve;
      script.onerror = reject;
      document.head.appendChild(script);
    });
  }

  function init(root) {
    if (!window.gsap || !window.ScrollTrigger) return;
    const track = root.querySelector('[data-shelf-track]');
    const viewport = root.querySelector('[data-shelf-viewport]');
    const current = root.querySelector('[data-shelf-current]');
    const bar = root.querySelector('[data-shelf-progress]');
    if (!track || !viewport) return;

    const gsap = window.gsap;
    gsap.registerPlugin(window.ScrollTrigger);

    const distance = function () {
      return Math.max(0, track.scrollWidth - viewport.clientWidth);
    };

    document.documentElement.classList.add('has-shelf');
    root.classList.add('is-shelf');

    gsap.to(track, {
      x: function () {
        return -distance();
      },
      ease: 'none',
      scrollTrigger: {
        trigger: root,
        start: 'top top',
        end: function () {
          return '+=' + distance();
        },
        scrub: 1,
        pin: true,
        anticipatePin: 1,
        invalidateOnRefresh: true,
        onUpdate: function (self) {
          if (bar) {
            bar.style.width = (self.progress * 100).toFixed(2) + '%';
          }
          if (current) {
            const total = track.querySelectorAll('[data-shelf-card]').length || 1;
            const index = Math.min(total, Math.floor(self.progress * total) + 1);
            current.textContent = String(index).padStart(2, '0');
          }
        },
      },
    });
  }

  function boot() {
    const root = document.querySelector('[data-shelf]');
    if (!root) return;

    const media = window.matchMedia;
    const reduce = media && media('(prefers-reduced-motion: reduce)').matches;
    const narrow = media && media('(max-width: 1024px)').matches;
    if (reduce || narrow) return; // se queda el carrusel con snap

    if (!('IntersectionObserver' in window)) {
      Promise.all(SOURCES.map(load)).then(function () { init(root); }).catch(function () {});
      return;
    }

    const observer = new IntersectionObserver(
      function (entries, obs) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          obs.disconnect();
          Promise.all(SOURCES.map(load))
            .then(function () { init(root); })
            .catch(function () { /* sin red: queda el fallback */ });
        });
      },
      { rootMargin: '400px 0px' }
    );
    observer.observe(root);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
