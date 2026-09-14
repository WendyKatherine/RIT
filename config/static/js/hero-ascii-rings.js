/**
 * Anillos ASCII del hero — canvas 2D, sin dependencias.
 *
 * Adaptado de `ascii-rings.js` (propuesta de diseño): anillos concéntricos de
 * puntos con desplazamiento orgánico por ondas; los anillos más externos
 * llevan acentos rojos. Vocabulario mínimo — un solo glifo (".") — que encaja
 * con el lenguaje gráfico de la marca.
 *
 * Diferencias con el original:
 * - Script plano (sin imports): encuentra el canvas por selector.
 * - Respeta `prefers-reduced-motion`: dibuja un cuadro y no anima.
 * - Pausa el dibujo cuando el hero sale de pantalla (ahorra CPU y batería).
 * - El acento usa el rojo de marca.
 */
(function () {
  'use strict';

  const TAU = Math.PI * 2;

  const DEFAULTS = {
    glyph: '.',
    accentGlyph: '.',
    font: '500 9px "JetBrains Mono", monospace',
    rings: 60, // anillos concéntricos
    innerRadius: 10, // radio en px del primer anillo
    dotSpacing: 5, // distancia de arco entre puntos: menos = más denso
    radiusScale: 0.46, // radio exterior como fracción del lado menor
    scale: 0.7, // multiplicador extra del radio (crop fuera del marco con > 1)
    centerX: 0.5, // 0–1 a lo ancho del canvas
    centerY: 0.5,
    fps: 15, // redibujo: bajo = cadencia "stepped" de terminal
    spin: 0.05, // giro base; los anillos alternos contra-rotan
    waves: [
      // desplazamiento orgánico: amplitud px, frecuencia angular, frecuencia de anillo, velocidad
      { amp: 10, freq: 3, ring: 0.24, speed: 0.55 },
      { amp: 6, freq: 5, ring: -0.15, speed: -0.38 },
      { amp: 3.5, freq: 8, ring: 0.08, speed: 0.9 }
    ],
    coreColor: '74,155,209', // anillos internos (acero)
    edgeColor: '232,241,248', // anillos externos (hielo)
    edgeStart: 0.72, // desde dónde cambia de color core → edge
    accentColor: '227,6,19', // rojo de marca
    accentRings: 5, // los N anillos más externos llevan acento
    accentEvery: 37, // cada N puntos de esos anillos
    minAlpha: 0.3,
    maxAlpha: 0.92
  };

  // Configuración de uso en el hero: centro desplazado a la derecha y escala
  // > 1 para que los anillos se salgan del marco.
  const HERO_OPTIONS = { centerX: 0.72, scale: 1.1 };

  function startAsciiRings(canvas, options) {
    if (!canvas) {
      return { start: function () {}, stop: function () {}, redraw: function () {} };
    }
    const o = Object.assign({}, DEFAULTS, options || {});
    const waves = o.waves;
    const ctx = canvas.getContext('2d');
    let W = 0;
    let H = 0;
    let timer = 0;

    const resize = function () {
      const rect = canvas.getBoundingClientRect();
      const dpr = Math.min(2, window.devicePixelRatio || 1);
      W = rect.width;
      H = rect.height;
      canvas.width = Math.max(1, W * dpr);
      canvas.height = Math.max(1, H * dpr);
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    };

    const t0 = performance.now();

    const draw = function () {
      const t = (performance.now() - t0) / 1000;
      const cx = W * o.centerX;
      const cy = H * o.centerY;
      const R = Math.min(W, H) * o.radiusScale * o.scale;
      ctx.clearRect(0, 0, W, H);
      ctx.font = o.font;
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';

      for (let i = 1; i <= o.rings; i++) {
        const k = i / o.rings; // 0 en el núcleo → 1 en el borde
        const rad = o.innerRadius + k * R;
        const count = Math.max(6, Math.round((TAU * rad) / o.dotSpacing));
        const spin = t * (i % 2 ? o.spin : -o.spin * 0.7) + i * 0.05;
        const isAccentRing = i > o.rings - o.accentRings;

        for (let j = 0; j < count; j++) {
          const a = (j / count) * TAU + spin;
          let d = 0;
          for (let wi = 0; wi < waves.length; wi++) {
            const wv = waves[wi];
            d += wv.amp * Math.sin(wv.freq * a + i * wv.ring + t * wv.speed);
          }
          const rr = rad + d * (0.25 + k * 0.85); // los anillos externos deforman más
          const x = cx + rr * Math.cos(a);
          const y = cy + rr * Math.sin(a);
          if (x < -8 || x > W + 8 || y < -8 || y > H + 8) continue;

          // la luminosidad sigue la onda principal: las crestas leen como filamentos
          const lead = waves[0];
          const lum =
            o.minAlpha +
            (o.maxAlpha - o.minAlpha) *
              (Math.sin(lead.freq * a + i * lead.ring + t * lead.speed) * 0.5 + 0.5);
          const accent = isAccentRing && j % o.accentEvery === 0;
          ctx.fillStyle = accent
            ? 'rgba(' + o.accentColor + ',.95)'
            : 'rgba(' +
              (k > o.edgeStart ? o.edgeColor : o.coreColor) +
              ',' +
              (lum * (0.45 + k * 0.55)).toFixed(3) +
              ')';
          ctx.fillText(accent ? o.accentGlyph : o.glyph, x, y);
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
      redraw: draw,
      stop: function () {
        stop();
        window.removeEventListener('resize', onResize);
      }
    };
  }

  function init() {
    const canvas = document.querySelector('.hero-ascii-canvas');
    if (!canvas) return;

    const art = startAsciiRings(canvas, HERO_OPTIONS);
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
