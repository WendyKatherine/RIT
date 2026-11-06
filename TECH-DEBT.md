# TECH-DEBT — RIT Website

> Registro vivo. Última revisión: **2026-11-05**.
> Prioridad: **alta** = bloquea trabajo o implica riesgo de seguridad/datos; **media** = frena cada semana; **baja** = cosmético o higiene.
> Una entrada sin costo concreto no es deuda: no entra.

## Resumen

| Prioridad | Entradas |
|---|---|
| Alta | D-02 · D-03 · D-04 · D-05 · D-06 · D-07 |
| Media | D-08 · D-11 |
| Baja | D-09 · D-10 · D-12 · D-13 |
| Pagadas | D-01 |

## Registro

### D-01 — Nombres de variables inconsistentes entre settings y `.env.example`

- **Área:** configuración / onboarding
- **Atajo:** `.env.example` declara `SECRET_KEY`, `DEBUG` y `ALLOWED_HOSTS`; `dev.py` y `production.py` leen `DJANGO_SECRET_KEY`, `DJANGO_DEBUG` y `DJANGO_ALLOWED_HOSTS`.
- **Por qué:** los settings migraron al prefijo `DJANGO_` y el archivo de ejemplo quedó con los nombres del template.
- **Costo si se deja:** un dev nuevo copia el archivo, cree que configuró y en local los defaults de `dev.py` lo tapan. En staging/producción falta `DJANGO_SECRET_KEY` y el arranque falla, o se queda con un `DEBUG` equivocado.
- **Fix propuesto:** alinear `.env.example` a los nombres reales; agregar un test de settings que falle si falta una variable requerida en producción.
- **Prioridad:** alta.
- **Trigger:** siguiente commit de configuración o antes de sumar a alguien al proyecto.
- **Estado:** pagada (2026-11-05). Guard estático en `tests/test_env_example.py` y test de comportamiento en `tests/test_settings_contract.py`.

### D-02 — El contenedor y WSGI arrancan con settings de desarrollo

- **Área:** deploy / infraestructura
- **Atajo:** `manage.py` y `config/wsgi.py` tienen `DJANGO_SETTINGS_MODULE=config.settings.dev` por defecto; el `CMD` del Dockerfile no define `DJANGO_SETTINGS_MODULE` y su propio comentario dice “settings por defecto: dev”.
- **Por qué:** el Dockerfile se armó para el slice de desarrollo; producción todavía no tiene entrypoint decidido.
- **Costo si se deja:** gunicorn en producción corre con los settings de dev: `DEBUG` por defecto, secreto inseguro si falta la variable, sin manifiesto de estáticos y con `ALLOWED_HOSTS` permisivo. Es un 500 o una exposición esperando el primer deploy.
- **Fix propuesto:** definir `DJANGO_SETTINGS_MODULE=config.settings.production` en el entorno del contenedor/proceso; en `wsgi.py`, quitar el default y fallar si no está definido. `manage.py` puede conservar `dev` para uso local.
- **Prioridad:** alta.
- **Trigger:** antes del primer deploy a staging o producción.

### D-03 — Faltan los settings de seguridad de producción

- **Área:** seguridad / settings
- **Atajo:** `production.py` define secreto, debug, hosts y storage, pero no `SECURE_SSL_REDIRECT`, `SECURE_HSTS_SECONDS`, `SESSION_COOKIE_SECURE`, `CSRF_COOKIE_SECURE` ni `SECURE_PROXY_SSL_HEADER`.
- **Por qué:** el foco de la fase fue SEO, i18n y contenido; el hardening quedó para el slice de deploy.
- **Costo si se deja:** cookies de sesión y CSRF pueden viajar por HTTP si el proxy no fuerza TLS; sin HSTS; `manage.py check --deploy` falla. Es riesgo de sesión, no cosmético.
- **Fix propuesto:** agregar los settings de seguridad y correr `manage.py check --deploy` en CI o como paso obligatorio del deploy.
- **Prioridad:** alta.
- **Trigger:** antes del primer deploy.

### D-04 — El HTML se declara en español aunque la página sea inglesa

- **Área:** i18n / SEO / accesibilidad
- **Atajo:** `base.html` fija `<html lang="es">` y `og:locale=es_CO`; los `hreflang` solo emiten `es-CO` y `x-default`.
- **Por qué:** el contenido nació en español; la versión inglesa aún no se publica.
- **Costo si se deja:** una página `/en/` se anuncia como española a buscadores y lectores de pantalla; no hay `hreflang="en"` que conecte ambas versiones. Se pierde la señal de traducción.
- **Fix propuesto:** derivar `lang` y `og:locale` del locale activo; emitir `hreflang` por cada traducción publicada.
- **Prioridad:** alta si se publica `/en/`; media mientras solo exista español.
- **Trigger:** primer contenido en inglés.

### D-05 — Menú y footer hardcodeados

- **Área:** navegación / contenido
- **Atajo:** `NAV`, `FOOTER_SECTIONS`, `FOOTER_COMPANY` y `FOOTER_LEGAL` viven en `config/context_processors.py` con `href` fijos.
- **Por qué:** transición rápida para el mockup; el menú desde el árbol de Wagtail quedó pendiente.
- **Costo si se deja:** renombrar un slug rompe el menú; una página nueva no aparece; los enlaces legales se mantienen a mano en dos lugares (NAV y footer). El editor no puede ordenar el menú.
- **Fix propuesto:** construir el menú desde `page.get_children().live()` / ancestros y un ajuste de Wagtail para orden/visibilidad; dejar `NAV` solo como fallback.
- **Prioridad:** alta.
- **Trigger:** próxima página nueva o cambio de slug.

### D-06 — Formulario de contacto y newsletter sin backend

- **Área:** conversión / backend
- **Atajo:** `contact_form.html` es una maqueta: los campos existen, pero el botón es `type="button"` y no hay `action` ni handler. El footer hace POST a `/newsletter`, ruta que no existe en `config/urls.py`.
- **Por qué:** faltaba definir validación, antispam, destino de leads y proveedor de newsletter.
- **Costo si se deja:** los leads del sitio se pierden; el formulario de newsletter devuelve 404; no hay CSRF ni validación server-side. Es una fuga directa de negocio.
- **Fix propuesto:** Django Form + vista POST + CSRF + envío a email/CRM; decidir newsletter (proveedor o baja); tests de válido, inválido y error de envío.
- **Prioridad:** alta.
- **Trigger:** antes de publicar el sitio.

### D-07 — Cobertura de tests insuficiente y settings de test vacíos

- **Área:** testing / CI
- **Atajo:** hay smoke tests (raíz, Home, admin), SEO y tests de `HomePage`; no hay tests de los otros 7 tipos de página, de bloques ni de formularios. `config/settings/test.py` está vacío y pytest usa `config.settings.dev`.
- **Por qué:** el seed y el render se validaron a mano durante el mockup; el CI priorizó lint y tipos.
- **Costo si se deja:** un cambio en `blocks.py` o en un template puede romper una página interior sin que CI lo detecte. Los tests corren con `DEBUG=True`, `ALLOWED_HOSTS=["*"]` y el secreto de dev, así que no reproducen producción.
- **Fix propuesto:** `test.py` con `DEBUG=False`, hosts de test y hashers rápidos; test parametrizado que renderice una instancia de cada Page model; tests de bloques con contenido mínimo; cobertura con umbral inicial bajo que suba por sprint.
- **Prioridad:** alta.
- **Trigger:** próxima modificación de bloques, template o página.

### D-08 — `blocks.py` monolítico

- **Área:** dominio / mantenibilidad
- **Atajo:** 521 líneas y 44 clases en un solo archivo.
- **Por qué:** velocidad del mockup; un archivo único era más simple mientras el catálogo crecía.
- **Costo si se deja:** conflictos de merge, revisiones lentas y difícil ubicar un bloque. La clave `stats` se reutiliza para dos clases distintas; renombrarla sin cuidado rompe contenido guardado.
- **Fix propuesto:** fase 1: paquete `apps/home/blocks/` por dominio (home, compartido, contacto, soluciones), reexportando nombres; conservar claves, alias y `Meta.template`. Sin migración si solo se mueven clases.
- **Prioridad:** media.
- **Trigger:** próxima feature que agregue o modifique bloques.

### D-09 — `EventPopup` en `home` y consultado en cada request

- **Área:** arquitectura / performance
- **Atajo:** el snippet global vive en `apps/home` y `config.context_processors.event_popup` ejecuta `EventPopup.objects.filter(...).first()` en cada request.
- **Por qué:** nació con la promo; `common` no era un destino claro y moverlo exige migración.
- **Costo si se deja:** el chrome global depende de `home`; una query extra por request; el día que se mueva hay que migrar el content type.
- **Fix propuesto:** fase 2: mover a `apps/common` con migración; cachear el popup activo por sitio o por fragmento.
- **Prioridad:** baja.
- **Trigger:** fase 2 o cuando se agregue otro elemento global.

### D-10 — Estáticos huérfanos

- **Área:** higiene / estáticos
- **Atajo:** siguen en el repo `apps/home/templates/home/welcome_page.html`, `apps/home/static/css/welcome_page.css`, `config/static/css/config.css` (vacío), `config/static/js/config.js` (vacío) y `config/static/js/hero-ascii.js` (no cargado; `base.html` usa `hero-ascii-rings.js`).
- **Por qué:** restos del template inicial de Wagtail y del mockup.
- **Costo si se deja:** ruido en el repo, `collectstatic` copia basura y un dev puede editar el archivo equivocado.
- **Fix propuesto:** borrar los 5 y agregar una revisión de referencias en el checklist de PR. `welcome_page.html` no tiene referencias; el `rg` ya se hizo.
- **Prioridad:** baja.
- **Trigger:** limpieza de fase 0/2.

### D-11 — Manifest de estáticos no estricto

- **Área:** deploy / estáticos
- **Atajo:** `NonStrictManifestStaticFilesStorage` con `manifest_strict = False`.
- **Por qué:** un `collectstatic` con settings equivocados dejó `staticfiles.json` viejo y cada asset nuevo producía 500.
- **Costo si se deja:** un asset faltante se sirve sin hash en vez de fallar; la invalidación de caché es silenciosa y el bug de fondo (collectstatic con settings incorrectos) sigue ahí.
- **Fix propuesto:** ejecutar `collectstatic --settings=config.settings.production` en el pipeline, verificar el manifiesto y volver a `ManifestStaticFilesStorage` estricto.
- **Prioridad:** media.
- **Trigger:** primer deploy con estáticos.

### D-12 — `PoliticaPage.fecha_doc` es texto libre

- **Área:** modelo de datos
- **Atajo:** `codigo`, `version_doc` y `fecha_doc` son `CharField`; la fecha no se valida ni se ordena.
- **Por qué:** el contenido vino de PDFs con formatos variables.
- **Costo si se deja:** fechas inconsistentes, typos invisibles y filtros futuros imposibles.
- **Fix propuesto:** `DateField` para la fecha y validación de formato para código/versión; migración de datos con parser.
- **Prioridad:** baja.
- **Trigger:** próxima actualización de políticas.

### D-13 — Migración con SQL crudo y numeración duplicada

- **Área:** migraciones
- **Atajo:** `0040_add_index_listing_block.py` usa SQL crudo con `jsonb`; existen dos migraciones `0037` y un merge `0041`.
- **Por qué:** el bloque se insertó directamente en el JSON de páginas y revisiones; las ramas se mergearon.
- **Costo si se deja:** la migración solo corre en Postgres (que es el target, pero ata el histórico), auditar el orden es más difícil y un squash futuro requiere cuidado.
- **Fix propuesto:** documentar la excepción en el ADR/mapa; no repetir SQL crudo para cambios de contenido; evaluar squash al estabilizar el esquema.
- **Prioridad:** baja.
- **Trigger:** próxima migración de datos.

## Top 3 para el próximo sprint

1. **D-02 + D-03** antes de cualquier deploy: settings de producción y hardening.
2. **D-01** antes del próximo onboarding: el archivo de ejemplo no configura lo que el código lee.
3. **D-06** antes de publicar: hoy el sitio no captura leads.

## Deuda que no es deuda

- Los **44 bloques** tienen declaración y seed; no hay bloques muertos.
- La estructura de una sola app `home` es una **decisión**, no deuda: el ADR 0001 la justifica y fija el trigger para revisarla.
