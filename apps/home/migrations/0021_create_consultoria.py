"""Crea el índice /consultoria/ y las 4 páginas de Consultoría.

Contenido según los docs de `rit-paginas-web/consultoria/*.txt` (RIT).
"""
from django.db import migrations

INDEX_BODY = [
    (
        "page_hero",
        {
            "badge": "Consultoría",
            "title_pre": "Consultoría que",
            "title_hi": "impulsa decisiones",
            "lead": (
                "Arquitectura, continuidad de negocio, migraciones y plan estratégico de TI "
                "con consultores certificados."
            ),
            "cta_label": "",
            "cta_href": "",
        },
    ),
    (
        "cta",
        {
            "title": "¿Necesita una hoja de ruta de TI?",
            "body": "Le ayudamos a invertir en tecnología de forma inteligente y eficiente.",
            "cta_label": "Contáctenos",
            "cta_href": "/contacto/",
        },
    ),
]

ARQUITECTURA = [
    (
        "page_hero",
        {
            "badge": "Consultoría · Arquitectura e Integración",
            "title_pre": "Arquitectura e",
            "title_hi": "Integración",
            "lead": (
                "Asesoramos en la identificación, diseño e implementación de la plataforma "
                "de TI para su empresa, garantizando un manejo controlado de crecimiento, "
                "escalable y con vigencia tecnológica."
            ),
            "cta_label": "Solicitar asesoría",
            "cta_href": "/contacto/",
        },
    ),
    (
        "checklist",
        {
            "badge": "",
            "title": "Soluciones pensadas para el hoy y para el mañana",
            "items": [
                "Estudio de requerimientos y alcances del servicio.",
                "Recomendaciones a prácticas y plataformas.",
                "Actualización de las plataformas.",
                "Proyección de capacidad.",
                "Riesgos e impacto en la plataforma TI.",
                "Dimensionamiento e integración en los servicios.",
                "Exposición y propuestas de soluciones.",
                "Implementación de herramientas específicas para la plataforma TI.",
            ],
        },
    ),
    (
        "cta",
        {
            "title": "Diseñe la plataforma que su negocio necesita",
            "body": "Contáctenos para un estudio de su arquitectura actual.",
            "cta_label": "Contáctenos ahora",
            "cta_href": "/contacto/",
        },
    ),
]

CONTINUIDAD = [
    (
        "page_hero",
        {
            "badge": "Consultoría · Continuidad de Negocio",
            "title_pre": "Plan de Continuidad de Negocios (BCP) y",
            "title_hi": "Recuperación de Desastres (DRP)",
            "lead": (
                "Las empresas deben prepararse para enfrentar incidentes que interrumpan los "
                "negocios, minimizando el impacto y evitando la pérdida de ingresos, de "
                "información y la afectación de su reputación."
            ),
            "cta_label": "Solicitar asesoría",
            "cta_href": "/contacto/",
        },
    ),
    (
        "checklist",
        {
            "badge": "",
            "title": "Nuestras tareas",
            "items": [
                "Análisis de impacto al negocio por interrupción de actividades.",
                "Tiempos máximos de tolerancia (MTO) para cada actividad.",
                "Nivel mínimo de desempeño de cada actividad al reanudarse.",
                "Periodo para reanudar los niveles normales de funcionamiento.",
                "Componentes de continuidad implementados por terceros.",
                "Identificación de amenazas a la continuidad de las operaciones.",
                "Nivel de impacto y probabilidad de las amenazas.",
                "Matriz de riesgos de Continuidad del Negocio.",
                "Inventario de activos de información.",
                "Plan de Continuidad del Negocio BCP y DRP.",
                "Plan de Manejo de Crisis.",
                "Comunicados predefinidos por tipo de crisis.",
                "Articulación del Plan de Manejo de Crisis con BCP.",
                "Socialización de riesgos, modelo BCP y manejo de crisis.",
            ],
        },
    ),
    (
        "highlight",
        {
            "badge": "Destacado",
            "title": "Planes y procedimientos documentados para recuperación y restauración",
            "body": "",
            "bullets": [
                "Estructura de respuesta al incidente.",
                (
                    "Opciones de recuperación (DRP) para falla del centro de cómputo "
                    "primario hacia el alterno."
                ),
                (
                    "Procedimiento de auditoría al BCP, DRP y Plan de Seguridad de la "
                    "Información."
                ),
                "Campaña de cultura y sensibilización en BCP/DRP.",
                "Plan de pruebas y prueba al BCP/DRP.",
            ],
            "cta_label": "",
            "cta_href": "",
        },
    ),
    (
        "cta",
        {
            "title": "Su negocio preparado ante cualquier crisis",
            "body": "Contáctenos para elaborar su Plan de Continuidad de Negocio.",
            "cta_label": "Contáctenos ahora",
            "cta_href": "/contacto/",
        },
    ),
]

MIGRACIONES = [
    (
        "page_hero",
        {
            "badge": "Consultoría · Migraciones SAP",
            "title_pre": "Migraciones de Sistemas SAP y",
            "title_hi": "otras Aplicaciones",
            "lead": (
                "RIT cuenta con la experiencia para ayudar a nuestros clientes en "
                "migraciones de SAP y otras aplicaciones, evitando al máximo la "
                "indisponibilidad de sus servicios."
            ),
            "cta_label": "Solicitar asesoría",
            "cta_href": "/contacto/",
        },
    ),
    (
        "split_bullets",
        {
            "badge": "Destacado",
            "title": "Metodología",
            "intro": (
                "Utilizamos metodologías que requieren planificación y diseño para evitar "
                "al máximo la indisponibilidad de sus servicios."
            ),
            "items": [
                {
                    "title": "Planificación y diseño",
                    "body": "De la migración.",
                },
                {
                    "title": "Implementación y migración",
                    "body": "De datos y aplicaciones.",
                },
                {
                    "title": "Ingenieros con experiencia certificable",
                    "body": "Para la tranquilidad de nuestros clientes.",
                },
            ],
            "note": "",
        },
    ),
    (
        "cta",
        {
            "title": "Migre sin interrupciones",
            "body": "Contáctenos para planear la migración de sus sistemas.",
            "cta_label": "Contáctenos ahora",
            "cta_href": "/contacto/",
        },
    ),
]

PLAN = [
    (
        "page_hero",
        {
            "badge": "Consultoría · Plan Estratégico de TI",
            "title_pre": "Elaboración del",
            "title_hi": "Plan Estratégico de TI",
            "lead": (
                "Consultoría especializada que tiene en cuenta cada área o proceso de su "
                "organización, para que invierta en tecnología de forma inteligente y "
                "eficiente."
            ),
            "cta_label": "Solicitar asesoría",
            "cta_href": "/contacto/",
        },
    ),
    (
        "story",
        {
            "badge": "Metodología",
            "title_pre": "Diagnóstico con",
            "title_hi": "análisis de impacto (BIA)",
            "paragraphs": [
                (
                    "Realizamos un diagnóstico y análisis de impacto al negocio (BIA) a "
                    "través de entrevistas especializadas a los recursos representativos de "
                    "cada área, identificando los procesos, servicios y aplicativos a los "
                    "que debe prestar especial atención."
                ),
                (
                    "Con consultores certificados Technical Architect evaluamos su "
                    "infraestructura con LIVE OPTICS, herramienta de DELL para recolección "
                    "de datos. Evaluamos desempeño, arquitectura actual, cargas de trabajo y "
                    "aplicativos, y proponemos la estrategia óptima."
                ),
            ],
        },
    ),
    (
        "checklist",
        {
            "badge": "",
            "title": "Qué incluye nuestra consultoría",
            "items": [
                "Diagnóstico y análisis de impacto al negocio (BIA).",
                "Evaluación de infraestructura con Dell LIVE OPTICS.",
                "Arquitectura para su centro alterno de datos.",
                "Simulacros controlados (el centro alterno toma control de la operación).",
                "Estrategia para tiempos de recuperación y disponibilidad óptimos.",
            ],
        },
    ),
    (
        "cta",
        {
            "title": "Inversiones en tecnología inteligentes y eficientes",
            "body": "Contáctenos para un diagnóstico de su infraestructura de TI.",
            "cta_label": "Contáctenos ahora",
            "cta_href": "/contacto/",
        },
    ),
]

PAGES = [
    ("Arquitectura e Integración", "arquitectura-integracion", ARQUITECTURA),
    ("Continuidad de Negocio (BCP/DRP)", "continuidad-negocio", CONTINUIDAD),
    ("Migraciones SAP y otras Aplicaciones", "migraciones-sap", MIGRACIONES),
    ("Plan Estratégico de TI", "plan-estrategico", PLAN),
]


def create_consultoria(apps, schema_editor):
    from wagtail.models import Page

    from apps.home.models import InteriorPage, SeccionIndexPage

    home = Page.objects.filter(slug="home").first()
    if home is None:
        return

    index = SeccionIndexPage.objects.filter(slug="consultoria").first()
    if index is None:
        index = SeccionIndexPage(
            title="Consultoría", slug="consultoria", body=INDEX_BODY
        )
        home.add_child(instance=index)
        index.save_revision().publish()

    for title, slug, body in PAGES:
        if InteriorPage.objects.filter(slug=slug).exists():
            continue
        page = InteriorPage(title=title, slug=slug, body=body)
        index.add_child(instance=page)
        page.save_revision().publish()


def remove_consultoria(apps, schema_editor):
    from apps.home.models import InteriorPage, SeccionIndexPage

    for _title, slug, _body in PAGES:
        InteriorPage.objects.filter(slug=slug).delete()
    SeccionIndexPage.objects.filter(slug="consultoria").delete()


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0020_create_servicios"),
        ("wagtailsearch", "0010_add_text_fields"),
    ]

    operations = [
        migrations.RunPython(create_consultoria, remove_consultoria),
    ]
