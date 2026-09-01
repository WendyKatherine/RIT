"""Context processors globales — navegación y footer del sitio.

TRANSICIÓN: estos datos viven hoy en Python (como en el front antiguo con
data.py), para no perder el contenido editorial ya aprobado.

El plan es migrarlos a Wagtail en slices posteriores:
- Slice 4: el menú (NAV) saldrá del árbol de páginas de Wagtail.
- Slice 5: el footer (contacto, links) saldrá de snippets/settings.
"""

NAV = [
    {"label": "Inicio", "href": "/", "route": "home"},
    {"label": "Qué Hacemos", "href": "/que-hacemos", "route": "que_hacemos"},
    {"label": "Industrias", "href": "/industrias", "route": "industrias"},
    {"label": "Nosotros", "href": "/nosotros", "route": "nosotros"},
    {"label": "Casos", "href": "/casos", "route": "casos"},
    {"label": "Recursos", "href": "/recursos", "route": "recursos"},
    {"label": "Contacto", "href": "/contacto", "route": "contacto"},
]

FOOTER_SERVICES = [
    {"label": "Ciberseguridad", "href": "/que-hacemos#ciberseguridad"},
    {"label": "Multicloud", "href": "/que-hacemos#multicloud"},
    {"label": "Estaciones", "href": "/que-hacemos#estaciones"},
    {"label": "Centro de Servicios", "href": "/que-hacemos#centro-de-servicios"},
    {"label": "Comunicaciones", "href": "/que-hacemos#comunicaciones"},
]

FOOTER_COMPANY = [
    {"label": "Nosotros", "href": "/nosotros"},
    {"label": "Industrias", "href": "/industrias"},
    {"label": "Casos de éxito", "href": "/casos"},
    {"label": "Recursos", "href": "/recursos"},
    {"label": "Contacto", "href": "/contacto"},
]


def global_nav(request: object) -> dict:
    """Expone NAV y footer en todas las plantillas."""
    return {
        "nav": NAV,
        "footer_services": FOOTER_SERVICES,
        "footer_company": FOOTER_COMPANY,
    }
