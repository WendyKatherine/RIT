# Inventario de color — base para el tema oscuro

> Generado sobre `config/static/css/*` el 2026-11-25. No incluye `tokens.css`.
> Uso: checklist de trabajo. No es una lista de reemplazos: cada línea exige clasificar el color.

## Resumen

| Hoja | Líneas con literal | Hex neutros | Sombras (se conservan) |
|---|---|---|---|
| base.css | 13 | 6 | 1 |
| components.css | 30 | 11 | 1 |
| pages.css | 41 | 12 | 0 |
| home.css | 35 | 5 | 0 |
| popup.css | 4 | 0 | 3 |
| fan-carousel.css | 8 | 3 | 0 |
| **Total** | **133** | **59** | **52** |

Por superficie: chrome 47 · home 35 · páginas 41 · fan 8.

## Las tres categorías

1. **Superficie** — `background: #fff`, `background: #eff3f9`. Cambia con el tema. Es la minoría.
2. **Texto sobre superficie oscura** — `color: #fff` dentro de hero, footer, tarjetas navy. **Se queda casi blanco en ambos temas.** Es la mayoría de los `#fff`.
3. **Marca y sombra** — `#e30613`, gradientes, `rgba(0,0,0,.5)`. Se conserva; la sombra solo cambia de color base.

## Trampas detectadas

- `pages.css:857` — `box-shadow: 0 0 0 4px #fff` es un anillo de foco sobre superficie, no texto: debe seguir al tema.
- `base.css:174` — `border: 1.5px solid rgba(255,255,255,.7)` sobre botón de marca: se queda.
- `components.css:431–432` — los estados `flash--success` / `flash--error` mezclan fondo con alfa y texto claro; en claro pueden quedar ilegibles. Revisar contraste en ambos temas.
- `home.css:203` — `rgba(0,27,58,.82)` como fondo de un chip: es superficie, no sombra.
- `components.css:574` — `rgba(0,27,58,.98)` del menú desplegable: es `--surface-2`, no overlay.
- `fan-carousel.css:170` — `background: #fff` en tarjeta central del carrusel: superficie.

## Criterio de cierre del inventario

- Toda línea de las categorías 1 y 3-que-cambia usa token semántico.
- Las líneas de categoría 2 se documentan como `--on-dark` y no se tocan a mano.
- Los 5 puntos de "trampas" tienen decisión escrita en el PR.
