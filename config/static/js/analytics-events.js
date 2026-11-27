/* Eventos de analitica sin tocar las plantillas: clics en contacto.
   Empuja a dataLayer (GTM) y, si existe, a gtag (GA4 directo). */
(function () {
  "use strict";

  function send(name, params) {
    var payload = Object.assign({ event: name }, params || {});
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push(payload);
    if (typeof window.gtag === "function") {
      window.gtag("event", name, params || {});
    }
  }

  document.addEventListener(
    "click",
    function (e) {
      var a = e.target && e.target.closest ? e.target.closest("a") : null;
      if (!a) return;
      var href = a.getAttribute("href") || "";
      if (href.indexOf("mailto:") === 0) {
        send("click_email", { link_url: href });
      } else if (/wa\.me|whatsapp/i.test(href)) {
        send("click_whatsapp", { link_url: href });
      } else if (href.indexOf("tel:") === 0) {
        send("click_phone", { link_url: href });
      }
    },
    true
  );
})();
