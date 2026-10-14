"""Cambios de texto solicitados por el cliente (Wendy Gordo, carpeta SharePoint).

Solo TEXTO, sin cambios estructurales. Actualiza:
- Home: aliados (sección 04), casos de éxito (sección 05), lead del bloque nosotros.
- Nosotros: stats, experiencia por sector, misión/visión (05), valores (06 → 10).
- Contacto: horario.
- Ciberseguridad: aliado Dell (Platinum → Titanium).
"""
from django.db import migrations

MARCAS = [
    "Absolute", "Adata", "Adobe", "APC", "Apple", "Armor", "Aruba", "Asus", "Cisco",
    "Crucial", "Dell", "Eon", "Epson", "Fortinet", "Genius", "Grandstream", "Hikvision",
    "HP", "Hpe", "Jabra", "Kinston", "Kyocera", "Lenovo", "Leviton", "LG", "Linkedpro",
    "Logitech", "Microsoft", "Opentex", "Planet", "Plantronics", "Poly", "Powest", "QNAP",
    "Quest", "Red", "Ricoh", "Samsung", "Sandisk", "SAT", "Seagate", "Symantec", "Targus",
    "Toshiba", "Tplink", "Trust", "Veeam", "WD Green", "Western", "Xiaomi", "Xue", "Zkteco",
]

CASES_NEW = [
    {
        "tag": "FINANCIERO",
        "title": "Sector Financiero",
        "body": "Evertec · Grupo Mok · Rapicredit",
        "result": "",
    },
    {
        "tag": "SALUD",
        "title": "Sector Salud",
        "body": "Clinaltec · Hospital Manuel Uribe Ángel · Hospital Federico Lleras · Materialise",
        "result": "",
    },
    {
        "tag": "INDUSTRIAL · OIL & GAS",
        "title": "Industrial, Oil & Gas",
        "body": "Acerías Paz del Río · Diaco S.A. · Coquecol · Biomax",
        "result": "",
    },
    {
        "tag": "EDUCACIÓN",
        "title": "Sector Educación",
        "body": "Universidad Cesmag · Universidad de Boyacá · Universidad de Cartagena · Universidad de Nariño",
        "result": "",
    },
]

LEADS_NEW = [
    (
        "Somos un equipo compacto de profesionales altamente especializados. Once años "
        "operando en Colombia nos enseñaron que la infraestructura crítica no se delega a "
        "un proveedor cualquiera: se construye con gente que responde."
    ),
    (
        "En 2025 crecimos 54% en activos concentrándonos en lo que hacemos mejor: "
        "infraestructura, ciberseguridad y cloud, con estándares internacionales de "
        "seguridad y trato directo."
    ),
]

MISION_NEW = (
    "Proveer a empresas medianas y grandes en Colombia soluciones integrales de Tecnologías "
    "de la Información, Seguridad de la Información e Inteligencia Artificial, a través de "
    "servicios, productos y consultoría de alto valor, garantizando calidad, "
    "confidencialidad, integridad y disponibilidad de la información. Nos fundamentamos en "
    "el mejoramiento continuo de nuestros procesos, el cumplimiento de requisitos aplicables "
    "y la generación de valor para nuestros clientes, empleados, accionistas y demás partes "
    "interesadas, contribuyendo al desarrollo sostenible y a la transformación digital del "
    "entorno empresarial."
)

VISION_NEW = (
    "Convertirnos para el año 2029 en una organización líder y referente en soluciones de "
    "Centros de Datos y servicios asociados a la optimización de infraestructura de TI, "
    "reconocida por su innovación, excelencia operativa y generación de valor para sus "
    "clientes."
)

VALORES_NEW = [
    {
        "title": "Enfoque al cliente",
        "body": (
            "Orientamos nuestros procesos y decisiones a satisfacer los requisitos del "
            "cliente y aumentar su confianza, generando valor sostenible."
        ),
    },
    {
        "title": "Calidad y excelencia operativa",
        "body": (
            "Garantizamos la mejora continua de nuestros procesos, productos y servicios, "
            "cumpliendo con estándares de calidad y requisitos aplicables."
        ),
    },
    {
        "title": "Seguridad de la información",
        "body": (
            "Protegemos la confidencialidad, integridad y disponibilidad de la información, "
            "promoviendo el uso seguro y responsable de los datos y tecnologías."
        ),
    },
    {
        "title": "Bienestar y seguridad laboral",
        "body": (
            "Promovemos ambientes de trabajo seguros y saludables, previniendo lesiones, "
            "enfermedades laborales y riesgos en todas nuestras operaciones."
        ),
    },
    {
        "title": "Responsabilidad ambiental",
        "body": (
            "Gestionamos nuestros impactos ambientales de manera responsable, contribuyendo "
            "a la protección del entorno y al uso sostenible de los recursos."
        ),
    },
    {
        "title": "Cumplimiento legal y normativo",
        "body": (
            "Aseguramos el cumplimiento de los requisitos legales, reglamentarios y otros "
            "aplicables a nuestra organización."
        ),
    },
    {
        "title": "Mejora continua",
        "body": (
            "Impulsamos la optimización permanente de nuestros sistemas de gestión, procesos "
            "y desempeño organizacional."
        ),
    },
    {
        "title": "Gestión del riesgo",
        "body": (
            "Identificamos, evaluamos y controlamos los riesgos para garantizar la "
            "continuidad del negocio, la seguridad y la sostenibilidad."
        ),
    },
    {
        "title": "Innovación responsable",
        "body": (
            "Desarrollamos e implementamos soluciones tecnológicas e inteligencia artificial "
            "de manera ética, segura y confiable."
        ),
    },
    {
        "title": "Cultura organizacional y trabajo en equipo",
        "body": (
            "Fomentamos la participación, el compromiso y la colaboración de nuestros "
            "colaboradores como base del logro organizacional."
        ),
    },
]

SECTORS_NEW = {
    "Sector Financiero": [
        "Más de 2.000 equipos portátiles y de escritorio vendidos.",
        (
            "Plan de Continuidad de Negocio y DRP para una microfinanciera con más de 60 "
            "oficinas a nivel nacional."
        ),
    ],
    "Sector Salud": [
        "Más de 2.300 equipos de usuario final.",
        "Más de 50 servidores.",
    ],
    "Oil & Gas, Industria y Comercio": [
        "Más de 500 equipos.",
        "Más de 60 servidores y almacenamiento.",
    ],
    "Sector Educación": [
        "Más de 200 equipos portátiles y de escritorio.",
        "Más de 40 servidores y almacenamiento.",
    ],
}


def _upd_block(block):
    """Aplica los cambios de texto a un bloque (StreamChild) del body."""
    bt = block.block_type
    val = block.value
    if bt == "partners":
        val["row_a"] = MARCAS[:26]
        val["row_b"] = MARCAS[26:]
    elif bt == "cases":
        val["cases"] = CASES_NEW
    elif bt == "nosotros":
        val["leads"] = list(LEADS_NEW)
    elif bt == "stats":
        for s in val.get("stats", []):
            label = s.get("label", "")
            if label == "Proyectos ejecutados":
                s["count"] = 2000
            elif label == "Clientes felices":
                s["count"] = 120
            elif "experiencia de nuestros" in label:
                s["count"] = 10
    elif bt == "mission_vision":
        val["mission"] = MISION_NEW
        val["vision"] = VISION_NEW
    elif bt == "values":
        val["items"] = VALORES_NEW
    elif bt == "sectors":
        for card in val.get("cards", []):
            title = card.get("title", "")
            if title in SECTORS_NEW:
                card["points"] = SECTORS_NEW[title]
    elif bt == "contact_info":
        for c in val.get("cards", []):
            if c.get("k") == "Horario":
                c["v"] = "Lunes a Viernes · 8:00 AM – 5:30 PM"
    elif bt == "allies":
        items = val.get("items", [])
        if items and "Platinum" in items[0]:
            items[0] = "Dell Technologies — Titanium Partner"


def apply(apps, schema_editor):
    from apps.home.models import ContactoPage, HomePage, NosotrosPage, SolucionPage

    pages = [
        HomePage.objects.first(),
        NosotrosPage.objects.filter(slug="nosotros").first(),
        ContactoPage.objects.filter(slug="contacto").first(),
        SolucionPage.objects.filter(slug="ciberseguridad").first(),
    ]
    for page in pages:
        if page is None:
            continue
        body = page.body
        for block in body:
            _upd_block(block)
        page.body = body
        page.save_revision().publish()


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0025_alter_contactopage_body"),
    ]

    operations = [
        migrations.RunPython(apply, migrations.RunPython.noop),
    ]
