"""Context processors globales — navegación y footer del sitio.

El NAV sigue el árbol de navegación aprobado: ítems con dropdown (Soluciones ·
Productos · Servicios · Consultoría) y enlaces directos (Inicio · Nosotros ·
Contacto). El estilo del menú lo define components.css (base de Wendy).
"""

from typing import Any

NAV: list[dict[str, Any]] = [
    {"label": "Inicio", "href": "/", "route": "home"},
    {
        "label": "Soluciones",
        "route": "soluciones",
        "children": [
            {
                "label": "Multicloud e Infraestructura",
                "href": "/soluciones/multicloud-infraestructura/",
            },
            {"label": "Ciberseguridad", "href": "/soluciones/ciberseguridad/"},
            {"label": "Comunicaciones Avanzadas", "href": "/soluciones/comunicaciones-avanzadas/"},
            {
                "label": "Espacios de Trabajo Inteligentes",
                "href": "/soluciones/espacios-de-trabajo/",
            },
            {"label": "Digitalización de Procesos", "href": "/soluciones/digitalizacion-procesos/"},
        ],
    },
    {
        "label": "Productos",
        "route": "productos",
        "children": [
            {"label": "Centros de Datos", "href": "/productos/centros-de-datos/"},
            {"label": "Usuario Final", "href": "/productos/usuario-final/"},
            {"label": "Dell APEX", "href": "/productos/dell-apex/"},
        ],
    },
    {
        "label": "Servicios",
        "route": "servicios",
        "children": [
            {"label": "Centro de Servicios", "href": "/servicios/centro-de-servicios/"},
            {"label": "Monitoreo y Gestión", "href": "/servicios/monitoreo-gestion/"},
            {"label": "Instalación e Implementación", "href": "/servicios/instalacion/"},
            {"label": "Servicios Postventa", "href": "/servicios/postventa/"},
        ],
    },
    {
        "label": "Consultoría",
        "route": "consultoria",
        "children": [
            {
                "label": "Continuidad de Negocio (BCP/DRP)",
                "href": "/consultoria/continuidad-negocio/",
            },
            {"label": "Plan Estratégico de TI", "href": "/consultoria/plan-estrategico/"},
            {
                "label": "Arquitectura e Integración",
                "href": "/consultoria/arquitectura-integracion/",
            },
            {"label": "Migraciones SAP", "href": "/consultoria/migraciones-sap/"},
        ],
    },
    {"label": "Nosotros", "href": "/nosotros/", "route": "nosotros"},
    {"label": "Contacto", "href": "/contacto/", "route": "contacto"},
]

# Columnas del footer derivadas del árbol del menú (NAV) — una sola fuente de verdad.
FOOTER_SECTIONS = [item for item in NAV if item.get("children")]

FOOTER_COMPANY = [
    {"label": "Inicio", "href": "/"},
    {"label": "Nosotros", "href": "/nosotros/"},
    {"label": "Contacto", "href": "/contacto/"},
]

FOOTER_LEGAL = [
    {"label": "Política de Tratamiento de Datos", "href": "/politicas/tratamiento-datos/"},
    {"label": "Código de Ética y Buena Conducta", "href": "/politicas/codigo-etica/"},
    {"label": "Política SIG", "href": "/politicas/politica-sig/"},
]


def global_nav(request: object) -> dict:
    """Expone NAV y footer en todas las plantillas."""
    return {
        "nav": NAV,
        "footer_sections": FOOTER_SECTIONS,
        "footer_company": FOOTER_COMPANY,
        "footer_legal": FOOTER_LEGAL,
    }


def seo(request: object) -> dict:
    """Expone URL canonica y el interruptor de indexado a las plantillas."""
    from django.conf import settings

    site_url = getattr(settings, "SITE_URL", "").rstrip("/")
    path = getattr(request, "path", "/")
    return {
        "seo_indexable": getattr(settings, "SEO_INDEXABLE", False),
        "site_url": site_url,
        "canonical_url": f"{site_url}{path}",
    }


def event_popup(request: object) -> dict:
    from apps.home.models import EventPopup

    popup = EventPopup.objects.filter(is_active=True).order_by("-id").first()
    return {"event_popup": popup}
