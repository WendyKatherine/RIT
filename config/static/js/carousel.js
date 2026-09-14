/**
 * Carrusel lineal infinito — sin dependencias.
 *
 * Convierte un riel ([data-carousel-track]) en un carrusel infinito: clona
 * tarjetas a los dos lados para que **nunca se vean huecos**, salta sin
 * animación al caer en un clon (loop sin costura) y expone botones, teclado y
 * arrastre.
 *
 * Sin JS el riel sigue siendo scroll horizontal nativo (ver home.css), así que
 * la sección nunca queda rota.
 *
 * Contrato del markup:
 *   <section data-carousel>
 *     <button data-carousel-prev> <button data-carousel-next>
 *     <span class="svc-current">01</span>
 *     <div data-carousel-track><article>…</article>…</div>
 *   </section>
 */
(function () {
  'use strict';

  const MAX_CLONES_PER_SIDE = 6; // tope: en pantallas enormes no clonamos de más
  const DRAG_THRESHOLD = 40; // px para considerar que fue un arrastre y no un clic
  const ANIM_MS = 500; // debe coincidir con la transición del riel en CSS

  function stripLinks(node) {
    node.querySelectorAll('a').forEach(function (link) {
      const span = document.createElement('span');
      span.className = link.className;
      span.innerHTML = link.innerHTML;
      link.replaceWith(span);
    });
  }

  function initCarousel(root) {
    const view = root.querySelector('.svc-view') || root;
    const track = root.querySelector('[data-carousel-track]');
    if (!track) return;
    const originals = Array.prototype.slice.call(track.children);
    const total = originals.length;
    if (total < 2) return;

    const prevBtn = root.querySelector('[data-carousel-prev]');
    const nextBtn = root.querySelector('[data-carousel-next]');
    const currentLabel = root.querySelector('.svc-current');
    const reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    let index = 0;
    let busy = false;
    let rafId = 0;
    let dragStart = 0;
    let dragged = false;

    // 1) Cuántas tarjetas clonar por lado: depende de cuántas se ven a la vez.
    //    Sin esto, al caer en un clon del wrap se alcanzaba a ver el hueco al
    //    final del riel y el salto invisible se notaba como un pop.
    const cardWidth = originals[0].getBoundingClientRect().width || 1;
    const viewport = view.clientWidth || cardWidth * 2;
    const perSide = Math.min(
      MAX_CLONES_PER_SIDE,
      Math.max(2, Math.ceil(viewport / cardWidth) + 1)
    );

    // 2) Clones a cada lado. Son decorativos: sin enlace y ocultos al lector.
    for (let i = 0; i < perSide; i++) {
      const before = originals[(total - 1 - i + total) % total].cloneNode(true);
      before.classList.add('svc-card--clone');
      before.setAttribute('aria-hidden', 'true');
      stripLinks(before);
      track.insertBefore(before, track.firstChild);

      const after = originals[i % total].cloneNode(true);
      after.classList.add('svc-card--clone');
      after.setAttribute('aria-hidden', 'true');
      stripLinks(after);
      track.appendChild(after);
    }

    function paint(instant) {
      const cards = track.querySelectorAll('.svc-card');
      const first = cards[0];
      const target = cards[perSide + index];
      if (!first || !target) return;

      // Posicionamos con la posición REAL de cada tarjeta en el layout
      // (offsetLeft), no multiplicando una medida: así no arrastramos error
      // por el gap computado y el encaje es exacto en cualquier navegador.
      const delta = target.offsetLeft - first.offsetLeft;

      if (instant) {
        track.classList.add('is-instant');
      }
      track.style.transform = 'translate3d(' + -delta + 'px,0,0)';
      if (instant) {
        void track.offsetWidth; // fuerza el reflow: el salto se aplica sin transición
        track.classList.remove('is-instant');
      }
      if (currentLabel) {
        const shown = ((index % total) + total) % total;
        currentLabel.textContent = String(shown + 1).padStart(2, '0');
      }
    }

    function move(delta) {
      if (busy) return;
      busy = true;
      index += delta;
      paint(false);
      window.setTimeout(
        function () {
          // Si caímos en un clon, saltamos sin animación a la tarjeta real
          if (index < 0) {
            index = total - 1;
            paint(true);
          } else if (index >= total) {
            index = 0;
            paint(true);
          }
          busy = false;
        },
        reduce ? 0 : ANIM_MS
      );
    }

    if (prevBtn) {
      prevBtn.addEventListener('click', function () {
        move(-1);
      });
    }
    if (nextBtn) {
      nextBtn.addEventListener('click', function () {
        move(1);
      });
    }

    // Teclado: el carrusel es enfocable y responde a las flechas
    root.setAttribute('tabindex', '0');
    root.addEventListener('keydown', function (event) {
      if (event.key === 'ArrowRight') {
        move(1);
        event.preventDefault();
      } else if (event.key === 'ArrowLeft') {
        move(-1);
        event.preventDefault();
      }
    });

    // Arrastre (mouse y touch): un arrastre no debe además activar un enlace
    track.addEventListener('pointerdown', function (event) {
      dragStart = event.clientX;
      dragged = false;
    });
    track.addEventListener('pointermove', function (event) {
      if (dragStart && Math.abs(event.clientX - dragStart) > DRAG_THRESHOLD) {
        dragged = true;
      }
    });
    track.addEventListener('pointerup', function (event) {
      if (!dragStart) return;
      const dx = event.clientX - dragStart;
      dragStart = 0;
      if (Math.abs(dx) > DRAG_THRESHOLD) {
        move(dx < 0 ? 1 : -1);
      }
    });
    track.addEventListener('click', function (event) {
      if (dragged) {
        event.preventDefault();
        dragged = false;
      }
    });

    window.addEventListener('resize', function () {
      if (rafId) return;
      rafId = window.requestAnimationFrame(function () {
        rafId = 0;
        paint(true);
      });
    });

    window.addEventListener('load', function () {
      paint(true);
    });

    root.classList.add('is-carousel');
    paint(true);
  }

  function init() {
    document.querySelectorAll('[data-carousel]').forEach(initCarousel);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
