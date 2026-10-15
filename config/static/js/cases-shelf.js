/**
 * Estante de casos — scroll horizontal anclado con GSAP + ScrollTrigger.
 *
 * La sección se ancla (pin) mientras el riel se desplaza en horizontal, y el
 * índice + la barra de progreso siguen el scroll.
 *
 * GSAP viene del cargador compartido (js/gsap-loader.js). Se pide cuando la
 * sección se acerca a pantalla, así no pesa en la carga inicial.
 * Si no hay red o el usuario pide menos movimiento, la sección queda como
 * carrusel horizontal con snap (CSS). Nunca se rompe.
 *
 * TODO (slice vendor): cuando GSAP se sirva desde el repo, acá no cambia nada:
 * solo se actualiza SOURCES en gsap-loader.js.
 */
(function () {
  'use strict';

  function init(root, gsap, ScrollTrigger) {
    const track = root.querySelector('[data-shelf-track]');
    const viewport = root.querySelector('[data-shelf-viewport]');
    const current = root.querySelector('[data-shelf-current]');
    const bar = root.querySelector('[data-shelf-progress]');
    if (!track || !viewport) return;

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
    if (!window.ritGsap) return;

    const media = window.matchMedia;
    const reduce = media && media('(prefers-reduced-motion: reduce)').matches;
    const narrow = media && media('(max-width: 1024px)').matches;
    if (reduce || narrow) return; // se queda el carrusel con snap

    const run = function () {
      window.ritGsap
        .load()
        .then(function (lib) {
          init(root, lib.gsap, lib.ScrollTrigger);
        })
        .catch(function () { /* sin red: queda el fallback */ });
    };

    if (!('IntersectionObserver' in window)) {
      run();
      return;
    }

    const observer = new IntersectionObserver(
      function (entries, obs) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          obs.disconnect();
          run();
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
