"""Crea la página Ciberseguridad (bajo /soluciones/) con el contenido real.

Contenido según la spec `soluciones/ciberseguridad.txt` (RIT / Open Group).
"""
from django.db import migrations

BODY = [
    (
        "page_hero",
        {
            "badge": "Soluciones · Ciberseguridad",
            "title_pre": "Protege tu negocio en un ",
            "title_hi": "mundo digital",
            "lead": (
                "En RIT entendemos los desafíos que enfrentan las empresas en el entorno "
                "digital actual. Por eso ofrecemos soluciones de ciberseguridad integrales "
                "que te permiten proteger tus datos, garantizar la continuidad de tu "
                "negocio y mantener la confianza de tus clientes."
            ),
            "cta_label": "Solicitar consulta gratuita",
            "cta_href": "/contacto/",
        },
    ),
    (
        "cards",
        {
            "badge": "",
            "title": "Nuestro Modelo de Entrega de Valor",
            "intro": "¿Por qué elegirnos?",
            "cards": [
                {
                    "badge": "",
                    "icon": "shield",
                    "title": "Estrategia y arquitectura personalizada",
                    "body": (
                        "Definimos una hoja de ruta clara y personalizada, alineada con los "
                        "objetivos estratégicos del negocio. Diseñamos soluciones "
                        "tecnológicas que generan valor desde el primer momento."
                    ),
                    "cta_label": "",
                    "cta_href": "",
                },
                {
                    "badge": "",
                    "icon": "server",
                    "title": "Operación y transición del servicio",
                    "body": (
                        "Implementamos y gestionamos la transición de servicios con "
                        "precisión operativa, asegurando continuidad, eficiencia y mínima "
                        "disrupción para el negocio."
                    ),
                    "cta_label": "",
                    "cta_href": "",
                },
                {
                    "badge": "",
                    "icon": "chat",
                    "title": "Mejora continua del servicio",
                    "body": (
                        "Evaluamos y optimizamos constantemente el rendimiento de los "
                        "servicios para adaptarnos a los cambios del entorno, impulsando la "
                        "innovación y la excelencia operativa."
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
            "title": "Retos Actuales en Ciberseguridad",
            "intro": "Expertos en Ciberseguridad",
            "cards": [
                {
                    "badge": "",
                    "icon": "shield",
                    "title": "Gestión de accesos e identidades",
                    "body": (
                        "Aseguramos el acceso a los recursos de forma controlada y basada "
                        "en confianza cero mediante control de admisión, gestión de "
                        "identidades y privilegios."
                    ),
                    "cta_label": "",
                    "cta_href": "",
                },
                {
                    "badge": "",
                    "icon": "cloud",
                    "title": "Protección de infraestructura y nube",
                    "body": (
                        "Fortalecemos la red, los puntos finales y los entornos en la nube "
                        "con firewalls avanzados, protección para aplicaciones y mecanismos "
                        "anti-DDoS."
                    ),
                    "cta_label": "",
                    "cta_href": "",
                },
                {
                    "badge": "",
                    "icon": "server",
                    "title": "Monitoreo y detección de amenazas",
                    "body": (
                        "Utilizamos herramientas que permiten identificar comportamientos "
                        "sospechosos, correlacionamos eventos y detectamos amenazas en "
                        "tiempo real."
                    ),
                    "cta_label": "",
                    "cta_href": "",
                },
                {
                    "badge": "",
                    "icon": "chat",
                    "title": "Seguridad del correo y concienciación del usuario",
                    "body": (
                        "Protegemos el correo electrónico corporativo y educamos a los "
                        "usuarios para reducir riesgos como phishing, ingeniería social y "
                        "errores humanos."
                    ),
                    "cta_label": "",
                    "cta_href": "",
                },
                {
                    "badge": "",
                    "icon": "shield",
                    "title": "Cumplimiento normativo y evaluación de postura",
                    "body": (
                        "Evaluamos tu nivel de cumplimiento frente a normas como ISO 27001, "
                        "identificamos brechas de seguridad y aplicamos controles de "
                        "gobernanza, riesgo y cumplimiento."
                    ),
                    "cta_label": "",
                    "cta_href": "",
                },
                {
                    "badge": "",
                    "icon": "headset",
                    "title": "Respuesta ante incidentes y recuperación",
                    "body": (
                        "Automatizamos la respuesta a incidentes, recuperamos rápidamente "
                        "información crítica y establecemos planes para la continuidad del "
                        "negocio."
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
            "badge": "Servicios de Ciberseguridad y Defensa",
            "title": "Protección 360°",
            "items": [
                "Monitoreo de seguridad SOC / NOC 7-24-365",
                "Atención, gestión y respuesta de incidentes de seguridad",
                "Análisis y evaluación de riesgo",
                "Consultoría de gobierno y cumplimiento normativo",
                "Concientización y sensibilización de seguridad",
                "Ethical Hacking y Pentesting",
                "Inteligencia de amenazas",
                "MDR (Managed Detection and Response)",
                "Postura de seguridad",
            ],
        },
    ),
    (
        "highlight",
        {
            "badge": "Destacado",
            "title": "Seguridad Gestionada 7x24 · SOC/CSIRT",
            "body": (
                "Nuestro SOC/CSIRT combina personas, procesos y tecnología para detectar, "
                "analizar y responder a incidentes de seguridad, reduciendo el impacto en "
                "tu operación y reputación."
            ),
            "bullets": [
                "Monitoreo continuo de eventos de seguridad con correlación avanzada.",
                "Análisis forense, contención y erradicación de incidentes.",
                (
                    "Modelos de servicio flexibles: desde acompañamiento hasta operación "
                    "total como servicio."
                ),
            ],
            "cta_label": "Solicitar consulta gratuita",
            "cta_href": "/contacto/",
        },
    ),
    (
        "badges",
        {
            "badge": "",
            "title": "¿Por qué elegirnos?",
            "subtitle": "",
            "items": [
                "Certificados ISO 27001",
                "Infraestructura SOC resiliente de nueva generación",
                "Equipo CSIRT",
                "Modelo OS3",
                "Miembro del MSSP Alert",
                "Manejo de soluciones multimarca",
                (
                    "Ingeniería propia local certificada en diferentes fabricantes y "
                    "estándares"
                ),
            ],
        },
    ),
    (
        "allies",
        {
            "badge": "",
            "title": "Nuestros Aliados",
            "subtitle": "Aliados que confían en nosotros",
            "items": ["Dell Technologies — Platinum Partner"],
        },
    ),
    (
        "cta",
        {
            "title": "Proteja su negocio hoy",
            "body": (
                "No espere a que sea demasiado tarde. Contáctenos hoy mismo para agendar "
                "una consulta gratuita y conocer cómo podemos apoyar a su organización "
                "frente a las amenazas cibernéticas más avanzadas."
            ),
            "cta_label": "Solicitar consulta gratuita",
            "cta_href": "/contacto/",
        },
    ),
]


def create_ciberseguridad(apps, schema_editor):
    from wagtail.models import Page

    from apps.home.models import SolucionPage, SolucionesIndexPage

    index = SolucionesIndexPage.objects.filter(slug="soluciones").first()
    if index is None:
        index = Page.objects.filter(slug="soluciones").first()
    if index is None or SolucionPage.objects.filter(slug="ciberseguridad").exists():
        return

    page = SolucionPage(
        title="Ciberseguridad",
        slug="ciberseguridad",
        body=BODY,
    )
    index.add_child(instance=page)
    page.save_revision().publish()


def remove_ciberseguridad(apps, schema_editor):
    from apps.home.models import SolucionPage

    SolucionPage.objects.filter(slug="ciberseguridad").delete()


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0013_alter_solucionpage_body"),
        ("wagtailsearch", "0010_add_text_fields"),
    ]

    operations = [
        migrations.RunPython(create_ciberseguridad, remove_ciberseguridad),
    ]
