"""Crea el índice /soluciones/ y la página Multicloud e Infraestructura.

Contenido según la spec `soluciones/multicloud-infraestructura.txt` (RIT).
"""
from django.db import migrations

INDEX_BODY = [
    (
        "page_hero",
        {
            "badge": "Soluciones",
            "title_pre": "Soluciones que impulsan",
            "title_hi": "tu negocio",
            "lead": (
                "Infraestructura, ciberseguridad, comunicaciones y consultoría, con "
                "estándares internacionales y respaldo de fabricantes líderes."
            ),
            "cta_label": "",
            "cta_href": "",
        },
    ),
    (
        "cta",
        {
            "title": "¿No sabe por dónde empezar?",
            "body": "Le ayudamos a elegir la solución correcta para su operación.",
            "cta_label": "Solicitar asesoría",
            "cta_href": "/contacto/",
        },
    ),
]

MULTICLOUD_BODY = [
    (
        "page_hero",
        {
            "badge": "Soluciones · Multicloud",
            "title_pre": "Infraestructura de TI ",
            "title_hi": "MultiCloud",
            "lead": (
                "Ofrecemos soluciones de MultiCloud a la medida, con servicios de "
                "instalación, gestión, monitoreo, observabilidad, migración de datos, "
                "planes de recuperación de desastres y replicación."
            ),
            "cta_label": "Solicitar asesoría",
            "cta_href": "/contacto/",
        },
    ),
    (
        "cards",
        {
            "badge": "",
            "title": "",
            "intro": "",
            "cards": [
                {
                    "badge": "Modernización tecnológica",
                    "icon": "cloud",
                    "title": "Nube Híbrida",
                    "body": (
                        "Acompañamos a nuestros clientes en la modernización tecnológica "
                        "de su centro de datos y en la incorporación del modelo de NUBE "
                        "HÍBRIDA para responder a los cambios tecnológicos y a desafíos "
                        "como la inteligencia artificial."
                    ),
                    "cta_label": "",
                    "cta_href": "",
                },
                {
                    "badge": "Tecnologías escalables",
                    "icon": "server",
                    "title": "Cloud con respaldo Dell Technologies",
                    "body": (
                        "Servicios de nube con crecimiento inmediato, escalables horizontal "
                        "y verticalmente. Gestión y monitoreo 7x24, procesos certificados y "
                        "Datacenters TIER IV."
                    ),
                    "cta_label": "",
                    "cta_href": "",
                },
            ],
        },
    ),
    (
        "cards",
        {
            "badge": "",
            "title": "Nuestra oferta de nube",
            "intro": "",
            "cards": [
                {
                    "badge": "",
                    "icon": "cloud",
                    "title": "Servicios de Nube Privada",
                    "body": (
                        "Oferta de nube a la medida con arquitecturas y servicios bajo "
                        "modelos de costo eficientes de pago por uso."
                    ),
                    "cta_label": "",
                    "cta_href": "",
                },
                {
                    "badge": "",
                    "icon": "cloud",
                    "title": "Servicios de Nube Pública",
                    "body": (
                        "Capacidades de nube pública con personal especializado en Azure, "
                        "AWS y GCP para una operación eficiente y segura."
                    ),
                    "cta_label": "",
                    "cta_href": "",
                },
                {
                    "badge": "",
                    "icon": "shield",
                    "title": "Nube Cibersegura",
                    "body": (
                        "Buenas prácticas de operación y ciberseguridad para cumplir sus "
                        "propósitos de cyber resiliencia."
                    ),
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
            "title": "Áreas de TI — Soluciones de alta calidad",
            "items": [
                "Centros de Datos",
                "Infraestructura como Servicio (IaaS)",
                "Servicios en la Nube Pública y Privada",
                "Backup & Recovery Service",
                "Colocación Datacenters Privados",
                "Servidores y Almacenamiento",
            ],
        },
    ),
    (
        "accordion",
        {
            "badge": "",
            "title": "Nuestra oferta Multicloud",
            "items": [
                {
                    "title": "Servicios de consultoría y diseño",
                    "body": (
                        "Soluciones de infraestructura personalizadas para sus necesidades "
                        "actuales y futuras."
                    ),
                },
                {
                    "title": "Servicios de implementación",
                    "body": (
                        "Profesionales certificados en instalación y configuración, con "
                        "respaldo de nuestra PMO."
                    ),
                },
                {
                    "title": "Servicios de monitoreo y gestión",
                    "body": (
                        "Nuestro Centro de Servicios opera 7x24 con detección proactiva de "
                        "fallas."
                    ),
                },
                {
                    "title": "Servicios de seguridad",
                    "body": (
                        "Ciberseguridad en Multicloud mediante tecnologías y buenas "
                        "prácticas que protegen sistemas y datos."
                    ),
                },
                {
                    "title": "Servicios de mantenimiento y soporte",
                    "body": (
                        "Actualizaciones que garantizan la operación y estabilidad de los "
                        "componentes."
                    ),
                },
            ],
        },
    ),
    (
        "highlight",
        {
            "badge": "Destacado",
            "title": "Infraestructura como Servicio (IaaS)",
            "body": (
                "Implemente la infraestructura en su propio centro de datos (on-premise) "
                "o aproveche la potencia de la nube, con la flexibilidad y el control que "
                "necesita."
            ),
            "cta_label": "Solicitar asesoría",
            "cta_href": "/contacto/",
        },
    ),
    (
        "cta",
        {
            "title": "Lleve su infraestructura al siguiente nivel",
            "body": "Contáctenos para una consulta gratuita de su entorno de TI.",
            "cta_label": "Contáctenos ahora",
            "cta_href": "/contacto/",
        },
    ),
]


def create_soluciones(apps, schema_editor):
    from wagtail.models import Page

    from apps.home.models import SolucionPage, SolucionesIndexPage

    home = Page.objects.filter(slug="home").first()
    if home is None:
        return

    index = SolucionesIndexPage.objects.filter(slug="soluciones").first()
    if index is None:
        index = SolucionesIndexPage(
            title="Soluciones", slug="soluciones", body=INDEX_BODY
        )
        home.add_child(instance=index)
        index.save_revision().publish()

    if not SolucionPage.objects.filter(slug="multicloud-infraestructura").exists():
        page = SolucionPage(
            title="Multicloud e Infraestructura de TI",
            slug="multicloud-infraestructura",
            body=MULTICLOUD_BODY,
        )
        index.add_child(instance=page)
        page.save_revision().publish()


def remove_soluciones(apps, schema_editor):
    from apps.home.models import SolucionPage, SolucionesIndexPage

    SolucionPage.objects.filter(slug="multicloud-infraestructura").delete()
    SolucionesIndexPage.objects.filter(slug="soluciones").delete()


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0011_solucionesindexpage_solucionpage"),
        ("wagtailsearch", "0010_add_text_fields"),
    ]

    operations = [
        migrations.RunPython(create_soluciones, remove_soluciones),
    ]
