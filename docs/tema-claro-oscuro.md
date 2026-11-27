# Tema claro/oscuro — contrato de integración

> Acompaña a `ADR-0003` y `inventario-colores.md`.
> El CSS ya está. Falta cablear cookie, plantilla, botón y endpoint. Eso **no** es CSS.

## Lo que ya está en el repo

- `tokens.css`: capa semántica (13 claves) + bloques `[data-theme="dark"]` y `[data-theme="system"]`.
- `base.css`: superficies, texto, botones e iconos leen tokens. El tema claro conserva los valores originales.
- `components.css`: header, tarjetas, pills y footer mapeados; `.theme-form` y `.theme-toggle` estilizados; logo con `--logo-plate`.
- `pages.css`, `home.css`, `fan-carousel.css`, `popup.css`: tarjetas y fondos claros mapeados.

## Decisión de flujo

El tema se cambia con un **POST al servidor** que fija la cookie y redirige. Sin JavaScript. El sitio ya declara que funciona sin JS; el toggle no puede ser la excepción. La recarga es intencional: garantiza que el primer paint traiga el tema correcto.

Si más adelante se quiere cambio instantáneo, se agrega JS **como mejora**, nunca como requisito.

## Contrato

1. **Atributo:** `<html data-theme="light|dark|system">`.
2. **Cookie:** `theme`, mismo valor, `Max-Age` de un año, `SameSite=Lax`, `Path=/`, `HttpOnly`. No se lee desde JS, así que puede ser HttpOnly.
3. **Servidor:** lee la cookie, valida contra la lista permitida (`light`, `dark`, `system`) y, si no hay cookie o el valor no es válido, usa `light`. Se escribe en el HTML inicial.
4. **Sin JS de arranque:** prohibido aplicar el tema al final del body.
5. **Botón:** formulario POST que cicla `light → dark → system → light` y redirige a la página actual.
6. **"system":** no se resuelve en el servidor; el CSS ya lo resuelve con `prefers-color-scheme`. El servidor solo guarda la palabra.

## Markup esperado por el CSS

- Formulario `.theme-form` con `method="post"`, token CSRF y un campo oculto `next` con la ruta actual.
- Botón `button.theme-toggle` dentro del formulario, con `aria-label` que anuncie la **acción** ("Cambiar a tema oscuro"), no el estado.
- Dos SVG hijos: `.theme-toggle__icon--light` y `.theme-toggle__icon--dark`.
- El botón vive en el header, entre el CTA y el burger, fuera de `.site-nav` para que siga visible en móvil.
- Logo: `img` dentro de `.brand`. Mientras no exista la variante para oscuro, el plato blanco lo hace legible.

## Orden de implementación

1. `apps/common/theme.py`: constantes, lectura validada y ciclo de estados.
2. `config/context_processors.py`: exponer tema, siguiente tema y etiqueta.
3. `config/settings/base.py`: registrar el processor.
4. `config/templates/base.html`: atributo en la etiqueta `html`.
5. `apps/common/views.py`: vista POST que valida, fija cookie y redirige.
6. `config/urls.py`: ruta fuera de `i18n_patterns`.
7. `config/templates/partials/header.html`: formulario y botón.
8. `tests/`: casos de cookie, ciclo, CSRF, método y redirect abierto.

## Checklist de revisión (por página y por tema)

1. Primer paint sin flash: recargar en oscuro y mirar el primer frame.
2. Recorrer 8 páginas × 2 temas: home, servicios, casos, nosotros, contacto, políticas, blog/índice y 404.
3. Contraste medido, no a ojo: texto ≥ 4.5:1; bordes y foco ≥ 3:1.
4. Puntos frágiles: rojo `#e30613` sobre navy, texto muted al 55 % en partner-pill, flash success/error, borde de tarjeta en hover, hover del popup.
5. Navegación con teclado: el anillo de foco se ve en ambos temas.
6. Popup de evento y menú desplegable: abren legibles en ambos.
7. Cambiar el tema del SO con `system` activo: el sitio acompaña sin recargar.
8. Navegar entre páginas: el tema no parpadea ni se pierde.

## Límite de esta entrega

El mapeo se hizo por análisis estático, sin navegador. Puede haber regresiones visuales puntuales: se corrigen en revisión, no se aceptan como "se ve raro". Si una página no se revisó en oscuro, se registra como pendiente.
