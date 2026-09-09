# syntax=docker/dockerfile:1
# Imagen del sitio RIT — dependencias con uv (lock reproducible).
# Default SEGURO: settings de producción (si faltan env vars, falla al arrancar
# en vez de exponer DEBUG=True). El dev local lo pide explícito en compose.yaml.
# TODO deploy slice: hardening (usuario no-root, whitenoise/nginx)

# ── Builder: compila/instala dependencias ──
FROM python:3.12-slim-bookworm AS builder

# Paquetes de build para wheels con extensión C (psycopg, Pillow, …)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev \
 && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir uv

WORKDIR /app

# 1) Solo dependencias primero → capa cacheable (se invalida solo si cambia el lock)
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-install-project

# 2) Código fuente
COPY . .

# ── Runtime ──
FROM python:3.12-slim-bookworm

# Librerías runtime de las wheels compiladas
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    libjpeg62-turbo \
    libwebp7 \
 && rm -rf /var/lib/apt/lists/*

ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=config.settings.production

WORKDIR /app
COPY --from=builder /app/ /app/

EXPOSE 8000

# Migra al arrancar y sirve con gunicorn. Los settings los define el entorno
# (la imagen por defecto usa production; el dev local los sobreescribe a dev).
CMD ["sh", "-c", "python manage.py migrate --noinput && gunicorn config.wsgi:application --bind 0.0.0.0:8000"]
