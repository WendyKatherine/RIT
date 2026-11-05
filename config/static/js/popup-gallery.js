(function () {
    'use strict';

    const SLOT_SELECTOR = '[data-gallery-event]';
    const MAIN_SLOT_ID = '1';
    const ROTATION_INTERVAL_MS = 5000;
    const FADE_MS = 300; // keep in sync with the CSS transition

    function swapSlotImages(slotA, slotB) {
        const imageA = slotA.querySelector('img');
        const imageB = slotB.querySelector('img');
        if (!imageA || !imageB) return;

        slotA.appendChild(imageB);
        slotB.appendChild(imageA);
    }

    function createTimer(callback, intervalMs) {
        let timerId = null;

        return {
            start() {
                if (timerId === null) timerId = setInterval(callback, intervalMs);
            },
            stop() {
                clearInterval(timerId);
                timerId = null;
            },
            restart() {
                this.stop();
                this.start();
            },
        };
    }

    function initEventGallery(root, { triggerOn = 'click', autoplay = true } = {}) {
        if (!root || root.dataset.galleryReady) return;

        const mainSlot = root.querySelector(`[data-gallery-event="${MAIN_SLOT_ID}"]`);
        if (!mainSlot) return;

        const dialog = root.closest('dialog');
        let rotationCursor = 0;

        const getThumbSlots = () =>
            [...root.querySelectorAll(SLOT_SELECTOR)].filter(
                (slot) => slot !== mainSlot && slot.querySelector('img')
            );

        function swapWithFade(slot) {
            if (root.classList.contains('is-swapping')) return;

            root.classList.add('is-swapping');
            setTimeout(() => {
                swapSlotImages(mainSlot, slot);
                root.classList.remove('is-swapping');
            }, FADE_MS);
        }

        function rotate() {
            if (dialog && !dialog.open) return;

            const thumbs = getThumbSlots();
            if (!thumbs.length) return;

            swapWithFade(thumbs[rotationCursor % thumbs.length]);
            rotationCursor += 1;
        }

        const timer = createTimer(rotate, ROTATION_INTERVAL_MS);

        root.addEventListener(triggerOn, (event) => {
            const slot = event.target.closest(SLOT_SELECTOR);
            if (!slot || slot === mainSlot) return;

            swapWithFade(slot);
            timer.restart();
        });

        const prefersReducedMotion = window.matchMedia(
            '(prefers-reduced-motion: reduce)'
        ).matches;

        if (autoplay && !prefersReducedMotion) {
            root.addEventListener('mouseenter', () => timer.stop());
            root.addEventListener('mouseleave', () => timer.start());
            document.addEventListener('visibilitychange', () =>
                document.hidden ? timer.stop() : timer.start()
            );
            timer.start();
        }

        root.dataset.galleryReady = 'true';
    }

    document.addEventListener('DOMContentLoaded', () => {
        initEventGallery(document.querySelector('.event-popup-body'));
    });
})();