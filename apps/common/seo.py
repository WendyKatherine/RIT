"""Datos de la entidad y utilidades SEO.

Una sola fuente de verdad para el nombre legal, NIT y contacto que se
publican en los datos estructurados (JSON-LD). Si cambia el telefono o la
razon social, se cambia aqui y se refleja en todo el sitio.
"""

from __future__ import annotations

from typing import Any

SITE_NAME = "RIT Enterprise Solutions"
LEGAL_NAME = "RIT Enterprise Solutions SAS"
TAX_ID = "901.106.159-8"
PHONE = "+57 317 5073040"
LOCALITY = "Bogota"
REGION = "Bogota D.C."
COUNTRY = "CO"
LANGUAGE = "es-CO"


def organization_schema(site_url: str) -> dict[str, Any]:
    """Ficha de la empresa para buscadores e IA."""
    return {
        "@type": "Organization",
        "@id": f"{site_url}/#organization",
        "name": SITE_NAME,
        "legalName": LEGAL_NAME,
        "taxID": TAX_ID,
        "url": f"{site_url}/",
        "logo": f"{site_url}/static/img/logo-rit-color.png",
        "telephone": PHONE,
        "address": {
            "@type": "PostalAddress",
            "addressLocality": LOCALITY,
            "addressRegion": REGION,
            "addressCountry": COUNTRY,
        },
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": PHONE,
                "contactType": "sales",
                "availableLanguage": ["es", "en"],
                "areaServed": COUNTRY,
            }
        ],
    }


def website_schema(site_url: str) -> dict[str, Any]:
    return {
        "@type": "WebSite",
        "@id": f"{site_url}/#website",
        "url": f"{site_url}/",
        "name": SITE_NAME,
        "publisher": {"@id": f"{site_url}/#organization"},
        "inLanguage": LANGUAGE,
    }


def breadcrumb_schema(page: Any, site_url: str, canonical_url: str) -> dict[str, Any] | None:
    """Migas de pan a partir de los ancestros reales de la pagina."""
    if page is None:
        return None
    items: list[dict[str, Any]] = []
    for ancestor in page.get_ancestors().live().filter(depth__gt=1):
        items.append(
            {
                "@type": "ListItem",
                "position": len(items) + 1,
                "name": ancestor.title,
                "item": f"{site_url}{ancestor.url}",
            }
        )
    items.append(
        {
            "@type": "ListItem",
            "position": len(items) + 1,
            "name": page.title,
            "item": canonical_url,
        }
    )
    if len(items) < 2:
        return None
    return {"@type": "BreadcrumbList", "itemListElement": items}


def service_schema(page: Any, site_url: str, canonical_url: str) -> dict[str, Any] | None:
    """Marca como Service las paginas de solucion."""
    if page is None or page.specific_class.__name__ != "SolucionPage":
        return None
    return {
        "@type": "Service",
        "name": page.title,
        "url": canonical_url,
        "provider": {"@id": f"{site_url}/#organization"},
        "areaServed": {"@type": "Country", "name": "Colombia"},
    }
