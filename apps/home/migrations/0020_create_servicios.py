"""Crea el índice /servicios/ y las 4 páginas de Servicios.

Contenido según los docs de `rit-paginas-web/servicios/*.txt` (RIT).
"""
from django.db import migrations

INDEX_BODY = [
    (
        "page_hero",
        {
            "badge": "Servicios",
            "title_pre": "Servicios que",
            "title_hi": "impulsan tu operación",
            "lead": (
                "Soporte, monitoreo, instalación y postventa con estándares "
                "internacionales y respaldo de fabricantes líderes."
            ),
            "cta_label": "",
            "cta_href": "",
        },
    ),
    (
        "cta",
        {
            "title": "¿Necesita soporte especializado?",
            "body": "Estamos para ayudarle a mantener su operación siempre activa.",
            "cta_label": "Contáctenos",
            "cta_href": "/contacto/",
        },
    ),
]

CENTRO = [
    (
        "page_hero",
        {
            "badge": "Servicios · Centro de Servicios",
            "title_pre": "Centro de Servicios —",
            "title_hi": "DOC, NOC y SOC 24/7",
            "lead": (
                "El área de Operaciones de Servicios de TI de RIT soporta, gestiona, "
                "administra y brinda consultoría de servicios profesionales en todas las "
                "tecnologías de nuestra propuesta."
            ),
            "cta_label": "Contáctenos",
            "cta_href": "/contacto/",
        },
    ),
    (
        "cards",
        {
            "badge": "",
            "title": "Operación centralizada",
            "intro": "",
            "cards": [
                {
                    "badge": "",
                    "icon": "server",
                    "title": "DOC — Digital Operations Center",
                    "body": (
                        "El corazón operativo donde monitorizamos y gestionamos la salud de "
                        "tus plataformas."
                    ),
                    "bullets": [
                        "Visibilidad unificada",
                        "Automatización de tareas",
                        "Informes ejecutivos",
                    ],
                    "cta_label": "",
                    "cta_href": "",
                },
                {
                    "badge": "",
                    "icon": "server",
                    "title": "NOC — Network Operations Center",
                    "body": "Asegura la continuidad y el desempeño de tus redes.",
                    "bullets": [
                        "Monitoreo de enlaces",
                        "Gestión de incidentes con SLA",
                        "Optimización continua",
                    ],
                    "cta_label": "",
                    "cta_href": "",
                },
                {
                    "badge": "",
                    "icon": "shield",
                    "title": "SOC/CSIRT — Seguridad Gestionada 7x24",
                    "body": "Detecta, analiza y responde a incidentes de seguridad.",
                    "bullets": [
                        "Monitoreo con correlación avanzada",
                        "Análisis forense",
                        "Modelos flexibles",
                    ],
                    "cta_label": "",
                    "cta_href": "",
                },
            ],
        },
    ),
    (
        "accordion",
        {
            "badge": "",
            "title": "Servicios Profesionales",
            "items": [
                {
                    "title": "Espacios de Trabajo Inteligentes",
                    "body": (
                        "DaaS · ServiceDesk (SPOC) · Soporte en Sitio · Administración de "
                        "Dispositivos (DOC) · Administración de Activos TI · Servicios O365"
                    ),
                },
                {
                    "title": "Ciberseguridad y Defensa (Protección 360°)",
                    "body": (
                        "SOC/NOC 24/7 · Respuesta a incidentes · Análisis de riesgo · "
                        "Cumplimiento · Pentesting · Inteligencia de amenazas · MDR · "
                        "Postura de seguridad"
                    ),
                },
                {
                    "title": "Infraestructura y Cloud",
                    "body": (
                        "Monitoreo NOC · Nube Híbrida · Migración Cloud · Administración de "
                        "Infraestructura · DRP y Continuidad · Enroque de DataCenter"
                    ),
                },
                {
                    "title": "Comunicaciones Avanzadas",
                    "body": (
                        "IP PBXaaS y CCaaS · Telefonía IP · Agente IA/ChatBot · Salas y "
                        "Carteleras · Omnicanalidad + IA · Telepresencia"
                    ),
                },
            ],
        },
    ),
    (
        "badges",
        {
            "badge": "",
            "title": "¿Por qué elegirnos?",
            "subtitle": "",
            "items": [
                "ISO 27001",
                "SOC resiliente",
                "CSIRT",
                "Modelo OS3",
                "MSSP Alert",
                "Multimarca",
                "Ingeniería certificada",
            ],
        },
    ),
    (
        "cta",
        {
            "title": "La tecnología impulsa su negocio",
            "body": (
                "Soporte técnico especializado, servicios administrados y monitoreo 24/7."
            ),
            "cta_label": "Contáctenos",
            "cta_href": "/contacto/",
        },
    ),
]

INSTALACION = [
    (
        "page_hero",
        {
            "badge": "Servicios · Instalación e Implementación",
            "title_pre": "Instalación de Equipos, Servidores,",
            "title_hi": "Almacenamiento y Redes",
            "lead": (
                "Ejecutada por ingenieros y técnicos altamente calificados, garantiza "
                "efectividad y rapidez, haciendo uso de las mejores prácticas definidas por "
                "Dell EMC."
            ),
            "cta_label": "Solicitar asesoría",
            "cta_href": "/contacto/",
        },
    ),
    (
        "split_bullets",
        {
            "badge": "Destacado",
            "title": "Ingenieros certificados por DELL",
            "intro": (
                "Todos los servicios de instalación, configuración y puesta en "
                "funcionamiento de servidores tradicionales, de convergencia o "
                "hiperconvergencia son ejecutados por ingenieros certificados por DELL con "
                "amplia experiencia certificable."
            ),
            "items": [
                {
                    "title": "Diseño y asesoramiento",
                    "body": (
                        "Por ingenieros certificados como Technical Architect."
                    ),
                },
                {
                    "title": "Análisis y diseño de soluciones",
                    "body": (
                        "De infraestructura y computación en su centro de datos o en la "
                        "nube."
                    ),
                },
                {
                    "title": "Acompañamiento",
                    "body": "Como parte de su transformación digital.",
                },
            ],
            "note": "",
        },
    ),
    (
        "cta",
        {
            "title": "Ponga su infraestructura en manos expertas",
            "body": "Contáctenos para planear la instalación de sus equipos.",
            "cta_label": "Contáctenos ahora",
            "cta_href": "/contacto/",
        },
    ),
]

MONITOREO = [
    (
        "page_hero",
        {
            "badge": "Servicios · Monitoreo y Gestión",
            "title_pre": "Monitoreo y Gestión de",
            "title_hi": "Eventos 24/7",
            "lead": (
                "Nuestro Centro de Servicios opera en modelo 7x24, enfocado en la detección "
                "proactiva de fallas y problemas para que sus sistemas funcionen de manera "
                "óptima."
            ),
            "cta_label": "Solicitar asesoría",
            "cta_href": "/contacto/",
        },
    ),
    (
        "split_bullets",
        {
            "badge": "Destacado",
            "title": "Monitoreo de seguridad SOC / NOC 7-24-365",
            "intro": (
                "Monitoreamos de forma continua los eventos de seguridad y de red, con "
                "correlación avanzada para detectar amenazas y anomalías en tiempo real."
            ),
            "items": [
                {
                    "title": "Monitoreo continuo de seguridad",
                    "body": "Con correlación avanzada de eventos.",
                },
                {
                    "title": "Monitoreo de red",
                    "body": "Enlaces, dispositivos y servicios críticos.",
                },
                {
                    "title": "Respuesta a incidentes",
                    "body": "Atención, gestión y respuesta de incidentes de seguridad.",
                },
                {
                    "title": "Detección proactiva",
                    "body": "De fallas y problemas antes de que afecten la operación.",
                },
            ],
            "note": "",
        },
    ),
    (
        "cards",
        {
            "badge": "",
            "title": "Gestión integral",
            "intro": "",
            "cards": [
                {
                    "badge": "",
                    "icon": "chat",
                    "title": "Gestión de incidentes y escalamiento",
                    "body": "Con métricas de SLA claras para cada servicio.",
                    "bullets": [],
                    "cta_label": "",
                    "cta_href": "",
                },
                {
                    "badge": "",
                    "icon": "server",
                    "title": "Optimización continua",
                    "body": "De capacidad, performance y disponibilidad.",
                    "bullets": [],
                    "cta_label": "",
                    "cta_href": "",
                },
                {
                    "badge": "",
                    "icon": "chat",
                    "title": "Informes ejecutivos",
                    "body": "Tableros de experiencia digital orientados al negocio.",
                    "bullets": [],
                    "cta_label": "",
                    "cta_href": "",
                },
            ],
        },
    ),
    (
        "cta",
        {
            "title": "Tranquilidad total sobre su infraestructura",
            "body": "Monitoreo proactivo que evita interrupciones antes de que ocurran.",
            "cta_label": "Contáctenos",
            "cta_href": "/contacto/",
        },
    ),
]

POSTVENTA = [
    (
        "page_hero",
        {
            "badge": "Servicios · Postventa",
            "title_pre": "Servicios",
            "title_hi": "Postventa",
            "lead": "Calificados como los mejores en el mercado de la tecnología.",
            "cta_label": "Solicitar soporte",
            "cta_href": "/contacto/",
        },
    ),
    (
        "highlight",
        {
            "badge": "Destacado",
            "title": "Los entornos complejos necesitan soporte de clase empresarial",
            "body": (
                "Con los servicios de soporte de Dell obtendrá la asistencia de expertos, "
                "las herramientas y los recursos para concentrarse en el crecimiento. En "
                "RIT le asesoramos sobre el estado de soporte de sus equipos DELL y le "
                "ayudamos a renovar sus garantías."
            ),
            "bullets": [],
            "cta_label": "",
            "cta_href": "",
        },
    ),
    (
        "cards",
        {
            "badge": "",
            "title": "Nuestros servicios postventa",
            "intro": "",
            "cards": [
                {
                    "badge": "",
                    "icon": "server",
                    "title": "Impresión de etiquetas",
                    "body": "Para identificar sus equipos y controlar su inventario.",
                    "bullets": [],
                    "cta_label": "",
                    "cta_href": "",
                },
                {
                    "badge": "",
                    "icon": "server",
                    "title": "Instalación y cambio de componentes",
                    "body": (
                        "Disponibilidad de partes, garantizando la continuidad operacional "
                        "del hardware."
                    ),
                    "bullets": [],
                    "cta_label": "",
                    "cta_href": "",
                },
                {
                    "badge": "",
                    "icon": "server",
                    "title": "Personalización de BIOS",
                    "body": "Adaptándose a las definiciones y necesidades de la empresa.",
                    "bullets": [],
                    "cta_label": "",
                    "cta_href": "",
                },
                {
                    "badge": "",
                    "icon": "cloud",
                    "title": "Creación y Clonación de Imágenes",
                    "body": (
                        "Procesos para agilizar la entrada de equipos nuevos, cumpliendo los "
                        "estándares definidos."
                    ),
                    "bullets": [],
                    "cta_label": "",
                    "cta_href": "",
                },
            ],
        },
    ),
    (
        "cta",
        {
            "title": "Su hardware siempre operativo",
            "body": "Contáctenos para renovar garantías o programar un servicio.",
            "cta_label": "Contáctenos ahora",
            "cta_href": "/contacto/",
        },
    ),
]

PAGES = [
    ("Centro de Servicios DOC, NOC y SOC 24/7", "centro-de-servicios", CENTRO),
    ("Instalación e Implementación", "instalacion", INSTALACION),
    ("Monitoreo y Gestión (NOC/SOC)", "monitoreo-gestion", MONITOREO),
    ("Servicios Postventa", "postventa", POSTVENTA),
]


def create_servicios(apps, schema_editor):
    from wagtail.models import Page

    from apps.home.models import InteriorPage, SeccionIndexPage

    home = Page.objects.filter(slug="home").first()
    if home is None:
        return

    index = SeccionIndexPage.objects.filter(slug="servicios").first()
    if index is None:
        index = SeccionIndexPage(title="Servicios", slug="servicios", body=INDEX_BODY)
        home.add_child(instance=index)
        index.save_revision().publish()

    for title, slug, body in PAGES:
        if InteriorPage.objects.filter(slug=slug).exists():
            continue
        page = InteriorPage(title=title, slug=slug, body=body)
        index.add_child(instance=page)
        page.save_revision().publish()


def remove_servicios(apps, schema_editor):
    from apps.home.models import InteriorPage, SeccionIndexPage

    for _title, slug, _body in PAGES:
        InteriorPage.objects.filter(slug=slug).delete()
    SeccionIndexPage.objects.filter(slug="servicios").delete()


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0019_alter_interiorpage_body_alter_solucionpage_body"),
        ("wagtailsearch", "0010_add_text_fields"),
    ]

    operations = [
        migrations.RunPython(create_servicios, remove_servicios),
    ]
