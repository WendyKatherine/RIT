/**
 * Popup de evento — se muestra una vez por sesión.
 *
 * Usa el elemento nativo <dialog>: foco atrapado, ESC y backdrop gratis.
 * Sin JS el <dialog> nace cerrado, así que no aparece y nada se rompe.
 */
(function () {
    'use strict';

    var KEY_PREFIX = 'rit:event-popup:';

    function boot() {
        var dialog = document.querySelector('[data-event-popup]');

        // Sin dialog o sin soporte nativo: no hay nada que hacer.
        if (!dialog || typeof dialog.showModal !== 'function') return;

        // La clave lleva el id del popup: si cambia el evento, se vuelve a mostrar.
        var key = KEY_PREFIX + (dialog.dataset.eventPopup || 'default');

        // Modo diseno (?popup=1): fuerza el popup y NO guarda nada, para
        // iterar estilos sin pelear con la marca de "visto".
        // ?popup=reset limpia la marca y lo muestra una vez.
        var mode = new URLSearchParams(window.location.search).get('popup');
        var forced = mode === '1';

        if (mode === 'reset') {
            try {
                window.localStorage.removeItem(key);
            } catch (e) {
                /* sin storage: nada que limpiar */
            }
        }

        var seen = false;
        try {
            seen = window.localStorage.getItem(key) === '1';
        } catch (e) {
            seen = false;
        }
        if (seen && !forced) return;

        document.body.classList.add('has-modal');
        dialog.showModal();

        // Dona ASCII: se monta al abrir (el canvas necesita tamaño real) y se
        // detiene al cerrar, para no gastar CPU con el popup oculto.
        var rings = null;

        function startRings() {
            var canvas = dialog.querySelector('[data-popup-rings]');
            if (!canvas || !window.ritStartAsciiRings) return;
            if (!rings) {
                rings = window.ritStartAsciiRings(canvas, {
                    centerX: 0.62,
                    centerY: 0.5,
                    scale: 1.25,
                    rings: 38,
                    dotSpacing: 6
                });
            }
            var reduce = window.matchMedia &&
                window.matchMedia('(prefers-reduced-motion: reduce)').matches;
            if (reduce) rings.redraw();
            else rings.start();
        }

        function stopRings() {
            if (rings) rings.stop();
        }

        startRings();

        function markSeen() {
            if (forced) return; // modo diseno: no persiste nada
            try {
                window.localStorage.setItem(key, '1');
            } catch (e) {
                /* sin storage: se mostrará de nuevo, es aceptable */
            }
        }

        function close() {
            markSeen();
            dialog.close();
        }

        var button = dialog.querySelector('[data-event-popup-close]');
        if (button) button.addEventListener('click', close);

        // Clic en el backdrop (fuera de la tarjeta) también cierra.
        dialog.addEventListener('click', function (event) {
            if (event.target === dialog) close();
        });

        // Cualquier cierre (✕, ESC, backdrop) marca el popup como visto.
        dialog.addEventListener('close', function () {
            markSeen();
            stopRings();
            document.body.classList.remove('has-modal');
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', boot);
    } else {
        boot();
    }
})();
