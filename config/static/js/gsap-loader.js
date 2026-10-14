/**
 * Cargador compartido de GSAP (window.ritGsap).
 *
 * Las secciones que animan piden las librerías por acá, así se descargan UNA
 * sola vez aunque haya varios efectos en la página:
 *
 *   window.ritGsap.load().then(function (lib) {
 *     lib.gsap.from(...);            // lib.ScrollTrigger ya está registrado
 *   });
 *
 * Ventaja del punto único: cuando se vendorice GSAP (pasarlo al repo en vez de
 * CDN) se cambia SOLO SOURCES acá y todos los efectos quedan locales.
 */
(function () {
  'use strict';

  const VERSION = '3.15.0';
  const SOURCES = [
    'https://cdn.jsdelivr.net/npm/gsap@' + VERSION + '/dist/gsap.min.js',
    'https://cdn.jsdelivr.net/npm/gsap@' + VERSION + '/dist/ScrollTrigger.min.js',
  ];

  let pending = null;

  function loadOne(src) {
    return new Promise(function (resolve, reject) {
      const script = document.createElement('script');
      script.src = src;
      script.async = false;
      script.onload = resolve;
      script.onerror = reject;
      document.head.appendChild(script);
    });
  }

  function load() {
    if (pending) return pending;
    pending = Promise.all(SOURCES.map(loadOne)).then(function () {
      window.gsap.registerPlugin(window.ScrollTrigger);
      return { gsap: window.gsap, ScrollTrigger: window.ScrollTrigger };
    });
    return pending;
  }

  window.ritGsap = { load: load, VERSION: VERSION };
})();
