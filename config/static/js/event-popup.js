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

        var seen = false;
        try {
            seen = window.localStorage.getItem(key) === '1';
        } catch (e) {
            seen = false;
        }
        if (seen) return;

        document.body.classList.add('has-modal');
        dialog.showModal();

        function markSeen() {
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
            document.body.classList.remove('has-modal');
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', boot);
    } else {
        boot();
    }
})();
