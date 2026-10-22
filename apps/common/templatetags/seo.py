"""Etiqueta de plantilla que renderiza el JSON-LD de la pagina actual."""

from __future__ import annotations

import json

from django import template
from django.conf import settings
from django.utils.safestring import mark_safe

from apps.common.seo import (
    breadcrumb_schema,
    organization_schema,
    service_schema,
    website_schema,
)

register = template.Library()


@register.simple_tag(takes_context=True)
def seo_jsonld(context: template.Context, page: object) -> str:
    request = context.get("request")
    site_url = getattr(settings, "SITE_URL", "http://localhost:8000").rstrip("/")
    path = getattr(request, "path", "/") if request is not None else "/"
    canonical_url = f"{site_url}{path}"

    graph = [organization_schema(site_url), website_schema(site_url)]

    crumbs = breadcrumb_schema(page, site_url, canonical_url)
    if crumbs:
        graph.append(crumbs)

    service = service_schema(page, site_url, canonical_url)
    if service:
        graph.append(service)

    data = {"@context": "https://schema.org", "@graph": graph}
    return mark_safe(json.dumps(data, ensure_ascii=False))
