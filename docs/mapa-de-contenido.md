# Mapa de contenido — RIT Website

> Inventario leído del repo el **2026-11-05**. No mueve modelos, migraciones, panels, CSS ni JS: es el insumo de la fase 1.
>
> Fuentes: `apps/home/models.py`, `apps/home/blocks.py`, `apps/home/templates/home/` y las migraciones `0002`–`0041` de `apps/home/migrations/`.

## 1. Tipos de página

Hay **8 modelos de página** y **27 instancias seed** en el árbol actual. Las URLs llevan prefijo de idioma (`/es/` o `/en/`); aquí se muestra el caso español.

| # | Modelo | Template | URL aproximada | Padre en el árbol | Instancias |
|---|---|---|---|---|---|
| 1 | `HomePage` | `home/home_page.html` | `/es/` | raíz del sitio | 1 |
| 2 | `NosotrosPage` | `home/nosotros_page.html` | `/es/nosotros/` | `HomePage` | 1 |
| 3 | `ContactoPage` | `home/contacto_page.html` | `/es/contacto/` | `HomePage` | 1 |
| 4 | `SolucionesIndexPage` | `home/soluciones_index.html` | `/es/soluciones/` | `HomePage` | 1 |
| 5 | `SolucionPage` | `home/solucion_page.html` | `/es/soluciones/<slug>/` | `SolucionesIndexPage` | 5 |
| 6 | `SeccionIndexPage` | `home/seccion_index.html` | `/es/<seccion>/` | `HomePage` | 4 |
| 7 | `InteriorPage` | `home/interior_page.html` | `/es/<seccion>/<slug>/` | `SeccionIndexPage` | 11 |
| 8 | `PoliticaPage` | `home/politica_page.html` | `/es/politicas/<slug>/` | `SeccionIndexPage` (políticas) | 3 |

`SeccionIndexPage` se usa para cuatro índices: `/productos/`, `/servicios/`, `/consultoria/` y `/politicas/`. Su docstring solo nombra los tres primeros; la realidad del árbol incluye el cuarto.

## 2. Árbol actual

```text
HomePage  /es/
├── NosotrosPage                    /es/nosotros/
├── ContactoPage                    /es/contacto/
├── SolucionesIndexPage             /es/soluciones/
│   ├── SolucionPage                /es/soluciones/multicloud-infraestructura/
│   ├── SolucionPage                /es/soluciones/ciberseguridad/
│   ├── SolucionPage                /es/soluciones/comunicaciones-avanzadas/
│   ├── SolucionPage                /es/soluciones/espacios-de-trabajo/
│   └── SolucionPage                /es/soluciones/digitalizacion-procesos/
├── SeccionIndexPage                /es/productos/
│   ├── InteriorPage                /es/productos/centros-de-datos/
│   ├── InteriorPage                /es/productos/dell-apex/
│   └── InteriorPage                /es/productos/usuario-final/
├── SeccionIndexPage                /es/servicios/
│   ├── InteriorPage                /es/servicios/centro-de-servicios/
│   ├── InteriorPage                /es/servicios/instalacion/
│   ├── InteriorPage                /es/servicios/monitoreo-gestion/
│   └── InteriorPage                /es/servicios/postventa/
├── SeccionIndexPage                /es/consultoria/
│   ├── InteriorPage                /es/consultoria/arquitectura-integracion/
│   ├── InteriorPage                /es/consultoria/continuidad-negocio/
│   ├── InteriorPage                /es/consultoria/migraciones-sap/
│   └── InteriorPage                /es/consultoria/plan-estrategico/
└── SeccionIndexPage                /es/politicas/
    ├── PoliticaPage                /es/politicas/codigo-etica/
    ├── PoliticaPage                /es/politicas/politica-sig/
    └── PoliticaPage                /es/politicas/tratamiento-datos/
```

## 3. Bloques

`blocks.py` tiene **44 clases**: 29 de nivel superior y 15 anidados. La columna **¿Se usa?** se leyó de las declaraciones `StreamField` de los modelos y del contenido de las migraciones de seed; no es una suposición.

### 3.1 Home (15)

| Clave | Clase | Nivel | ¿Se usa? |
|---|---|---|---|
| `hero` | `HeroBlock` | superior | Sí — `HomePage`, seed `0004` |
| ↳ slide | `HeroSlideBlock` | anidado | Sí — dentro de `hero` |
| `marquee` | `MarqueeBlock` | superior | Sí — `HomePage`, seed `0004` |
| ↳ item | `BrandItemBlock` | anidado | Sí — `marquee` y `partners` |
| `nosotros` | `NosotrosBlock` | superior | Sí — `HomePage`, seed `0004` |
| ↳ card | `ValueCardBlock` | anidado | Sí — dentro de `nosotros` |
| `services` | `ServicesBlock` | superior | Sí — `HomePage`, seed `0004` |
| ↳ card | `ServiceCardBlock` | anidado | Sí — dentro de `services` |
| `partners` | `PartnersBlock` | superior | Sí — `HomePage`, seed `0004` |
| `stats` | `StatsBlock` | superior | Sí — `HomePage`, seed `0004` |
| ↳ stat | `StatBlock` | anidado | Sí — `stats` e `interior_stats` |
| `cases` | `CasesBlock` | superior | Sí — `HomePage`, seed `0004` |
| ↳ case | `CaseBlock` | anidado | Sí — dentro de `cases` |
| `contact` | `ContactBlock` | superior | Sí — `HomePage`, seed `0004` |
| ↳ row | `ContactRowBlock` | anidado | Sí — dentro de `contact` |

### 3.2 Contenido compartido e interiores (24)

| Clave | Clase | Nivel | ¿Se usa? |
|---|---|---|---|
| `page_hero` | `PageHeroBlock` | superior | Sí — 6 modelos de página |
| `story` | `StoryBlock` | superior | Sí — Nosotros, Solución, Interior |
| `cta` | `CTABandBlock` | superior | Sí — 6 modelos de página |
| `cards` | `CardsBlock` | superior | Sí — Solución, Interior |
| ↳ card | `IconCardBlock` | anidado | Sí — dentro de `cards` |
| `checklist` | `ChecklistBlock` | superior | Sí — Solución, Interior |
| `accordion` | `AccordionBlock` | superior | Sí — Solución, Interior |
| ↳ item | `AccordionItemBlock` | anidado | Sí — dentro de `accordion` |
| `highlight` | `HighlightBlock` | superior | Sí — Solución, Interior |
| `badges` | `BadgesBlock` | superior | Sí — Solución, Interior |
| `allies` | `AlliesBlock` | superior | Sí — Solución, Interior |
| `timeline` | `TimelineBlock` | superior | Sí — Solución, Interior |
| ↳ step | `TimelineStepBlock` | anidado | Sí — dentro de `timeline` |
| `split_bullets` | `SplitBulletsBlock` | superior | Sí — Solución, Interior |
| ↳ item | `SplitItemBlock` | anidado | Sí — dentro de `split_bullets` |
| `quote` | `QuoteBlock` | superior | Sí — Solución, Interior |
| `tabs` | `TabsBlock` | superior | Sí — `InteriorPage` (Productos) |
| ↳ tab | `TabItemBlock` | anidado | Sí — dentro de `tabs` |
| `sectors` | `SectorsBlock` | superior | Sí — `NosotrosPage` |
| ↳ card | `SectorCardBlock` | anidado | Sí — dentro de `sectors` |
| `mission_vision` | `MissionVisionBlock` | superior | Sí — `NosotrosPage` |
| `values` | `ValuesBlock` | superior | Sí — `NosotrosPage` |
| ↳ item | `ValueItemBlock` | anidado | Sí — dentro de `values` |
| `stats` | `InteriorStatsBlock` | superior | Sí — `NosotrosPage` (misma clave que `StatsBlock`) |

### 3.3 Contacto (4)

| Clave | Clase | Nivel | ¿Se usa? |
|---|---|---|---|
| `contact_info` | `ContactInfoBlock` | superior | Sí — `ContactoPage`, seed `0010` |
| ↳ card | `ContactCardBlock` | anidado | Sí — dentro de `contact_info` |
| `contact_form` | `ContactFormBlock` | superior | Sí — `ContactoPage`; es maqueta, sin backend |
| `map` | `MapBlock` | superior | Sí — `ContactoPage`, iframe de Google Maps |

### 3.4 Soluciones (1)

| Clave | Clase | Nivel | ¿Se usa? |
|---|---|---|---|
| `index_listing` | `IndexListingBlock` | superior | Sí — `SolucionesIndexPage`; seed insertado por `0040` |

**Bloques muertos:** ninguno de los 44 está sin declarar o sin seed. El único artefacto huérfano de esta fase es `home/welcome_page.html`.

## 4. Observaciones para la fase 1

- **Corte propuesto por dominio:** home (15), compartido/interiores (24), contacto (4), soluciones (1). Total: 44.
- **Claves compartidas:** `stats` se usa para dos clases distintas (`StatsBlock` en Home, `InteriorStatsBlock` en Nosotros). Al partir el archivo hay que conservar ambos alias; si se renombra una, se rompe el contenido guardado.
- **Bloques compartidos:** `BrandItemBlock` (marquee, partners) y `StatBlock` (stats, interior_stats). Revisar antes de mover.
- **Artefactos sin referencias:** `home/welcome_page.html`, `apps/home/static/css/welcome_page.css`, `config/static/css/config.css` (vacío), `config/static/js/config.js` (vacío) y `config/static/js/hero-ascii.js` (no cargado; `base.html` usa `hero-ascii-rings.js`).
- **Formulario de contacto:** el bloque renderiza campos, pero el botón es `type="button"` y no tiene `action` ni handler. El footer apunta a `/newsletter`, ruta que no existe en `config/urls.py`.
