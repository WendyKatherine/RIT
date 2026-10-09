"""Crea el índice /productos/ y las 3 páginas de Productos.

Contenido según los docs de `rit-paginas-web/productos/*.txt` (RIT).
"""
from django.db import migrations

INDEX_BODY = [
    (
        "page_hero",
        {
            "badge": "Productos",
            "title_pre": "Equipos y soluciones",
            "title_hi": "Dell",
            "lead": (
                "Servidores, almacenamiento, as-a-service y equipos para usuario final, con "
                "el respaldo de Dell Technologies."
            ),
            "cta_label": "",
            "cta_href": "",
        },
    ),
    (
        "cta",
        {
            "title": "¿Necesita una cotización?",
            "body": "Le ayudamos a elegir el equipo correcto para su operación.",
            "cta_label": "Solicitar cotización",
            "cta_href": "/contacto/",
        },
    ),
]

CENTROS = [
    (
        "page_hero",
        {
            "badge": "Productos · Centros de Datos",
            "title_pre": "Servidores y almacenamiento para su",
            "title_hi": "centro de datos",
            "lead": (
                "Equipos con la última tecnología, diseñados para todo tipo de carga de "
                "trabajo, adaptables a los presupuestos y requerimientos de procesamiento."
            ),
            "cta_label": "Solicitar cotización",
            "cta_href": "/contacto/",
        },
    ),
    (
        "tabs",
        {
            "badge": "",
            "title": "Servidores",
            "subtitle": "Dell PowerEdge",
            "tabs": [
                {
                    "label": "Torre",
                    "title": "Servidores en Torre",
                    "body": (
                        "Flexibilidad en ubicación física, diversidad de aplicaciones, "
                        "oficinas remotas o principales."
                    ),
                },
                {
                    "label": "Rack",
                    "title": "Servidores Rack",
                    "body": (
                        "Para infraestructura fuerte en cómputo con espacio limitado; "
                        "optimiza el área."
                    ),
                },
                {
                    "label": "Blade",
                    "title": "Servidores Blade",
                    "body": (
                        "Arquitectura simple consolidada; crecer modularmente no es un "
                        "problema."
                    ),
                },
                {
                    "label": "Convergentes",
                    "title": "Infraestructura Convergente",
                    "body": (
                        "Consolida cómputo, almacenamiento y comunicaciones para oficinas "
                        "remotas."
                    ),
                },
                {
                    "label": "Hiperconvergencia (HCI)",
                    "title": "Hiperconvergencia (HCI)",
                    "body": (
                        "Convergencia con almacenamiento definido por software, para cómputo "
                        "confiable de altísimo desempeño."
                    ),
                },
            ],
        },
    ),
    (
        "cards",
        {
            "badge": "",
            "title": "Sistemas de Almacenamiento Dell EMC",
            "intro": (
                "Almacenamiento de entrada y rango medio. Desde arreglos ALL FLASH hasta "
                "sistemas NAS híbridos y de escalamiento horizontal, para consolidación de "
                "cargas, VDI, replicación, federación y compresión."
            ),
            "cards": [
                {
                    "badge": "",
                    "icon": "server",
                    "title": "Dell EMC Unity",
                    "body": "Arreglos unificados ALL FLASH (SAN y NAS) para consolidación.",
                    "cta_label": "",
                    "cta_href": "",
                },
                {
                    "badge": "",
                    "icon": "server",
                    "title": "Serie SC",
                    "body": "SAN de rango medio, ALL FLASH e híbrido.",
                    "cta_label": "",
                    "cta_href": "",
                },
                {
                    "badge": "",
                    "icon": "cloud",
                    "title": "Serie NX",
                    "body": "NAS de escalamiento horizontal.",
                    "cta_label": "",
                    "cta_href": "",
                },
                {
                    "badge": "",
                    "icon": "server",
                    "title": "PowerVault MD / ME4",
                    "body": "Almacenamiento de entrada.",
                    "cta_label": "",
                    "cta_href": "",
                },
            ],
        },
    ),
    (
        "checklist",
        {
            "badge": "",
            "title": "Estrategia de respaldo y continuidad",
            "items": [
                "Procesos de respaldos y recuperación.",
                "Ambientes para Contingencia.",
                "Políticas de retención de datos.",
                "Definición y auditorías de RPO y RTO.",
            ],
        },
    ),
    (
        "highlight",
        {
            "badge": "",
            "title": "Almacenamiento Enterprise o de gama alta",
            "body": (
                "Flash es la nueva norma y la base de la transformación de TI. Con la "
                "Hiperconvergencia y el almacenamiento definido por software de Dell EMC "
                "creamos una capa unificada e inteligente con máxima facilidad, "
                "automatización y control."
            ),
            "bullets": [],
            "cta_label": "",
            "cta_href": "",
        },
    ),
    (
        "checklist",
        {
            "badge": "",
            "title": "Protección de Datos",
            "items": [
                "Integrated Data Protection Appliance",
                "Data Domain",
                "Data Backup and Recovery",
            ],
        },
    ),
    (
        "cta",
        {
            "title": "Dimensione el centro de datos que su negocio necesita",
            "body": "Consulte gratuitamente el estado de su infraestructura actual.",
            "cta_label": "Solicitar asesoría",
            "cta_href": "/contacto/",
        },
    ),
]

APEX = [
    (
        "page_hero",
        {
            "badge": "Productos · Dell APEX",
            "title_pre": "APEX — Céntrese más en los resultados y menos en la",
            "title_hi": "administración de la infraestructura",
            "lead": "Experiencias de nube simples y coherentes ofrecidas como servicio.",
            "cta_label": "Solicitar asesoría personalizada",
            "cta_href": "/contacto/",
        },
    ),
    (
        "cards",
        {
            "badge": "",
            "title": "Beneficios clave",
            "intro": "",
            "cards": [
                {
                    "badge": "",
                    "icon": "cloud",
                    "title": "Sencillez",
                    "body": "Operación simple y coherente en todas sus nubes.",
                    "cta_label": "",
                    "cta_href": "",
                },
                {
                    "badge": "",
                    "icon": "server",
                    "title": "Agilidad",
                    "body": "Aprovisione rápidamente y escale según la demanda.",
                    "cta_label": "",
                    "cta_href": "",
                },
                {
                    "badge": "",
                    "icon": "shield",
                    "title": "Control",
                    "body": "Mantenga el control de sus datos y su infraestructura.",
                    "cta_label": "",
                    "cta_href": "",
                },
            ],
        },
    ),
    (
        "story",
        {
            "badge": "Descripción",
            "title_pre": "Infraestructura como servicio con",
            "title_hi": "pago por uso",
            "paragraphs": [
                (
                    "Aprovisione rápidamente, escale según la demanda y utilice 'Pay as you "
                    "go' en todo el entorno multicloud, bordes y centro de datos. Consuma la "
                    "innovación como servicio de Dell Technologies."
                ),
                (
                    "APEX Cloud Services simplifica las múltiples nubes con experiencia "
                    "coherente y seguridad sólida. APEX Console proporciona acceso de "
                    "autoservicio a un catálogo de servicios de cloud basados en resultados."
                ),
            ],
        },
    ),
    (
        "cta",
        {
            "title": "La transformación digital está en marcha",
            "body": (
                "Acceda a la combinación adecuada de tecnología para la velocidad de su "
                "negocio."
            ),
            "cta_label": "Solicitar asesoría",
            "cta_href": "/contacto/",
        },
    ),
]

USUARIO = [
    (
        "page_hero",
        {
            "badge": "Productos · Usuario Final",
            "title_pre": "Desktop y Portátiles para su",
            "title_hi": "empresa",
            "lead": (
                "Equipos Dell para todos los perfiles de su compañía: desde ofimática "
                "sencilla hasta equipos móviles potentes, sin privarse de estilo y potencia."
            ),
            "cta_label": "Solicitar cotización",
            "cta_href": "/contacto/",
        },
    ),
    (
        "cards",
        {
            "badge": "",
            "title": "Desktop y Portátiles",
            "intro": "",
            "cards": [
                {
                    "badge": "",
                    "icon": "server",
                    "title": "OptiPlex",
                    "body": (
                        "Computadoras de escritorio de clase empresarial, rápidas, seguras "
                        "y escalables (Micro, SFF, MT y AIO)."
                    ),
                    "cta_label": "",
                    "cta_href": "",
                },
                {
                    "badge": "",
                    "icon": "headset",
                    "title": "Latitude",
                    "body": (
                        "Los mejores portátiles corporativos: elegantes, resistentes, "
                        "poderosos y seguros (series 3000, 5000, 7000 y 9000)."
                    ),
                    "cta_label": "",
                    "cta_href": "",
                },
                {
                    "badge": "",
                    "icon": "cloud",
                    "title": "Wyse",
                    "body": (
                        "El cliente ligero más seguro del sector con Dell ThinOS, "
                        "optimizado para cloud Dell y VMware."
                    ),
                    "cta_label": "",
                    "cta_href": "",
                },
            ],
        },
    ),
    (
        "highlight",
        {
            "badge": "",
            "title": "Workstation",
            "body": (
                "Las estaciones de trabajo Dell EMC se caracterizan por su escalabilidad y "
                "alto rendimiento en todas sus gamas de portátiles y escritorio; dan la "
                "mejor experiencia para los trabajos del día a día."
            ),
            "bullets": [],
            "cta_label": "Solicitar asesoría",
            "cta_href": "/contacto/",
        },
    ),
    (
        "cta",
        {
            "title": "Equipe a su equipo de trabajo",
            "body": "Contáctenos para una cotización a la medida de su organización.",
            "cta_label": "Contáctenos ahora",
            "cta_href": "/contacto/",
        },
    ),
]

PAGES = [
    ("Equipos para Centros de Datos", "centros-de-datos", CENTROS),
    ("Dell APEX", "dell-apex", APEX),
    ("Equipos para Usuario Final", "usuario-final", USUARIO),
]


def create_productos(apps, schema_editor):
    from wagtail.models import Page

    from apps.home.models import InteriorPage, SeccionIndexPage

    home = Page.objects.filter(slug="home").first()
    if home is None:
        return

    index = SeccionIndexPage.objects.filter(slug="productos").first()
    if index is None:
        index = SeccionIndexPage(title="Productos", slug="productos", body=INDEX_BODY)
        home.add_child(instance=index)
        index.save_revision().publish()

    for title, slug, body in PAGES:
        if InteriorPage.objects.filter(slug=slug).exists():
            continue
        page = InteriorPage(title=title, slug=slug, body=body)
        index.add_child(instance=page)
        page.save_revision().publish()


def remove_productos(apps, schema_editor):
    from apps.home.models import InteriorPage, SeccionIndexPage

    for _title, slug, _body in PAGES:
        InteriorPage.objects.filter(slug=slug).delete()
    SeccionIndexPage.objects.filter(slug="productos").delete()


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0017_interiorpage_seccionindexpage"),
        ("wagtailsearch", "0010_add_text_fields"),
    ]

    operations = [
        migrations.RunPython(create_productos, remove_productos),
    ]
