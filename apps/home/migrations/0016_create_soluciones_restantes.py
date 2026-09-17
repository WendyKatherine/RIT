"""Crea las 3 páginas de Soluciones restantes (bajo /soluciones/).

- Comunicaciones Avanzadas
- Espacios de Trabajo Inteligentes
- Digitalización de Procesos de Negocio

Contenido según los docs de `soluciones/*.txt` (RIT).
"""
from django.db import migrations

COMUNICACIONES = [
    (
        "page_hero",
        {
            "badge": "Soluciones · Comunicaciones Avanzadas",
            "title_pre": "Transformamos la forma en que tu empresa",
            "title_hi": "se conecta, comunica y crece",
            "lead": "Comunicaciones y espacios inteligentes con IA.",
            "cta_label": "Cotizar ahora",
            "cta_href": "/contacto/",
        },
    ),
    (
        "cards",
        {
            "badge": "",
            "title": "",
            "intro": (
                "Integramos plataformas como Dialvox con soluciones de IA que automatizan "
                "centros de contacto, analizan conversaciones y mejoran la experiencia del "
                "usuario. Además diseñamos salas inteligentes con audio, video, pantallas "
                "interactivas y control automatizado."
            ),
            "cards": [
                {
                    "badge": "",
                    "icon": "headset",
                    "title": "Todo en uno",
                    "body": "Voicebot, Chatbot, PBX y Contact Center en una sola plataforma.",
                    "cta_label": "",
                    "cta_href": "",
                },
                {
                    "badge": "",
                    "icon": "shield",
                    "title": "Seguridad",
                    "body": "Comunicaciones cifradas y 100% confiables.",
                    "cta_label": "",
                    "cta_href": "",
                },
                {
                    "badge": "",
                    "icon": "cloud",
                    "title": "Escalabilidad",
                    "body": "Crece con tu empresa sin inversiones extras.",
                    "cta_label": "",
                    "cta_href": "",
                },
                {
                    "badge": "",
                    "icon": "chat",
                    "title": "Soporte técnico",
                    "body": "Asistencia experta, siempre que la necesites.",
                    "cta_label": "",
                    "cta_href": "",
                },
                {
                    "badge": "",
                    "icon": "cloud",
                    "title": "En la nube",
                    "body": "Infraestructura cloud, disponible en todo momento.",
                    "cta_label": "",
                    "cta_href": "",
                },
                {
                    "badge": "",
                    "icon": "server",
                    "title": "Automatización",
                    "body": "IA que atiende, entiende y mejora la experiencia.",
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
            "title": "Servicios avanzados que ofrece Dialvox",
            "intro": "",
            "cards": [
                {
                    "badge": "",
                    "icon": "headset",
                    "title": "Dialvox Voicebot",
                    "body": (
                        "IA conversacional en llamadas entrantes y salientes. Habla con "
                        "lenguaje natural y reproduce voz en diferentes idiomas y acentos."
                    ),
                    "cta_label": "",
                    "cta_href": "",
                },
                {
                    "badge": "",
                    "icon": "chat",
                    "title": "Dialvox Chatbot",
                    "body": (
                        "Automatiza la atención en canales digitales y redes sociales con "
                        "IA humanizada. Escala a un agente cuando es necesario."
                    ),
                    "cta_label": "",
                    "cta_href": "",
                },
                {
                    "badge": "",
                    "icon": "cloud",
                    "title": "Dialvox PBX",
                    "body": (
                        "Centraliza llamadas, video y UC. Integra IVR transaccional 24/7 y "
                        "compatibilidad con Microsoft Teams."
                    ),
                    "cta_label": "",
                    "cta_href": "",
                },
                {
                    "badge": "",
                    "icon": "headset",
                    "title": "Dialvox Contact Center",
                    "body": (
                        "Enrutamiento avanzado, reportes en tiempo real y marcación "
                        "Predictivo y Preview."
                    ),
                    "cta_label": "",
                    "cta_href": "",
                },
            ],
        },
    ),
    (
        "timeline",
        {
            "badge": "",
            "title": "Cómo se integran todos los servicios en una sola plataforma",
            "steps": [
                {"title": "Dialvox unifica canales y orquesta la comunicación con IA", "body": ""},
                {"title": "PBX gestiona llamadas entrantes de forma segura y escalable", "body": ""},
                {
                    "title": (
                        "IVR transaccional enruta solicitudes y conecta con sus sistemas 24/7"
                    ),
                    "body": "",
                },
                {
                    "title": (
                        "Voicebot y Chatbot atienden con lenguaje natural y escalan a agente"
                    ),
                    "body": "",
                },
                {"title": "Contact Center coordina atención, ventas y cobranzas", "body": ""},
            ],
        },
    ),
    (
        "split_bullets",
        {
            "badge": "",
            "title": "Salas inteligentes que impulsan la colaboración",
            "intro": "",
            "items": [
                {
                    "title": "Experiencia audiovisual inmersiva",
                    "body": (
                        "Sonido profesional, pantallas interactivas y videoproyección de "
                        "alta calidad."
                    ),
                },
                {
                    "title": "Control y automatización total",
                    "body": (
                        "Gestiona audio, video, iluminación y climatización desde un solo "
                        "dispositivo."
                    ),
                },
                {
                    "title": "Conectadas con tu negocio",
                    "body": "Compatibles con tus plataformas de videoconferencia.",
                },
                {
                    "title": "Diseño a la medida",
                    "body": "Salas ejecutivas, auditorios, formación y entornos híbridos.",
                },
            ],
            "note": (
                "Respaldo de marcas líderes: Hikvision, Jabra, Cisco, ScreenBeam, Orbys, "
                "i3, Shure, QSC y más."
            ),
        },
    ),
    (
        "cta",
        {
            "title": "Siempre contigo — un equipo humano para respaldar tu tecnología",
            "body": "Asistencia 24/7, mantenimiento preventivo y capacitación continua.",
            "cta_label": "Contáctenos ahora",
            "cta_href": "/contacto/",
        },
    ),
]

ESPACIOS = [
    (
        "page_hero",
        {
            "badge": "Soluciones · Espacios de Trabajo Inteligentes",
            "title_pre": "Transforma tu trabajo con",
            "title_hi": "tecnología del futuro",
            "lead": "Productividad, colaboración y DaaS para equipos que quieren trabajar mejor.",
            "cta_label": "Cotizar ahora",
            "cta_href": "/contacto/",
        },
    ),
    (
        "cards",
        {
            "badge": "",
            "title": "Integra Hardware y Software",
            "intro": "",
            "cards": [
                {
                    "badge": "",
                    "icon": "server",
                    "title": "Equipos de Cómputo",
                    "body": "Soluciones para mejorar la experiencia del usuario final.",
                    "cta_label": "",
                    "cta_href": "",
                },
                {
                    "badge": "",
                    "icon": "headset",
                    "title": "Audio, video y periféricos",
                    "body": "Periféricos ergonómicos que facilitan la colaboración.",
                    "cta_label": "",
                    "cta_href": "",
                },
                {
                    "badge": "",
                    "icon": "server",
                    "title": "Mobiliario",
                    "body": "Entornos de trabajo cómodos, eficientes y saludables.",
                    "cta_label": "",
                    "cta_href": "",
                },
                {
                    "badge": "",
                    "icon": "cloud",
                    "title": "Software de productividad",
                    "body": "Microsoft 365 y videoconferencia integrados.",
                    "cta_label": "",
                    "cta_href": "",
                },
                {
                    "badge": "",
                    "icon": "shield",
                    "title": "Seguridad para Endpoint",
                    "body": "Protección contra amenazas y cumplimiento normativo.",
                    "cta_label": "",
                    "cta_href": "",
                },
                {
                    "badge": "",
                    "icon": "cloud",
                    "title": "Software de Backup",
                    "body": "Seguridad y disponibilidad de sus datos.",
                    "cta_label": "",
                    "cta_href": "",
                },
                {
                    "badge": "",
                    "icon": "headset",
                    "title": "Implementación, Soporte y Mesa de Ayuda",
                    "body": "Soporte continuo y servicios gestionados.",
                    "cta_label": "",
                    "cta_href": "",
                },
            ],
        },
    ),
    (
        "highlight",
        {
            "badge": "DaaS — Device As A Service",
            "title": "Integra Hardware y Software en un único modelo mensual",
            "body": (
                "El modelo de Dispositivo como Servicio (DaaS) integra hardware, software "
                "y soporte en una única factura, simplificando su gestión operativa y "
                "tecnológica."
            ),
            "bullets": [
                "Todo en una Suscripción — Hardware, software y servicios en una única factura.",
                "Cobertura Total — Garantía de hasta 5 años, reemplazo rápido y soporte 24/7.",
            ],
            "cta_label": "Contáctenos",
            "cta_href": "/contacto/",
        },
    ),
    (
        "cta",
        {
            "title": "Su equipo siempre productivo y enfocado",
            "body": "Hablemos de cómo equipar su organización de principio a fin.",
            "cta_label": "Solicitar asesoría",
            "cta_href": "/contacto/",
        },
    ),
]

DIGITALIZACION = [
    (
        "page_hero",
        {
            "badge": "Soluciones · Digitalización de Procesos",
            "title_pre": "Digitalización de",
            "title_hi": "Procesos de Negocio",
            "lead": (
                "Su organización ya tiene los datos. El problema es que no están "
                "conectados, no son confiables y no se usan para decidir. Nosotros "
                "resolvemos exactamente eso."
            ),
            "cta_label": "Hablar con un experto",
            "cta_href": "/contacto/",
        },
    ),
    (
        "quote",
        {
            "badge": "Propósito",
            "text": (
                "Orquestamos Ecosistemas Digitales Inteligentes para incrementar la "
                "productividad, acelerar la toma de decisiones basadas en datos confiables "
                "y convertir la Inteligencia Artificial en resultados reales para el "
                "negocio."
            ),
        },
    ),
    (
        "story",
        {
            "badge": "El reto",
            "title_pre": "La mayoría de las organizaciones tienen datos. Pocas los usan para",
            "title_hi": "crecer",
            "paragraphs": [
                (
                    "No abordar la automatización de procesos soportada en datos confiables "
                    "no solo limita el crecimiento — condena a la operación a volverse cada "
                    "vez más lenta y costosa."
                ),
            ],
        },
    ),
    (
        "cards",
        {
            "badge": "",
            "title": "Cómo convertimos su operación en una operación inteligente",
            "intro": (
                "Un ecosistema que acompaña a su organización desde el diagnóstico hasta "
                "la operación continua con inteligencia artificial."
            ),
            "cards": [
                {
                    "badge": "Consultoría de",
                    "icon": "server",
                    "title": "Gobierno de Datos",
                    "body": (
                        "Evaluamos el estado de sus datos, identificamos silos, "
                        "duplicidades y brechas de calidad. Diseñamos un marco de gobierno "
                        "que garantiza información confiable, accesible y segura desde el "
                        "origen."
                    ),
                    "cta_label": "",
                    "cta_href": "",
                },
                {
                    "badge": "Automatización",
                    "icon": "cloud",
                    "title": "De Procesos",
                    "body": (
                        "Implementamos automatización con RPA, integración de sistemas y "
                        "orquestación de flujos. Eliminamos tareas manuales repetitivas y "
                        "reducimos errores."
                    ),
                    "cta_label": "",
                    "cta_href": "",
                },
                {
                    "badge": "Operación",
                    "icon": "chat",
                    "title": "Continua con IA",
                    "body": (
                        "Desplegamos modelos de IA y analítica avanzada para generar "
                        "insights predictivos, alertas tempranas y recomendaciones "
                        "automatizadas."
                    ),
                    "cta_label": "",
                    "cta_href": "",
                },
            ],
        },
    ),
    (
        "cta",
        {
            "title": "¿Sus datos están trabajando para su negocio?",
            "body": (
                "Si la respuesta genera duda, es el momento de actuar. Agendemos una "
                "conversación."
            ),
            "cta_label": "Solicitar evaluación gratuita",
            "cta_href": "/contacto/",
        },
    ),
]

PAGES = [
    ("Comunicaciones Avanzadas", "comunicaciones-avanzadas", COMUNICACIONES),
    ("Espacios de Trabajo Inteligentes", "espacios-de-trabajo", ESPACIOS),
    ("Digitalización de Procesos de Negocio", "digitalizacion-procesos", DIGITALIZACION),
]


def create_restantes(apps, schema_editor):
    from wagtail.models import Page

    from apps.home.models import SolucionPage, SolucionesIndexPage

    index = SolucionesIndexPage.objects.filter(slug="soluciones").first()
    if index is None:
        index = Page.objects.filter(slug="soluciones").first()
    if index is None:
        return

    for title, slug, body in PAGES:
        if SolucionPage.objects.filter(slug=slug).exists():
            continue
        page = SolucionPage(title=title, slug=slug, body=body)
        index.add_child(instance=page)
        page.save_revision().publish()


def remove_restantes(apps, schema_editor):
    from apps.home.models import SolucionPage

    for _title, slug, _body in PAGES:
        SolucionPage.objects.filter(slug=slug).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0015_alter_solucionpage_body"),
        ("wagtailsearch", "0010_add_text_fields"),
    ]

    operations = [
        migrations.RunPython(create_restantes, remove_restantes),
    ]
