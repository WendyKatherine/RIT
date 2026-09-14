/**
 * Abanico de tarjetas (fan carousel) — controlador, sin dependencias.
 *
 * Toma cada elemento [data-fan] con tarjetas .fan-card y las reparte en
 * abanico 3D: una al frente (tema oscuro) y el resto a los lados.
 *
 * Sin este script la sección se ve como la grilla plana de siempre: el 3D
 * solo se activa cuando JS agrega .is-fan (degradación segura).
 *
 * Interacción (estática: no gira sola):
 * - Clic en la mitad izquierda/derecha del abanico → retrocede / avanza una
 *   tarjeta, en loop infinito.
 * - Clic sobre la tarjeta del frente → sigue su enlace (.fan-card-link).
 * - Teclado: ← y → cuando el abanico tiene el foco.
 *
 * La geometría vive en el CSS (fan-carousel.css) y se deriva de --d, --ad y
 * --org; acá solo movemos los índices y marcamos la tarjeta central.
 */
(function () {
  'use strict';

  function initFan(root) {
    const cards = Array.prototype.slice.call(root.querySelectorAll('.fan-card'));
    const total = cards.length;
    if (total < 2) return;

    const center = Math.floor(total / 2);
    const previous = new Array(total).fill(null);
    let offset = 0;

    root.classList.add('is-fan');
    if (!root.hasAttribute('tabindex')) {
      root.setAttribute('tabindex', '0');
    }

    const render = function () {
      for (let index = 0; index < total; index++) {
        const card = cards[index];
        const slot = ((index - offset) % total + total) % total;
        const d = slot - center;
        const ad = Math.abs(d);
        const wrap = previous[index] !== null && Math.abs(slot - previous[index]) > 1;
        previous[index] = slot;

        // Cuando una tarjeta "salta" de un extremo al otro, no queremos verla
        // cruzar el abanico: se aplica sin transición y se restaura al siguiente
        // cuadro.
        if (wrap) {
          card.style.transition = 'none';
        }
        card.style.setProperty('--d', String(d));
        card.style.setProperty('--ad', String(ad));
        card.style.setProperty('--org', d < 0 ? 'right' : 'left');
        card.style.zIndex = String(10 - ad);
        card.classList.toggle('is-center', d === 0);
        if (wrap) {
          window.requestAnimationFrame(function () {
            card.style.transition = '';
          });
        }
      }
    };

    const move = function (step) {
      offset += step;
      render();
    };

    root.addEventListener('click', function (event) {
      const hit = event.target.closest('.fan-hit');
      if (!hit) return;
      move(hit.classList.contains('fan-hit--next') ? 1 : -1);
    });

    root.addEventListener('keydown', function (event) {
      if (event.key === 'ArrowRight') {
        move(1);
        event.preventDefault();
      } else if (event.key === 'ArrowLeft') {
        move(-1);
        event.preventDefault();
      }
    });

    render();
  }

  function init() {
    document.querySelectorAll('[data-fan]').forEach(initFan);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
