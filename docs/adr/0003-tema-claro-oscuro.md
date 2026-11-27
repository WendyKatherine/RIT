# ADR-0003 — Tema claro/oscuro con capa semántica

- **Estado:** aceptado (2026-11-25)
- **Decisores:** Wendy (implementación), Atlas (revisión)
- **Contexto técnico verificado en:** `config/static/css/*`, `config/templates/base.html`

## Contexto

El sitio necesita un tema claro/oscuro. Hoy `tokens.css` contiene **primitivas de marca** (`--red`, `--navy-800`, `--cloud`, `--white`, `--line`, `--gray`), no claves de tema. No existe capa semántica ni hook de tema en `base.html`.

Medición del repo:

- 362 usos de `var()` sobre 39 tokens en 8 hojas.
- 188 literales de color fuera de `tokens.css`: 61 hex + 127 `rgb()/rgba()`.
- De esos, **52 son sombras/overlays** con alfa bajo (se conservan) y **133 líneas** contienen un literal que exige una decisión.
- Los 133 se reparten: chrome (base 13 + components 30 + popup 4) = **47**, home **35**, páginas **41**, fan-carousel **8**.
- El logo existe en una sola variante (`logo-rit-color.png`).

## Decisión

1. **Toggle de tres estados** (sistema / claro / oscuro), persistido en cookie. El default es **claro**.
2. El tema se resuelve en el **servidor** (cookie) y se escribe como `data-theme` en `<html>` en el HTML inicial. **No** se aplica con JS al final del body.
3. Se introduce **una capa semántica** en `tokens.css`. Los overrides de oscuro viven en `[data-theme="dark"]`. Prohibido mantener dos hojas paralelas o duplicar reglas por tema.
4. `color-scheme` se declara para que scrollbar y controles nativos acompañen.
5. Los colores de marca y sus gradientes **no** cambian con el tema.

## Contrato de tokens semánticos

| Token | Propósito | Claro | Oscuro |
|---|---|---|---|
| `--bg` | Fondo de página | blanco | navy profundo |
| `--bg-alt` | Sección alterna | cloud | navy medio |
| `--surface` | Tarjeta / caja | blanco | navy elevado |
| `--surface-2` | Menú, popup, modal | blanco | navy más elevado |
| `--fg` | Texto primario | navy-900 | casi blanco |
| `--fg-muted` | Texto secundario | gray | gris claro |
| `--border` | Línea fina | line | blanco al 12–16 % |
| `--on-dark` | Texto sobre superficie de marca/oscura | casi blanco | casi blanco |
| `--on-dark-muted` | Texto secundario sobre oscuro | blanco al 70–80 % | igual |
| `--shadow` | Color base de sombra | navy con alfa | negro con más alfa |
| `--focus` | Anillo de foco | azul | azul claro |
| `--logo-plate` | Fondo detrás del logo en oscuro | transparente | blanco o chip claro |

Reglas:

- `#fff` es **ambiguo**: puede ser superficie o texto sobre oscuro. Se clasifica por contexto, nunca con reemplazo global.
- Las sombras conservan su geometría; cambia solo el color base vía `--shadow`.
- Gradientes de hero y overlays se mantienen: ya son oscuros por diseño.
- Código nuevo no usa literales de color; usa el token semántico.
- Contraste objetivo: texto ≥ 4.5:1, controles y bordes de estado ≥ 3:1, en ambos temas.

## Consecuencias

**Positivas**

- Un solo lugar define el tema; los bloques nuevos heredan ambos modos.
- Sin FOUC: el primer paint ya trae el tema correcto.
- El cambio de logo futuro es un token, no una cirugía de CSS.

**Negativas**

- Hay que tocar 133 líneas repartidas en 6 hojas; el riesgo de regresión visual es real.
- El color de marca `#e30613` sobre navy profundo es el punto frágil de contraste: exige medición, no criterio visual.
- Mientras no exista variante del logo, el color logo sobre fondo oscuro necesita un plato claro.

**Costo de reversa:** bajo. Quitar el toggle y dejar solo `prefers-color-scheme` es eliminar la cookie y el atributo; la capa semántica se queda y sigue siendo útil.

## Alternativas rechazadas

- **Solo `prefers-color-scheme`:** no permite forzar; el usuario que quiere oscuro con SO claro no puede.
- **Dos hojas de estilo:** duplica mantenimiento y garantiza divergencia.
- **Filtro CSS de inversión:** rompe imágenes, marca y contraste.
- **Aplicar el tema con JS al cargar:** produce flash blanco en oscuro.
