# Plan de cierre — RIT Website

> Revisión **2** · 2026-11-25. Cambia el orden: el formulario queda bloqueado por el cliente y pasa a Fase 3; el tema claro/oscuro sube a Fase 1.
> Base verificada en el repo: TECH-DEBT.md (rev. 2026-11-05), README, `config/urls.py`, `config/static/css/*`, `config/templates/base.html`.

## 1. Qué está bloqueado y qué no

| Trabajo | Depende de | Estado |
|---|---|---|
| Formulario (G1) | Cliente: campos + proveedor + casilla | **Bloqueado** |
| Newsletter (404 vivo) | Nadie | **Desbloqueado** · decisión de 15 min |
| Tema claro/oscuro | Nadie | **Desbloqueado** |
| Prod segura (D-02, D-03, media, restore) | Nadie | **Desbloqueado** |
| GA4 + Search Console | Cliente: cuenta/propiedad | Parcial |
| Blog / EN | Cliente: alcance | Fuera de la entrega |

Regla: no se construye el formulario a ciegas. La parte que no depende de las respuestas (persistencia, CSRF, honeypot, tests) se puede adelantar, pero el costo de esperar es bajo y el de adivinar los campos es una migración. Se espera al cliente; el newsletter no.

## 2. Gates de entrega (sin cambios)

| Gate | Se cumple cuando |
|---|---|
| **G1 — Leads** | Un envío real crea registro y llega a una persona de RIT. |
| **G2 — Prod segura** | `manage.py check --deploy` sin warnings, TLS forzado, media fuera de gunicorn. |
| **G3 — Medición** | GA4 con consentimiento + Search Console verificado. |
| **G4 — Recuperable** | Restore de BD **y media** probado. |
| **G5 — Transferible** | Manual CMS + runbook + credenciales + UAT firmada. |

## 3. Regla de deuda (sin cambios)

Entra al sprint solo si: (1) bloquea un gate, (2) está en un archivo que ya se toca y cuesta ≤ 2 h, (3) evita una migración de datos futura. Techo 20 % semanal, una entrada no bloqueante por semana. El resto actualiza trigger en TECH-DEBT.

## 4. Fase 1 — Tema claro/oscuro (3,5–4,5 d)

### 4.1 Diagnóstico real (medido, no estimado)

- `tokens.css` son **primitivas de marca**, no claves de tema: `--red`, `--navy-800`, `--cloud`, `--white`, `--line`, `--gray`. No existe capa semántica (`--bg`, `--fg`, `--surface`, `--border`, `--muted`).
- **362 usos** de `var()` sobre **39 tokens** distintos en 8 hojas.
- **188 literales de color fuera de `tokens.css`**: 61 hex + 127 `rgb()/rgba()` (components 19+41, pages 16+38, home 9+34, popup 0+7, fan-carousel 6+3, base 11+4).
- Los tokens más usados que **sí** deben cambiar con el tema: `--navy-800` (43), `--gray` (31), `--line` (31), `--cloud` (7), `--white` (4). Los de marca (`--red` 63, `--blue`) se quedan.
- No hay hook de tema en `base.html` ni `color-scheme` declarado. El logo es una sola variante (`logo-rit-color.png`); no hay versión para fondo oscuro.

Conclusión: no es "duplicar el CSS". Es **insertar una capa semántica** y mapear los literales de las superficies que se toquen. Sin esa capa, el modo oscuro es un fork y cada bloque nuevo rompe uno de los dos temas.

### 4.2 Decisión de arquitectura (va en ADR-0003)

- `@media (prefers-color-scheme: dark)` **no** como única fuente: el usuario debe poder forzar.
- Tema resuelto en el **servidor** (cookie) y escrito como `data-theme` en `<html>` **antes del primer paint**: sin FOUC y sin script inline bloqueante.
- Un solo set de tokens; los overrides viven en `[data-theme="dark"]`. Prohibido mantener dos hojas paralelas.
- `color-scheme: light dark` para que los controles nativos y el scrollbar acompañen.

### 4.3 Historias y criterios de aceptación

**US-T1 — El visitante elige tema y se respeta**

- Given primera visita sin cookie, when carga, then se usa `prefers-color-scheme`; si el SO no informa, claro.
- Given el usuario cambia a oscuro, when navega a otra página, then el tema se mantiene sin parpadeo.
- Given el usuario elige "sistema", when cambia el tema del SO, then el sitio acompaña sin recargar.
- Given un tema activo, when se inspecciona `<html>`, then `data-theme` y `color-scheme` son coherentes desde el HTML inicial.

**US-T2 — Ambos temas son legibles (a11y)**

- Given cualquier texto, then contraste ≥ 4.5:1; iconos y bordes de control ≥ 3:1, en los dos temas.
- Given foco de teclado, then el anillo es visible en ambos.
- Given imágenes y logo sobre superficie oscura, then existe variante o contraste aceptable; el ASCII del hero no se pierde.
- Given el popup y el footer, then también están cubiertos (no solo la Home).

**US-T3 — El sistema de color queda sano**

- Given un bloque nuevo, then no introduce hex/rgb crudo: usa tokens semánticos.
- Given las superficies tocadas, then su inventario de literales queda en cero (o justificado: sombras y gradientes de marca que no cambian).
- Given una página sin revisar, then sigue viéndose bien en claro; en oscuro se marca como pendiente, no se degrada.

### 4.4 Entregables por paso

| Paso | Trabajo | Estimado |
|---|---|---|
| 0 | Inventario por superficie + capa semántica en tokens + ADR-0003 | 0,5 d |
| A | Resolución de tema sin FOUC + toggle + chrome (header, footer, popup) | 1 d |
| B | Home: hero + bloques de mayor uso | 1–1,5 d |
| C | Resto de páginas, imágenes/logo, QA de contraste ambos temas | 1–1,5 d |

**DoD Fase 1:** toggle persistente sin FOUC; contraste AA verificado en las 8 páginas × 2 temas (checklist firmado); inventario de literales en cero en las superficies tocadas; ADR-0003 escrito; sin regresiones en claro.

> Nota de alcance: si el cliente pide tema oscuro "solo en la Home", el paso C se corta y se registra la deuda del resto. No se entrega a medias sin decirlo.

## 5. Fase 2 — Prod segura (2 d) · sin dependencia del cliente

- D-02: `DJANGO_SETTINGS_MODULE` explícito; `wsgi.py` falla si falta.
- D-03: `SECURE_PROXY_SSL_HEADER`, `SECURE_SSL_REDIRECT`, cookies `Secure`, HSTS, `check --deploy` en CI.
- Media por nginx, `DJANGO_SERVE_MEDIA=False`.
- Backup de media + **prueba de restore**.
- D-11 de arrastre: manifest estricto tras corregir `collectstatic`.

**DoD:** `check --deploy` limpio; HTTP→HTTPS 301; flags de cookie; `/media/` 200 desde nginx; restore ejecutado y documentado.

## 6. Fase 3 — Leads, cuando el cliente responda (3 d)

Se dispara con tres datos: campos, proveedor/casilla, y decisión de newsletter.

- Persistencia del lead primero; notificación después. Si el SMTP falla, el dato no se pierde.
- CSRF, validación por campo, honeypot, rate limit por IP, página de gracias.
- Tests: válido, inválido, CSRF, antispam, límite y fallo de correo.
- Newsletter: hoy el footer apunta a `/newsletter`, que no existe (404). Mientras no haya proveedor, **se retira el formulario**; es un cambio de 15 minutos y elimina una promesa rota.
- PII: no se registra el mensaje completo en logs; política de retención acordada con el cliente.

## 7. Fase 4 — Cierre (2 d)

- GTM/GA4 **con consentimiento previo** (Ley 1581); sin banner no se enciende.
- Search Console + sitemap.
- Primer slice de D-07: un test de render por cada uno de los 8 Page models.
- UAT, manual del CMS, runbook, credenciales.

## 8. Decisiones abiertas

| # | Decisión | Recomendación |
|---|---|---|
| T1 | ¿Toggle manual o solo `prefers-color-scheme`? | **Toggle de 3 estados** (sistema/claro/oscuro) con cookie. El "solo sistema" se ve moderno y enfurece a quien quiere forzar. |
| T2 | ¿Default? | **Claro.** La marca está diseñada sobre blanco; oscuro es opción. |
| T3 | ¿Alcance? | **Todo el sitio por superficie**, con paso C recortable. Si se entrega solo la Home, se registra deuda. |
| D4 | Newsletter | **Retirar el formulario hoy.** |
| D5 | Consentimiento GA4 | **Sí, banner mínimo antes de GTM.** |
| D6 | Blog / EN | Fuera de esta entrega; fase 2 con alcance propio. |

## 9. Riesgos

- **R1 — Dos fuentes de color.** Si el tema se implementa por overrides puntuales sin capa semántica, el siguiente bloque nace roto en oscuro. Mitigación: paso 0 obligatorio.
- **R2 — FOUC.** Aplicar el tema con JS al final del body produce un flash blanco en oscuro. Mitigación: cookie + atributo en el HTML inicial.
- **R3 — Contraste "a ojo".** El rojo `#e30613` sobre `#001b3a` y los textos de marca en oscuro son los puntos frágiles. Medir, no estimar.
- **R4 — Imágenes de marca.** Una sola variante de logo. Definir antes del paso C, no después.
- **R5 — Backup sin restore.** Sigue abierto; se paga en Fase 2.

## 10. Lo que necesito de ti

1. **T1 y T2** (toggle/default) para cerrar el ADR-0003 y arrancar el paso 0.
2. ¿El logo/isotipo tiene variante para fondo oscuro, o hay que pedirla a diseño?
3. Confirmar que el otro agente ya no toca el repo, para cerrar su rama y evitar pushes cruzados.
