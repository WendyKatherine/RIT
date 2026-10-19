/**
 * Reveal de títulos por palabra — GSAP + ScrollTrigger (cargador compartido).
 *
 * Uso: agregale data-title-reveal a cualquier título:
 *
 *   <h2 data-title-reveal>Proyectos que <span class="grad-text">transforman</span></h2>
 *
 * El script parte el texto en palabras SIN romper el HTML interno (los spans
 * con gradiente siguen funcionando) y las hace subir desde una máscara.
 *
 * Degradación: sin JS, sin red o con prefers-reduced-motion, el título se ve
 * normal (el corte en palabras solo ocurre dentro del script).
 */
(function () {
  'use strict';

  const WORD = 'tr-w';
  const INNER = 'tr-wi';

  // Divide un nodo en palabras preservando el markup (span, strong, etc.)
  function splitNode(node, target) {
    Array.prototype.slice.call(node.childNodes).forEach(function (child) {
      if (child.nodeType === 3) {
        child.nodeValue.split(/(\s+)/).forEach(function (part) {
          if (!part) return;
          if (/^\s+$/.test(part)) {
            target.appendChild(document.createTextNode(part));
            return;
          }
          const outer = document.createElement('span');
          outer.className = WORD;
          const inner = document.createElement('span');
          inner.className = INNER;
          inner.textContent = part;
          outer.appendChild(inner);
          target.appendChild(outer);
        });
        return;
      }
      if (child.nodeType === 1) {
        const clone = document.createElement(child.tagName);
        Array.prototype.forEach.call(child.attributes, function (attr) {
          clone.setAttribute(attr.name, attr.value);
        });
        splitNode(child, clone);
        target.appendChild(clone);
      }
    });
  }

  function split(title) {
    if (title.dataset.trReady) return null;
    const holder = document.createElement('span');
    holder.className = 'tr';
    splitNode(title, holder);
    title.innerHTML = '';
    title.appendChild(holder);
    title.dataset.trReady = '1';
    return holder.querySelectorAll('.' + INNER);
  }

  // Red de seguridad: si por cualquier motivo el ScrollTrigger no llega a
  // dispararse (layout shift, pin de otra sección, refresh desactualizado) y
  // las palabras quedan ocultas, las forzamos visibles cuando el título ya
  // está claramente en pantalla. El retardo le da tiempo al ScrollTrigger de
  // dispararse y animar antes de decidir que quedó atascado; así el título
  // NUNCA queda invisible y no pisamos la animación en el camino normal.
  function guard(title, words, lib) {
    if (!('IntersectionObserver' in window)) return;
    let timer = null;
    const observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting || timer) return;
          timer = setTimeout(function () {
            const stuck = Array.prototype.some.call(words, function (w) {
              return parseFloat(getComputedStyle(w).opacity) === 0;
            });
            if (stuck) {
              lib.gsap.set(words, { yPercent: 0, opacity: 1, overwrite: true, clearProps: 'all' });
            }
            observer.disconnect();
          }, 1600);
        });
      },
      { threshold: 0.5 }
    );
    observer.observe(title);
  }

  function boot() {
    const titles = document.querySelectorAll('[data-title-reveal]');
    if (!titles.length) return;
    if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    if (!window.ritGsap) return;

    window.ritGsap.load().then(function (lib) {
      titles.forEach(function (title) {
        const words = split(title);
        if (!words || !words.length) return;
        lib.gsap.from(words, {
          yPercent: 110,
          opacity: 0,
          duration: 0.75,
          ease: 'power3.out',
          stagger: 0.045,
          scrollTrigger: { trigger: title, start: 'top 88%', once: true },
        });
        guard(title, words, lib);
      });
      lib.ScrollTrigger.refresh();
    }).catch(function () { /* sin red: títulos normales */ });

    // Las fuentes/imágenes pueden llegar después de la primera medición y
    // correr las posiciones: refrescamos al terminar la carga para que los
    // triggers apunten al sitio correcto.
    window.addEventListener('load', function () {
      if (window.gsap && window.ScrollTrigger) {
        window.ScrollTrigger.refresh();
      }
    });
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot);
  else boot();
})();
