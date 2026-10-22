"""Cabeceras SEO por entorno.

En produccion el sitio se indexa; en local y staging se marca `noindex` a
nivel de cabecera. Es un segundo candado: aunque alguien olvide el
robots.txt, los buscadores no indexan staging.
"""

from __future__ import annotations

from collections.abc import Callable

from django.conf import settings
from django.http import HttpRequest, HttpResponse


class SeoHeadersMiddleware:
    def __init__(self, get_response: Callable[[HttpRequest], HttpResponse]) -> None:
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        response = self.get_response(request)
        if not getattr(settings, "SEO_INDEXABLE", False):
            response["X-Robots-Tag"] = "noindex, nofollow"
        return response
