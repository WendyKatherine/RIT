"""Crea la página Nosotros (bajo Home) y carga el contenido real.

Contenido según la spec `nosotros.txt` (RIT): quiénes somos, números
(+600 · +60 · +11 · +18), experiencia por sector, misión/visión, valores y CTA.
"""
from django.db import migrations

SEED_BODY = [
    (
        "page_hero",
        {
            "badge": "Nosotros",
            "title_pre": "Expertos en TI,",
            "title_hi": "aliados",
            "lead": (
                "A través de consultoría y asesoría simple pero especializada, ofrecemos a "
                "nuestros clientes soluciones de infraestructura tecnológica: consolidación, "
                "virtualización, respaldo y el mejor camino hacia la NUBE."
            ),
            "cta_label": "Conoce nuestras soluciones",
            "cta_href": "/soluciones/ciberseguridad/",
        },
    ),
    (
        "story",
        {
            "badge": "02 · Quiénes somos",
            "title_pre": "Consultoría simple,",
            "title_hi": "especializada",
            "paragraphs": [
                (
                    "RIT Enterprise Solutions es una empresa que, a través de consultoría y "
                    "asesoría simple pero especializada, ofrece a sus clientes soluciones de "
                    "infraestructura tecnológica, incluyendo consolidación, virtualización, "
                    "respaldo y el mejor camino hacia la NUBE."
                ),
                (
                    "En 11 años hemos realizado proyectos exitosos y continuamos creciendo. "
                    "Como Partner Directo de Dell, acompañamos a empresas de sectores como el "
                    "financiero, salud, oil & gas y educación, con más de 600 proyectos "
                    "ejecutados y 18 años de experiencia acumulada de nuestros ingenieros."
                ),
            ],
        },
    ),
    (
        "stats",
        {
            "badge": "03 · Números",
            "title": "Números que respaldan nuestra experiencia",
            "stats": [
                {"count": 600, "pre": "+", "post": "", "label": "Proyectos ejecutados"},
                {"count": 60, "pre": "+", "post": "", "label": "Clientes felices"},
                {"count": 11, "pre": "+", "post": "", "label": "Años como Partner Directo de DELL"},
                {
                    "count": 18,
                    "pre": "+",
                    "post": "",
                    "label": "Años de experiencia de nuestros ingenieros",
                },
            ],
        },
    ),
    (
        "sectors",
        {
            "badge": "04 · Experiencia por sector",
            "title": "Historias reales en las industrias que importan",
            "cards": [
                {
                    "num": "01",
                    "title": "Sector Financiero",
                    "tag": "Dell Latitude · OptiPlex · PowerEdge",
                    "points": [
                        (
                            "Más de 2.000 equipos portátiles Latitude y de escritorio OptiPlex "
                            "vendidos."
                        ),
                        (
                            "Más de 50 servidores PowerEdge y equipos de almacenamiento MD, "
                            "Compellent, Unity."
                        ),
                        (
                            "Plan de Continuidad de Negocio y DRP para una microfinanciera con "
                            "más de 60 oficinas a nivel nacional."
                        ),
                    ],
                },
                {
                    "num": "02",
                    "title": "Sector Salud",
                    "tag": "Dell Latitude · OptiPlex · PowerEdge",
                    "points": [
                        "Más de 2.000 equipos portátiles Latitude y de escritorio OptiPlex.",
                        (
                            "Más de 50 servidores PowerEdge y equipos de almacenamiento MD, "
                            "Compellent, Unity."
                        ),
                    ],
                },
                {
                    "num": "03",
                    "title": "Oil & Gas, Industria y Comercio",
                    "tag": "Dell Latitude · OptiPlex · PowerEdge",
                    "points": [
                        "Más de 500 equipos portátiles Latitude y de escritorio OptiPlex.",
                        (
                            "Más de 60 servidores PowerEdge y equipos de almacenamiento MD, "
                            "Compellent, Unity."
                        ),
                    ],
                },
                {
                    "num": "04",
                    "title": "Sector Educación",
                    "tag": "Dell Latitude · OptiPlex · PowerEdge",
                    "points": [
                        "Más de 200 equipos portátiles Latitude y de escritorio OptiPlex.",
                        (
                            "Más de 40 servidores PowerEdge y equipos de almacenamiento MD, "
                            "Compellent, Unity."
                        ),
                    ],
                },
            ],
        },
    ),
    (
        "mission_vision",
        {
            "badge": "05 · Misión y Visión",
            "title_pre": "Lo que",
            "title_hi": "nos mueve",
            "mission": (
                "Proveer a las empresas medianas y grandes de Colombia los productos, "
                "soluciones y servicios de TIC, incluyendo siempre en nuestra propuesta los "
                "más altos estándares de calidad, seriedad y servicio en los compromisos "
                "adquiridos con nuestros clientes."
            ),
            "vision": (
                "Convertirnos en líderes y expertos de referencia en tecnología de Centro de "
                "Datos y Servicios asociados a la optimización de la infraestructura de IT."
            ),
        },
    ),
    (
        "values",
        {
            "badge": "06 · Valores",
            "title": "Lo que nos mueve todos los días",
            "items": [
                {"title": "Calidad", "body": "En el trabajo que hacemos y presentamos a nuestros clientes."},
                {"title": "Comunicación", "body": "Clara hacia nuestros socios y hacia nuestros clientes."},
                {"title": "Honestidad", "body": "En cada una de nuestras actividades y escenarios."},
                {"title": "Responsabilidad", "body": "En cada una de las acciones y tareas que realizamos."},
                {"title": "Trabajo en equipo", "body": "Con involucramiento y entrega personalizada."},
                {"title": "Involucramiento", "body": "No participamos en los proyectos, nos involucramos."},
            ],
        },
    ),
    (
        "cta",
        {
            "title": "¿Necesita una consulta?",
            "body": (
                "Póngase en contacto con algunos de nuestros expertos o agentes. Estamos para "
                "ayudarlo."
            ),
            "cta_label": "Contáctenos ahora",
            "cta_href": "/contacto/",
        },
    ),
]


def create_nosotros(apps, schema_editor):
    from wagtail.models import Page

    from apps.home.models import NosotrosPage

    home = Page.objects.filter(slug="home").first()
    if home is None or NosotrosPage.objects.filter(slug="nosotros").exists():
        return
    page = NosotrosPage(title="Nosotros", slug="nosotros", body=SEED_BODY)
    home.add_child(instance=page)
    page.save_revision().publish()


def remove_nosotros(apps, schema_editor):
    from apps.home.models import NosotrosPage

    NosotrosPage.objects.filter(slug="nosotros").delete()


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0007_nosotrospage"),
        # El seed crea una página -> dispara el indexado de búsqueda de Wagtail;
        # garantizar que las tablas de wagtailsearch ya existan (BD nueva/tests).
        ("wagtailsearch", "0010_add_text_fields"),
    ]

    operations = [
        migrations.RunPython(create_nosotros, remove_nosotros),
    ]
