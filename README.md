# RIT Enterprise — Sitio Web (CMS)

[![CI](https://github.com/WendyKatherine/RIT/actions/workflows/ci.yml/badge.svg)](https://github.com/WendyKatherine/RIT/actions)

Sitio corporativo de **RIT Enterprise Solutions SAS** (`ritenterprise.com.co`), construido con **Django + Wagtail**. El contenido —hero, servicios, casos, políticas, datos de contacto— se edita desde el admin de Wagtail sin tocar código.

El front es server-side: templates de Django, CSS con design tokens y **JavaScript vanilla**. No hay framework de front. GSAP se usa solo para animaciones atadas al scroll y el sitio sigue funcionando sin JS. La regla completa está en el [ADR 0001](docs/adr/0001-estructura-de-apps.md).

## Stack

| Capa | Tecnología |
|---|---|
| Framework | Django 5.2 LTS |
| CMS | Wagtail 7.4 LTS (StreamField, i18n, traducción) |
| Base de datos | PostgreSQL 16 (Docker, host 5433) |
| Gestión de proyecto | uv (pyproject + lock) |
| Configuración | django-environ (variables de entorno, `.env`) |
| Front | Templates server-side + CSS con design tokens + JS vanilla |
| Calidad | ruff · mypy estricto (django-stubs) · pytest (pytest-django) |
| CI | GitHub Actions (lint, tipos, migraciones, tests con Postgres real) |

## Requisitos

- Python ≥ 3.12
- [uv](https://docs.astral.sh/uv/) (gestor de dependencias)
- Docker (para Postgres local)

## Puesta en marcha (local)

```bash
# 1. Clonar e instalar dependencias
git clone https://github.com/WendyKatherine/RIT.git
cd rit-website
uv sync

# 2. Configurar el entorno
cp .env.example .env
# Edita .env con los nombres que leen los settings (ver "Variables de entorno"):
#   DJANGO_SECRET_KEY=<una clave real>
#   DATABASE_URL=postgres://rit:rit@localhost:5433/rit_website
#   DJANGO_DEBUG=True
uv run python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

# 3. Levantar Postgres (host 5433)
docker compose up -d postgres

# 4. Migrar (las migraciones de seed cargan el contenido del mockup)
uv run python manage.py migrate

# 5. Crear el superusuario del admin
uv run python manage.py createsuperuser

# 6. Arrancar
uv run python manage.py runserver
```

- Sitio: <http://localhost:8000/es/>
- Admin de Wagtail: <http://localhost:8000/admin/>
- Django admin: <http://localhost:8000/django-admin/>
- La raíz `/` redirige con 301 a `/es/`

## Comandos

| Comando | Qué hace |
|---|---|
| `make check` | ruff + formato + mypy + pytest (lo mismo que corre en CI) |
| `make fix` | Auto-corrige lint y formato |
| `make test` | Solo pytest (requiere Postgres arriba) |
| `make mypy` | Solo tipos |
| `make migrate` | `uv run python manage.py migrate` |
| `docker compose up -d postgres` | Levanta solo la base de datos local |

No existe un target `make up`. Para el sitio completo en Docker está el servicio `web` de `compose.yaml`, pero el flujo de desarrollo documentado usa `runserver`.

## Estructura del repo

```text
rit-website/
├── apps/
│   ├── home/                     # Páginas públicas: 8 Page models + 44 bloques
│   │   ├── models.py             # 8 tipos de página + EventPopup (snippet)
│   │   ├── blocks.py             # 29 de nivel superior + 15 anidados
│   │   ├── templates/home/       # 8 templates de página + blocks/ (30 archivos)
│   │   ├── static/css/           # CSS específico de home
│   │   └── migrations/           # Esquema + seed del contenido
│   ├── common/                   # SiteSettings/FooterSettings, SEO, middleware
│   ├── search/                   # Búsqueda del sitio
│   └── users/                    # User custom (AUTH_USER_MODEL = "users.User")
├── config/
│   ├── settings/                 # base · dev · production · test
│   ├── templates/                # base.html + partials (header, footer, popup)
│   ├── static/                   # CSS (tokens) + JS + vendor/gsap
│   ├── context_processors.py     # NAV, footer, SEO y popup globales
│   └── urls.py                   # Admin + i18n_patterns + robots/sitemap
├── docs/
│   ├── adr/0001-estructura-de-apps.md
│   └── mapa-de-contenido.md
├── tests/                        # Smoke tests y SEO
├── .github/workflows/ci.yml      # CI
├── compose.yaml                  # PostgreSQL 16 (host 5433)
├── Makefile                      # Targets de calidad y migración
└── pyproject.toml                # Dependencias + config ruff/mypy/pytest
```

## Páginas

Hay **8 modelos de página** y **27 instancias seed**. La URL mostrada es la versión en español; las rutas usan prefijo de idioma (`/es/` o `/en/` cuando existe traducción).

| Modelo | Template | URL aproximada | Instancias |
|---|---|---|---|
| `HomePage` | `home/home_page.html` | `/es/` | 1 |
| `NosotrosPage` | `home/nosotros_page.html` | `/es/nosotros/` | 1 |
| `ContactoPage` | `home/contacto_page.html` | `/es/contacto/` | 1 |
| `SolucionesIndexPage` | `home/soluciones_index.html` | `/es/soluciones/` | 1 |
| `SolucionPage` | `home/solucion_page.html` | `/es/soluciones/<slug>/` | 5 |
| `SeccionIndexPage` | `home/seccion_index.html` | `/es/<seccion>/` | 4 |
| `InteriorPage` | `home/interior_page.html` | `/es/<seccion>/<slug>/` | 11 |
| `PoliticaPage` | `home/politica_page.html` | `/es/politicas/<slug>/` | 3 |

`SeccionIndexPage` sirve cuatro índices: `/productos/`, `/servicios/`, `/consultoria/` y `/politicas/`. El detalle de cada página y de los 44 bloques está en el [mapa de contenido](docs/mapa-de-contenido.md).

## Front: JS y CSS

**No hay "cero JavaScript".** El proyecto usa JS vanilla donde el CSS no alcanza, sin framework, y degrada sin JS:

- **Global** (`config/templates/base.html`): `hero-ascii-rings.js` (canvas), `event-popup.js` (`<dialog>` nativo) y `popup-gallery.js`.
- **Home** (`home_page.html`): `hero-slider.js`, `fan-carousel.js`, `carousel.js`, `cases-shelf.js` y `title-reveal.js`.
- **GSAP**: vendorizado en `config/static/vendor/gsap/`, cargado una sola vez por `gsap-loader.js`. Solo lo consumen `cases-shelf.js` y `title-reveal.js`, ambos para animaciones atadas al scroll.
- **CSS**: `tokens.css` (marca), `base.css`, `components.css`, `animations.css` y `popup.css` son globales; `home.css` y `pages.css` se cargan por tipo de página; `fan-carousel.css` y `motion.css` solo en Home.

Sin JS, el hero muestra el primer slide, los carruseles quedan como scroll horizontal y el popup no aparece: no se rompe nada.

## Arquitectura y decisiones

- **CMS sobre Django**: el contenido es dato en la base (páginas Wagtail + StreamField), no HTML hardcodeado. El front renderiza lo que el cliente edita en el admin.
- **Una app para las páginas públicas**: `apps/home` concentra los 8 tipos de página y los 44 bloques mientras compartan equipo, árbol y deploy. El porqué, las alternativas descartadas y la deuda aceptada están en el [ADR 0001](docs/adr/0001-estructura-de-apps.md).
- **Apps con una responsabilidad** bajo `apps/`: `home` (páginas/contenido), `users` (identidad), `common` (ajustes globales, SEO, middleware), `search` (búsqueda).
- **Configuración 12-factor**: settings por entorno (`base`/`dev`/`production`/`test`) y secretos desde variables de entorno. `DATABASE_URL` es obligatoria: no hay fallback a sqlite.
- **i18n es/en**: `LANGUAGE_CODE="es"`, `LocaleMiddleware`, `i18n_patterns` y `simple_translation` para traducir páginas desde el admin.
- **User custom** (`apps.users.User` heredando `AbstractUser`): se define antes de la primera migración; después es casi imposible cambiarlo.
- **Bloques con template explícito**: cada bloque declara su template en `Meta`; la auto-detección de Wagtail no resuelve con el paquete anidado `apps/`.
- **Chrome global**: header y footer en `config/templates/partials/`; el popup de evento se expone por context processor y se incluye en `base.html`.

### Contenido editable (para el cliente)

1. Entrar a `/admin/` → **Páginas**.
2. La Home se compone de **bloques** (hero, servicios, casos…): agregar, editar, reordenar o eliminar secciones.
3. **Imágenes** y documentos se gestionan en la librería de Wagtail y se referencian desde los bloques.
4. **Traducción**: cada página tiene su versión por locale (menú Locales / botón *Translate*).
5. **Ajustes globales**: nombre del sitio, preloader, datos del footer y popup de evento se editan en **Settings**.

### Cómo agregar una página nueva (dev)

1. Definir el modelo en `apps/home/models.py` (extiende `Page`) o reutilizar uno de los 8 existentes.
2. Crear su template en `apps/home/templates/home/` y, si lleva secciones nuevas, el bloque en `apps/home/blocks.py`.
3. `uv run python manage.py makemigrations` + `uv run python manage.py migrate`.
4. Crear la página desde el admin.
5. Si debe aparecer en el menú, agregarla a `NAV` en `config/context_processors.py`: **el menú todavía no se genera desde el árbol de Wagtail**.

## Estado del proyecto

- ✅ Home con StreamField + contenido seed (mockup V1), editable desde el admin
- ✅ Nosotros, Contacto y 5 páginas de Soluciones
- ✅ Índices y páginas de Productos (3), Servicios (4) y Consultoría (4)
- ✅ Índice y 3 páginas de Políticas
- ✅ i18n es/en · redirects 301 · user custom · CI configurado · tooling de calidad
- ✅ SEO por entorno: `robots.txt` dinámico, sitemap, canonical, Open Graph y JSON-LD
- ✅ Popup de evento global (una vez por sesión, `?popup=1` para diseñar)
- 🔜 Menú dinámico desde el árbol de páginas de Wagtail (hoy `NAV` está hardcodeado)
- 🔜 Formulario de contacto funcional y newsletter: hoy son maqueta; `/newsletter` no existe como ruta
- 🔜 Deploy: Docker + gunicorn + Postgres en VPS; media en Cloudflare R2 (decisión en curso)
- 🔜 Fase 1: partir `blocks.py` por dominio; fase 2: mover `EventPopup` a `common`
- 🔜 Limpieza de estáticos huérfanos (`welcome_page.css`, `config.css`, `config.js`, `hero-ascii.js`)

## Variables de entorno

| Variable | Descripción | Dev | Prod |
|---|---|---|---|
| `DJANGO_SECRET_KEY` | Secreto de Django (generar con `get_random_secret_key`) | Default inseguro | **Requerida** |
| `DJANGO_DEBUG` | `True` en dev, `False` en producción | `True` | `False` |
| `DJANGO_ALLOWED_HOSTS` | Hosts permitidos, separados por coma | `*` | **Requerida** |
| `DATABASE_URL` | Conexión Postgres (ej. `postgres://rit:rit@localhost:5433/rit_website`) | **Requerida** | **Requerida** |
| `WAGTAILADMIN_BASE_URL` | URL base para links absolutos del admin | `http://localhost:8000` | `https://ritenterprise.com.co` |
| `DJANGO_SERVE_MEDIA` | Django sirve `/media/` (staging sin nginx) | `False` | `False` |
| `DJANGO_CSRF_TRUSTED_ORIGINS` | Orígenes CSRF detrás de proxy, separados por coma | Vacío | URLs públicas |
| `SEO_INDEXABLE` | Habilita indexación, sitemap y `robots.txt` permisivo | `False` | `True` |
| `SITE_URL` | URL pública canónica (canonical, hreflang, OG, JSON-LD) | `http://localhost:8000` | `https://ritenterprise.com.co` |
| `POSTGRES_PASSWORD` | Contraseña del contenedor Postgres de `compose.yaml` | `rit` | La del servidor |

## Calidad y testing

```bash
make check   # ruff + formato + mypy + pytest (lo mismo que corre en CI)
make fix     # auto-corrige lint y formato
make test    # solo pytest
make mypy    # solo tipos
```

| Herramienta | Qué valida |
|---|---|
| ruff | Lint (line-length 100) + formato + orden de imports |
| mypy | Tipos estrictos con django-stubs (el código de `apps/` está tipeado) |
| pytest | Comportamiento con una base Postgres real de prueba |
| `makemigrations --check` (CI) | Que ningún modelo se quede sin migración |

Los tests corren contra una test DB en tu Postgres local: `docker compose ps` debe mostrar el contenedor `healthy`.

## CI (GitHub Actions)

En cada push a `main` y en cada PR: `uv sync --frozen` → ruff → mypy → `makemigrations --check` → pytest contra un servicio Postgres efímero.

## Documentación

- [ADR 0001 — Estructura de apps, templates y chrome global](docs/adr/0001-estructura-de-apps.md)
- [Mapa de contenido — 8 tipos de página y 44 bloques](docs/mapa-de-contenido.md)

Para cambios de estructura, primero se actualiza el ADR y el mapa; después se toca el código.
