/**
 * Cordilleras ASCII del hero — canvas 2D, sin dependencias.
 *
 * Adaptado de `ascii-landscape.js` del mockup V1 (diseño de referencia):
 * tres cordilleras dibujadas con glifos monoespaciados, dither p² para que se
 * disuelvan hacia el pie, cresta con "=", acento rojo cada N columnas en la
 * cordillera frontal, y grano de estrellas sobre el horizonte.
 *
 * Diferencias con el original:
 * - Script plano (sin React ni imports): encuentra el canvas por selector.
 * - Respeta `prefers-reduced-motion`: dibuja un cuadro y no anima.
 * - Pausa el dibujo cuando el hero sale de pantalla (ahorra CPU y batería).
 */
(function () {
  'use strict';

  const DEFAULTS = {
    charW: 9, // ancho de celda del glifo (px)
    charH: 12, // alto de celda del glifo (px)
    font: '11px "JetBrains Mono", ui-monospace, monospace',
    ramp: ' .·:-=+*', // rampa de densidad, dispersa → densa
    ridgeChar: '=', // glifo de la cresta
    fps: 11, // redibujo: bajo = sensación "stepped" de terminal
    stars: true, // grano parpadeante sobre el horizonte
    starColor: 'rgba(160,196,226,.18)',
    accentColor: 'rgba(227,6,19,.9)', // rojo de marca
    accentEvery: 23, // cada N columnas de la cordillera frontal lleva acento
    layers: [
      // lejos → cerca
      { amp: 0.1, base: 0.46, f: 0.02, sp: 0.07, rgb: '46,128,186', a: 0.6, span: 0.22 },
      { amp: 0.14, base: 0.6, f: 0.014, sp: 0.13, rgb: '96,172,220', a: 0.72, span: 0.29 },
      { amp: 0.18, base: 0.76, f: 0.01, sp: 0.22, rgb: '221,236,248', a: 0.85, span: 0.36 }
    ]
  };

  const hash = function (a, b) {
    const n = Math.sin(a * 127.1 + b * 311.7) * 43758.5453;
    return n - Math.floor(n);
  };

  // Silueta: tres senos sumados para que las crestas no se repitan visiblemente.
  const ridgeAt = function (layer, x, t) {
    return (
      layer.base -
      layer.amp *
        (0.55 * Math.sin(x * layer.f + t * layer.sp) +
          0.3 * Math.sin(x * layer.f * 2.3 + t * layer.sp * 1.6) +
          0.15 * Math.sin(x * layer.f * 4.7 - t * layer.sp * 0.9))
    );
  };

  function startAsciiLandscape(canvas, options) {
    if (!canvas) {
      return { start: function () {}, stop: function () {} };
    }
    const o = Object.assign({}, DEFAULTS, options || {});
    const layers = o.layers;
    const ctx = canvas.getContext('2d');
    const ramp = o.ramp;
    let W = 0;
    let H = 0;
    let cols = 0;
    let rows = 0;
    let timer = 0;

    const resize = function () {
      const rect = canvas.getBoundingClientRect();
      const dpr = Math.min(2, window.devicePixelRatio || 1);
      W = rect.width;
      H = rect.height;
      canvas.width = Math.max(1, W * dpr);
      canvas.height = Math.max(1, H * dpr);
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      cols = Math.ceil(W / o.charW) + 1;
      rows = Math.ceil(H / o.charH) + 1;
    };

    const t0 = performance.now();

    const draw = function () {
      const t = (performance.now() - t0) / 1000;
      ctx.clearRect(0, 0, W, H);
      ctx.font = o.font;
      ctx.textBaseline = 'top';

      if (o.stars) {
        ctx.fillStyle = o.starColor;
        for (let c = 0; c < cols; c += 2) {
          for (let r = 0; r < rows * 0.55; r += 2) {
            const n = hash(c, r);
            if (n > 0.985 && Math.sin(t * 1.4 + n * 40) > 0.2) {
              ctx.fillText('.', c * o.charW, r * o.charH);
            }
          }
        }
      }

      for (let li = 0; li < layers.length; li++) {
        const layer = layers[li];
        const span = rows * (layer.span != null ? layer.span : 0.22 + li * 0.07);
        const front = li === layers.length - 1;
        for (let c = 0; c < cols; c++) {
          const rr = Math.round(ridgeAt(layer, c * o.charW, t) * rows);
          for (let r = Math.max(0, rr); r < rows; r++) {
            const d = r - rr; // filas bajo la cresta
            const p = 1 - d / span; // 1 en la cresta → 0 en el pie
            if (p <= 0) break;
            if (hash(c * 3.1 + li * 17, r * 1.7) > p * p) continue; // dither
            const ch =
              d === 0
                ? o.ridgeChar
                : ramp[Math.max(1, Math.min(ramp.length - 1, Math.round(p * (ramp.length - 1))))];
            const accent = front && d === 0 && o.accentEvery && c % o.accentEvery === 0;
            ctx.fillStyle = accent
              ? o.accentColor
              : 'rgba(' + layer.rgb + ',' + (layer.a * (d === 0 ? 1 : 0.55 + p * 0.45)).toFixed(3) + ')';
            ctx.fillText(ch, c * o.charW, r * o.charH);
          }
        }
      }
    };

    const start = function () {
      if (timer) return;
      resize();
      draw();
      timer = window.setInterval(draw, Math.round(1000 / o.fps));
    };

    const stop = function () {
      if (timer) {
        window.clearInterval(timer);
        timer = 0;
      }
    };

    const onResize = function () {
      resize();
      draw();
    };
    window.addEventListener('resize', onResize);

    return {
      start: start,
      stop: function () {
        stop();
        window.removeEventListener('resize', onResize);
      },
      redraw: draw
    };
  }

  function init() {
    const canvas = document.querySelector('.hero-ascii-canvas');
    if (!canvas) return;

    const art = startAsciiLandscape(canvas);
    const reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    if (reduce) {
      art.redraw(); // un solo cuadro, sin animación
      return;
    }

    art.start();

    // Fuera de pantalla no se dibuja: el hero no se ve, no hace falta gastar CPU.
    if ('IntersectionObserver' in window) {
      const observer = new IntersectionObserver(
        function (entries) {
          entries.forEach(function (entry) {
            if (entry.isIntersecting) art.start();
            else art.stop();
          });
        },
        { threshold: 0 }
      );
      observer.observe(canvas);
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
