"""Context processors globales — navegación y footer del sitio.

El NAV sigue el árbol de navegación aprobado: ítems con dropdown (Soluciones ·
Productos · Servicios · Consultoría) y enlaces directos (Inicio · Nosotros ·
Contacto). El estilo del menú lo define components.css (base de Wendy).
"""

NAV = [
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
