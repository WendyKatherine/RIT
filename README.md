# RIT Enterprise — Sitio Web (CMS)

[![CI](https://github.com/WendyKatherine/RIT/actions/workflows/ci.yml/badge.svg)](https://github.com/WendyKatherine/RIT/actions)

Sitio corporativo CMS para **RIT Enterprise Solutions SAS** (`ritenterprise.com.co`), construido con **Django + Wagtail**. El contenido (hero, servicios, casos de éxito, datos de contacto…) lo edita el cliente directamente desde el admin de Wagtail — sin tocar código.

> **Front público: cero JavaScript** (decisión de equipo). Todo lo interactivo se resuelve con CSS puro y templates server-side. El diseño sigue el **mockup V1 aprobado por el cliente**, con los colores del Manual de Marca RIT vía design tokens.

## Stack

| Capa | Tecnología |
|---|---|
| Framework | Django 5.2 LTS |
| CMS | Wagtail 7.4 LTS (StreamField, i18n, traducción) |
| Base de datos | PostgreSQL 16 (Docker) |
| Gestión de proyecto | uv (pyproject + lock) |
| Configuración | django-environ (variables de entorno, `.env`) |
| Front | Templates server-side + CSS puro con design tokens (cero JS) |
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
# En .env: genera un SECRET_KEY real y descomenta DATABASE_URL
uv run python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

# 3. Levantar Postgres (puerto host 5433)
docker compose up -d postgres

# 4. Migrar (la migración de seed carga el contenido inicial del mockup)
uv run python manage.py migrate

# 5. Crear el superusuario del admin
uv run python manage.py createsuperuser

# 6. Arrancar
uv run python manage.py runserver
```

- Sitio: <http://localhost:8000/es/>
- Admin (Wagtail): <http://localhost:8000/admin/>
- La raíz `/` redirige a `/es/` (idioma por defecto)

> Si `uv sync` falla tras agregar dependencias, borra `.venv` y repite. Nunca crees un `requirements.txt` — todo vive en `pyproject.toml`/`uv.lock`.

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
| mypy | Tipos estrictos con el plugin de django-stubs (el código de `apps/` está tipeado) |
| pytest | Tests de comportamiento con una base Postgres real de prueba |
| `makemigrations --check` (CI) | Que ningún modelo se quede sin migración |

Los tests corren contra una test DB en tu Postgres local (`docker compose ps` debe estar `healthy`).

## CI (GitHub Actions)

En cada push a `main` y en cada PR: `uv sync --frozen` → ruff → mypy → `makemigrations --check` → pytest contra un servicio Postgres efímero.

## Estructura del repo

```
rit-website/
├── apps/                         # Aplicaciones del proyecto (paquete Python)
│   ├── home/                     # Página de inicio: HomePage + bloques StreamField + seed
│   ├── search/                   # Búsqueda del sitio
│   ├── users/                    # User custom (AUTH_USER_MODEL = "users.User")
│   └── common/                   # Utilidades compartidas (tag de iconos SVG)
├── config/                       # Configuración del proyecto Django
│   ├── settings/                 # base.py · dev.py · production.py · test.py
│   ├── templates/                # base.html + partials (header/footer)
│   ├── static/                   # CSS con design tokens + imágenes
│   ├── context_processors.py     # Nav/footer globales (transición)
│   └── urls.py                   # Rutas (admin + i18n_patterns)
├── tests/                        # Smoke tests del sitio
├── .github/workflows/ci.yml      # CI
├── compose.yaml                  # PostgreSQL 16 (host:5433)
├── Makefile                      # Targets de calidad (make check / fix)
└── pyproject.toml                # Dependencias + config ruff/mypy/pytest
```

## Arquitectura y decisiones

- **CMS sobre Django**: el contenido es *dato en la base de datos* (páginas Wagtail + bloques StreamField), nunca HTML hardcodeado. El front solo renderiza lo que el cliente edita en el admin. Separación contenido ↔ presentación clara.
- **Apps con una responsabilidad** bajo el paquete `apps/`: `home` (páginas/contenido), `users` (identidad), `common` (utilidades transversales), `search` (búsqueda).
- **Configuración 12-factor**: settings divididos por entorno (`base`/`dev`/`production`) y secretos/configuración desde variables de entorno (`.env` gitignored). `DATABASE_URL` es obligatoria (sin fallback a sqlite).
- **i18n es/en**: `LANGUAGE_CODE="es"`, `LocaleMiddleware`, `i18n_patterns` (páginas en `/es/...` y `/en/...`), `simple_translation` para traducir páginas desde el admin.
- **User custom** (`apps.users.User` heredando `AbstractUser`): se define ANTES de la primera migración — después es casi imposible cambiarlo.
- **Front sin JS**: carruseles/tabs con radio-hack CSS, acordeones con `<details>`, animaciones scroll-driven. Estilos con **design tokens** (`tokens.css`) + CSS por sección.
- **Bloques con template explícito**: cada bloque del StreamField declara su template en `Meta` (la auto-detección de Wagtail no resuelve con el paquete anidado `apps/`).

### Contenido editable (para el cliente)

1. Entrar a `/admin/` → **Páginas**.
2. La Home se compone de **bloques** (hero, servicios, casos…): agregar, editar, reordenar o eliminar secciones.
3. **Imágenes** y documentos se gestionan en la librería de Wagtail y se referencian desde los bloques.
4. **Traducción**: cada página tiene su versión por locale (menú Locales / botón *Translate*).

### Cómo agregar una página nueva (dev)

1. Definir el modelo (extiende `Page`) o un bloque nuevo en `apps/home/blocks.py`.
2. Crear su template en `apps/<app>/templates/...`.
3. `uv run python manage.py makemigrations` + `uv run python manage.py migrate`.
4. Crear la página desde el admin (el menú global se actualiza solo al integrar el árbol de páginas — hoy el nav es transitorio en `config/context_processors.py`).

## Estado del proyecto

- ✅ Home completa con StreamField + contenido seed (mockup V1) — editable desde el admin
- ✅ i18n es/en · redirects automáticos · user custom · CI verde · tooling de calidad
- 🔜 Páginas interiores (Qué Hacemos, Nosotros, Industrias, Casos, Recursos, Contacto)
- 🔜 Formularios de contacto/newsletter (Django Forms)
- 🔜 Menú dinámico desde el árbol de páginas de Wagtail
- 🔜 Deploy: Docker + gunicorn + Postgres en VPS; imágenes a Cloudflare R2 (decisión en curso)

## Variables de entorno

| Variable | Descripción |
|---|---|
| `DJANGO_SECRET_KEY` | Secreto de Django (generar con `get_random_secret_key`) |
| `DJANGO_DEBUG` | `True` en dev, `False` en producción |
| `DJANGO_ALLOWED_HOSTS` | Hosts permitidos, separados por coma |
| `DATABASE_URL` | Cadena de conexión Postgres (ej. `postgres://rit:rit@localhost:5433/rit_website`) |
| `WAGTAILADMIN_BASE_URL` | URLs absolutas del admin (previews/correos); en prod `https://ritenterprise.com.co` |
