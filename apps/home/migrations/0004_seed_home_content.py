"""Seed de contenido de la Home (mockup V1 aprobado).

Carga en la HomePage los valores del front antiguo (data.py): hero, marquee,
nosotros, servicios, aliados, resultados, casos y contacto. Sin esta migración
la Home arranca vacía hasta que el cliente cargue contenido en el admin.
"""
from django.db import migrations

HERO_SLIDES = [
    {
        "pre": "Llevamos tu infraestructura al ",
        "hi": "siguiente nivel",
        "kicker": "Ciberseguridad, nube e infraestructura que protegen y aceleran tu negocio.",
        "index": "01",
        "sub": "Expertos colombianos con estándares internacionales. Diseñamos, protegemos y operamos tu base tecnológica.",
    },
    {
        "pre": "Seguridad que ",
        "hi": "no se negocia",
        "kicker": "Protección integral: auditorías, hardening, monitoreo 24/7 y respuesta a incidentes.",
        "index": "02",
        "sub": "Tu infraestructura crítica vigilada por especialistas que responden cuando importa.",
    },
    {
        "pre": "Cloud sin ",
        "hi": "fricción",
        "kicker": "Migración, arquitectura y operación en AWS, Azure y Huawei Cloud.",
        "index": "03",
        "sub": "Menos dolor de cabeza, más velocidad: migramos y operamos tu nube de principio a fin.",
    },
]

HERO_PILLS = ["7+ AÑOS", "+47% CRECIMIENTO", "SOPORTE 24/7"]

TECH_LOOP = [
    "MICROSOFT", "VMWARE", "CISCO", "HUAWEI CLOUD", "AWS",
    "AZURE", "PALO ALTO", "FORTINET", "ELASTIC", "SAP",
]

VALUE_CARDS = [
    {"num": "01", "title": "Seguridad primero", "body": "Protegemos cada capa de tu infraestructura.", "icon": "shield"},
    {"num": "02", "title": "Nube sin fricción", "body": "Migraciones y operación cloud sin dolores de cabeza.", "icon": "cloud"},
    {"num": "03", "title": "Infraestructura sólida", "body": "Diseño, implementación y soporte de redes y servidores.", "icon": "server"},
    {"num": "04", "title": "Acompañamiento real", "body": "Un equipo experto que responde cuando lo necesitas.", "icon": "chat"},
]

SERVICES = [
    {"n": "01", "tag": "INFRAESTRUCTURA", "title": "Infraestructura", "body": "Diseñamos, implementamos y operamos tu infraestructura tecnológica: redes, servidores, virtualización y storage.", "icon": "server"},
    {"n": "02", "tag": "CIBERSEGURIDAD", "title": "Ciberseguridad", "body": "Protegemos tu negocio: auditorías, hardening, monitoreo 24/7 y respuesta a incidentes.", "icon": "shield"},
    {"n": "03", "tag": "CLOUD", "title": "Cloud", "body": "Migración, arquitectura y operación en AWS, Azure y Huawei Cloud.", "icon": "cloud"},
    {"n": "04", "tag": "SOPORTE GESTIONADO", "title": "Soporte gestionado", "body": "Mesa de ayuda y administración proactiva de tu infraestructura.", "icon": "headset"},
]

PARTNERS_A = ["MICROSOFT", "VMWARE", "CISCO", "HUAWEI CLOUD", "AWS", "AZURE", "PALO ALTO", "FORTINET"]
PARTNERS_B = ["ELASTIC", "SAP", "DELL", "ORACLE", "IBM", "RED HAT", "SERVICENOW", "NUTANIX"]

STATS = [
    {"count": 7, "pre": "+", "post": "", "label": "Años de experiencia"},
    {"count": 47, "pre": "+", "post": "%", "label": "Crecimiento en activos · 2024"},
    {"count": 24, "pre": "", "post": "/7", "label": "Monitoreo y soporte"},
    {"count": 120, "pre": "", "post": "+", "label": "Proyectos entregados"},  # TODO: confirmar con RIT
]

CASES = [
    {"tag": "SALUD · MIGRACIÓN", "title": "Migración a la nube", "body": "Modernización de infraestructura para una red de clínicas: migración escalonada sin interrupciones del servicio.", "result": "-30% en costos de infraestructura"},
    {"tag": "FINANCIERO · SEGURIDAD", "title": "Ciberseguridad", "body": "Auditoría, hardening y monitoreo continuo para una entidad financiera.", "result": "Cero incidentes críticos en 12 meses"},
    {"tag": "MANUFACTURA · INFRAESTRUCTURA", "title": "Infraestructura", "body": "Rediseño de red y servidores para una planta de manufactura con operación 24/7.", "result": "99.9% de disponibilidad"},
]

CONTACT_ROWS = [
    {"k": "EMAIL", "v": "hola@ritenterprise.com.co"},  # TODO: confirmar con RIT
    {"k": "TELÉFONO", "v": "+57 1 234 5678"},  # TODO: confirmar con RIT
    {"k": "UBICACIÓN", "v": "Bogotá, Colombia"},
    {"k": "HORARIO", "v": "Lun – Vie · 8:00 am – 6:00 pm"},
]


def seed_home(apps, schema_editor):
    HomePage = apps.get_model("home", "HomePage")
    home = HomePage.objects.first()
    if home is None:
        return

    home.body = [
        ("hero", {"slides": HERO_SLIDES, "pills": HERO_PILLS}),
        ("marquee", {"items": TECH_LOOP}),
        (
            "nosotros",
            {
                "leads": [
                    "Somos un equipo compacto de 5 a 6 profesionales altamente especializados. Siete años operando en Colombia nos enseñaron que la infraestructura crítica no se delega a un proveedor cualquiera: se construye con gente que responde.",
                    "En 2024 crecimos 47% en activos concentrándonos en lo que hacemos mejor: infraestructura, ciberseguridad y cloud, con estándares internacionales y trato directo.",
                ],
                "cards": VALUE_CARDS,
            },
        ),
        ("services", {"cards": SERVICES}),
        ("partners", {"row_a": PARTNERS_A, "row_b": PARTNERS_B}),
        ("stats", {"stats": STATS}),
        ("cases", {"cases": CASES}),
        ("contact", {"rows": CONTACT_ROWS}),
    ]
    home.save()


def unseed_home(apps, schema_editor):
    HomePage = apps.get_model("home", "HomePage")
    home = HomePage.objects.first()
    if home is not None:
        home.body = []
        home.save()


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0003_homepage_body"),
    ]

    operations = [
        migrations.RunPython(seed_home, unseed_home),
    ]
