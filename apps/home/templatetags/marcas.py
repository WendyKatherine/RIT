"""Resuelve el logo estático de una marca de la sección de aliados.

Los datos de Wagtail guardan el NOMBRE de la marca; este tag lo mapea al archivo
de `static/img/marcas/` (descargados de Simple Icons + Brandfetch).
"""

import os
import re

from django import template
from django.conf import settings
from django.templatetags.static import static

register = template.Library()

# Nombres que no normalizan solos -> clave real del archivo.
_OVERRIDES = {
    "kinston": "kingston",
    "western": "wdgreen",
}

# El carrusel superior del home usa logos distintos a los de la sección de
# aliados (p. ej. Dell se muestra como "Dell Titanium Partner").
_MARQUEE_OVERRIDES = {
    "dell": "dell-titanium",
}


def _marcas_dir() -> str | None:
    for d in getattr(settings, "STATICFILES_DIRS", []):
        p = os.path.join(str(d), "img", "marcas")
        if os.path.isdir(p):
            return p
    return None


def _slug(name: str) -> str:
    key = re.sub(r"[^a-z0-9]", "", (name or "").lower())
    return _OVERRIDES.get(key, key)


def _logo_for_key(key: str) -> str:
    root = _marcas_dir()
    if not root:
        return ""
    for cand in (f"{key}.svg", f"{key}.png", f"{key}.webp", f"bf-{key}.svg", f"bf-{key}.webp"):
        if os.path.exists(os.path.join(root, cand)):
            return static(f"img/marcas/{cand}")
    return ""


@register.simple_tag
def marca_slug(name: str) -> str:
    return _slug(name)


@register.simple_tag
def marca_logo(name: str) -> str:
    return _logo_for_key(_slug(name))


@register.simple_tag
def marca_logo_marquee(name: str) -> str:
    """Logo para el carrusel superior (con overrides propios del marquee)."""
    key = _slug(name)
    return _logo_for_key(_MARQUEE_OVERRIDES.get(key, key))
