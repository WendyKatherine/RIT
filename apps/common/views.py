"""Vistas SEO: robots.txt dinamico por entorno.

No se sirve un archivo estatico a proposito: el mismo codigo debe producir
un robots permisivo en produccion y uno bloqueante en staging/local. Un
robots.txt estatico copiado a staging indexa el staging.
"""

from __future__ import annotations

from django.conf import settings
from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.decorators.http import require_POST

from apps.common.theme import theme_values


def robots_txt(request: HttpRequest) -> HttpResponse:
    site_url = getattr(settings, "SITE_URL", "http://localhost:8000").rstrip("/")

    if not getattr(settings, "SEO_INDEXABLE", False):
        lines = [
            "# Entorno no indexable (local/staging).",
            "User-agent: *",
            "Disallow: /",
            "",
        ]
    else:
        lines = [
            "User-agent: *",
            "Allow: /",
            "Disallow: /admin/",
            "Disallow: /django-admin/",
            "Disallow: /documents/",
            "Disallow: /search",
            "",
            "# Bots de IA: permitidos para que puedan citar el sitio.",
            "User-agent: GPTBot",
            "Allow: /",
            "",
            "User-agent: ClaudeBot",
            "Allow: /",
            "",
            "User-agent: PerplexityBot",
            "Allow: /",
            "",
            "User-agent: Google-Extended",
            "Allow: /",
            "",
            "Content-Signal: search=yes, ai-input=yes, ai-train=no",
            "",
            f"Sitemap: {site_url}/sitemap.xml",
            "",
        ]

    return HttpResponse("\n".join(lines), content_type="text/plain; charset=utf-8")


@require_POST
def set_theme(request: HttpRequest, theme: str) -> HttpResponse:
    if theme not in theme_values:
        return HttpResponseBadRequest("Theme not valid")

    next_url = request.POST.get("next", "")
    if not url_has_allowed_host_and_scheme(
        next_url,
        allowed_hosts={request.get_host()},
        require_https=request.is_secure(),
    ):
        next_url = "/"

    response = HttpResponseRedirect(next_url)

    response.set_cookie(
        "theme",
        theme,
        max_age=31536000,
        path="/",
        httponly=True,
        samesite="Lax",
        secure=request.is_secure(),
    )

    return response
