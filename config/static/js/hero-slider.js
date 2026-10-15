/**
 * Slider del hero — autoplay configurable, pausa al interactuar, flechas
 * reales, teclado y fundido de los anillos ASCII fuera del primer slide.
 *
 * Configuración desde Wagtail (la setea el template):
 *   <section class="hero" data-hero-slider data-autoplay="10">   0 = sin autoplay
 *
 * SIN GSAP a propósito: esto corre al cargar la página, así que no queremos
 * cargar 40KB de librería por un temporizador y unos fundidos. GSAP sigue
 * reservado para las animaciones atadas al scroll (ver js/gsap-loader.js).
 *
 * Sin JS: el CSS muestra el primer slide (ver .hero:not(.is-slider)) y el
 * autoplay no existe. Nunca se rompe.
 */
(function () {
  'use strict';

  function boot() {
    const root = document.querySelector('[data-hero-slider]');
    if (!root) return;

    const slides = Array.prototype.slice.call(root.querySelectorAll('.hero-slide'));
    if (slides.length < 2) return;

    const canvas = root.querySelector('.hero-ascii-canvas');
    const bar = root.querySelector('[data-hero-progress]');
    const seconds = parseInt(root.dataset.autoplay || '10', 10);
    const reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    let index = 0;
    let rafId = 0;
    let startedAt = 0;
    let paused = false;

    // Le avisamos al CSS que el JS está al mando (cambia el fallback)
    root.classList.add('is-slider');

    function paint(next) {
      index = (next + slides.length) % slides.length;

      slides.forEach(function (slide, i) {
        slide.classList.toggle('is-active', i === index);
      });

      // Los anillos son la firma del slide 1: en el resto se apagan y dejan de dibujar
      if (canvas) {
        canvas.style.opacity = index === 0 ? '0.85' : '0';
      }
      if (window.ritHeroAscii) {
        if (index === 0) {
          window.ritHeroAscii.start();
        } else {
          window.ritHeroAscii.stop();
        }
      }

      if (bar) {
        bar.style.transform = 'scaleX(0)';
      }
      restartTimer();
    }

    function tick(now) {
      if (!seconds || paused) return;
      const progress = Math.min(1, (now - startedAt) / (seconds * 1000));
      if (bar) {
        bar.style.transform = 'scaleX(' + progress + ')';
      }
      if (progress >= 1) {
        paint(index + 1);
        return;
      }
      rafId = window.requestAnimationFrame(tick);
    }

    function stopTimer() {
      if (rafId) {
        window.cancelAnimationFrame(rafId);
        rafId = 0;
      }
    }

    function restartTimer() {
      stopTimer();
      if (!seconds || reduce || paused) return;
      startedAt = performance.now();
      rafId = window.requestAnimationFrame(tick);
    }

    function pause() {
      paused = true;
      stopTimer();
    }

    function resume() {
      if (!paused) return;
      paused = false;
      restartTimer();
    }

    // Controles: cada slide visible trae sus flechas (las ocultas no son tabulables)
    // Controles por delegación: cubre las flechas de todos los slides y
    // resiste a que el markup se re-renderice.
    root.addEventListener('click', function (event) {
      if (event.target.closest('[data-hero-next]')) {
        paint(index + 1);
        return;
      }
      if (event.target.closest('[data-hero-prev]')) {
        paint(index - 1);
      }
    });
    Array.prototype.forEach.call(root.querySelectorAll('[data-hero-next]'), function (btn) {
      btn.addEventListener('click', function () {
        paint(index + 1);
      });
    });

    // Teclado
    root.setAttribute('tabindex', '0');
    root.addEventListener('keydown', function (event) {
      if (event.key === 'ArrowRight') {
        paint(index + 1);
        event.preventDefault();
      } else if (event.key === 'ArrowLeft') {
        paint(index - 1);
        event.preventDefault();
      }
    });

    // Pausa al pasar el mouse o al enfocar con teclado
    root.addEventListener('mouseenter', pause);
    root.addEventListener('mouseleave', resume);
    root.addEventListener('focusin', pause);
    root.addEventListener('focusout', resume);

    // Pausa si la pestaña no está visible
    document.addEventListener('visibilitychange', function () {
      if (document.hidden) {
        pause();
      } else {
        resume();
      }
    });

    // Pausa cuando el hero sale de pantalla
    if ('IntersectionObserver' in window) {
      const observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            resume();
          } else {
            pause();
          }
        });
      });
      observer.observe(root);
    }

    paint(0);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
