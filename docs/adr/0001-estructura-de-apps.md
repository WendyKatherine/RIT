# ADR 0001 — Estructura de apps, templates y chrome global

- **Estado:** Propuesto (pendiente de revisión con quien estructuró `home`)
- **Fecha:** 2026-11-05
- **Decisores:** Wendy (backend) + revisión del equipo

## Contexto

El sitio público vive hoy en una sola app:

- `apps/home/models.py` define **8 modelos de página** (`HomePage`, `NosotrosPage`, `ContactoPage`, `SolucionesIndexPage`, `SolucionPage`, `SeccionIndexPage`, `InteriorPage`, `PoliticaPage`) y un snippet global, `EventPopup`.
- Las migraciones de seed crean **27 páginas** con esos 8 modelos.
- `apps/home/blocks.py` tiene **521 líneas** y **44 clases de bloque**: 29 de nivel superior y 15 anidados. Hay 28 claves de StreamField únicas porque `stats` se reutiliza para `StatsBlock` (Home) e `InteriorStatsBlock` (Nosotros).
- Los 8 templates de página viven en `apps/home/templates/home/`; los bloques, en `home/blocks/` (30 archivos: 29 templates + el partial `_svc_card.html`).
- `SeccionIndexPage` sirve `/productos/`, `/servicios/`, `/consultoria/` y también `/politicas/`; su docstring solo menciona las tres primeras.
- El chrome global (header y footer) está en `config/templates/partials/`. `EventPopup` vive en `apps/home`, se expone con `config.context_processors.event_popup`, se renderiza en `config/templates/base.html` y se comporta con `config/static/js/event-popup.js`.
- El front **no es "cero JS"**: `config/static/js/` tiene 11 archivos; `base.html` carga 3 (`hero-ascii-rings`, `event-popup`, `popup-gallery`) y `home_page.html` carga 6 más (`gsap-loader`, `hero-slider`, `fan-carousel`, `carousel`, `cases-shelf`, `title-reveal`). GSAP está vendorizado en `config/static/vendor/gsap/` y solo lo consumen `cases-shelf.js` y `title-reveal.js`.

## Decisión

1. **Una sola app `home` para los 8 tipos de página**, mientras compartan un equipo editorial, un árbol de páginas, un catálogo de bloques y un deploy. Una app de Django no es una sección de URL: la jerarquía la define Wagtail, no `INSTALLED_APPS`.
2. **Los templates se organizan por tipo de página dentro de la app**, no por dominio de URL: `apps/home/templates/home/<page_type>.html` y `home/blocks/<block>.html`. Si una sección se separa en otra app, su template se mueve con ella.
3. **El chrome global vive fuera de la app de páginas**: header y footer en `config/templates/partials/`. `EventPopup` se queda en `home` por ahora porque es un snippet, no una página, y moverlo exige migración de contenido; su lugar objetivo es `apps/common` en la fase 2.
4. **Regla de JS:** vanilla permitido cuando el CSS no alcanza; sin frameworks de front; GSAP solo para animaciones atadas al scroll, cargado una vez por `gsap-loader.js`; todo script debe degradar sin JS. Esta regla reemplaza la afirmación "cero JavaScript" del README anterior.

## Alternativas descartadas

| Alternativa | Por qué se descarta |
|---|---|
| Una app por tipo de página (8 apps) | Ocho historias de migraciones, imports cruzados para bloques compartidos y más ceremonia. El árbol de Wagtail es global, así que la app no aísla contenido. Se revisa si una sección pasa a tener equipo y cadencia propios. |
| Implementación paralela de páginas V2 junto a V1 | Duplica modelos, templates y contenido; no hay requisito de A/B ni de corte gradual. Reemplazar en el mismo árbol es suficiente. |
| Templates de página en `templates/pages/<dominio>/` a nivel de proyecto | Rompe el descubrimiento por app y obliga a declarar rutas completas en cada `Page`. No aporta mientras una sola app sea dueña de las páginas. |

## Consecuencias

**A favor**

- Un solo lugar para encontrar tipos de página, bloques y templates.
- Migraciones lineales y sin dependencias cruzadas entre apps.
- El árbol del editor y la estructura del código cuentan la misma historia.

**Deuda aceptada**

| Deuda | Por qué se acepta | Cuándo se paga |
|---|---|---|
| `blocks.py` monolítico (521 líneas, 44 clases) | La fase 0 no toca código; el archivo está tipado y funciona | Fase 1: partir por dominio (home, compartido, contacto, soluciones) |
| `EventPopup` en `home` | Es un snippet global, no una página; moverlo requiere migración | Fase 2: mover a `common` |
| `welcome_page.html` huérfano | No existe `WelcomePage` y ningún template lo referencia | Fase 0: borrar (este PR) |
| `welcome_page.css` huérfano | Ningún template lo carga | Limpieza de estáticos (fase 2) |
| Nav hardcodeado en `config/context_processors.py` | Transición hasta el menú desde el árbol de Wagtail | Fase de menú dinámico |
| Formulario de contacto es maqueta | Falta definir backend, validación y antispam | Fase de formularios |

**Costo de revertir:** medio-alto. Separar apps después implica mover modelos, migraciones y templates conservando `content_type` y el árbol de páginas; requiere migración de datos y redirects.

## Verificación

- `apps/home/models.py`: 8 subclases de `Page` + `EventPopup`.
- `apps/home/blocks.py`: 44 clases; 521 líneas.
- `apps/home/templates/home/`: 8 templates de página + `blocks/` con 30 archivos.
- `config/static/js/`: 11 archivos; 9 referenciados desde templates.
- `config/context_processors.py`: `event_popup`; `config/templates/base.html`: `{% include "partials/event_popup.html" %}`.
