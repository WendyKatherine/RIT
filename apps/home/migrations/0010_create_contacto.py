"""Crea la página Contacto (bajo Home) y carga el contenido real.

Contenido según la spec `contacto.txt` (RIT): datos de contacto reales, PQR
(Forms de Microsoft), formulario (maqueta), mapa y CTA.
"""
from django.db import migrations

PQR_URL = (
    "https://forms.cloud.microsoft/pages/responsepage.aspx"
    "?id=30wyaGggOUutVwtxV3wlVyKOaXt8lEJFi12RgBVYUWhUN0FRUVJXTU4zVVUzWkJUNDNZSzNPVTlSRS4u"
    "&route=shorturl"
)

SEED_BODY = [
    (
        "page_hero",
        {
            "badge": "Contacto",
            "title_pre": "Hable con un",
            "title_hi": "experto",
            "lead": "Gracias por creer en el poder de la transformación tecnológica.",
            "cta_label": "",
            "cta_href": "",
        },
    ),
    (
        "contact_info",
        {
            "badge": "Nuestro contacto",
            "title": "Estamos para ayudarte",
            "cards": [
                {"k": "Oficina", "v": "AV Kra 9 # 115-06 OF 1207, Edif. Tierra Firme, Bogotá", "href": ""},
                {"k": "Email", "v": "info@ritenterprise.com.co", "href": "mailto:info@ritenterprise.com.co"},
                {"k": "Teléfono", "v": "+57 317 5073040", "href": "tel:+573175073040"},
                {"k": "Horario", "v": "Lunes a Viernes · 8:00 AM – 6:00 PM", "href": ""},
                {"k": "Redes", "v": "LinkedIn", "href": "https://www.linkedin.com/"},
                {"k": "PQR", "v": "Formulario de peticiones, quejas y reclamos", "href": PQR_URL},
            ],
        },
    ),
    (
        "contact_form",
        {
            "badge": "Escríbenos",
            "title": "Cuéntanos tu reto",
            "note": "Autorizo el tratamiento de mis datos personales según la",
            "privacy_href": "/politica-de-privacidad/",
        },
    ),
    (
        "map",
        {
            "title": "Cómo llegar",
            "query": "AV Kra 9 # 115-06, Bogotá, Colombia",
        },
    ),
    (
        "cta",
        {
            "title": "¡Estamos para ayudarte!",
            "body": "Te respondemos en menos de 24 horas hábiles.",
            "cta_label": "Escríbenos",
            "cta_href": "mailto:info@ritenterprise.com.co",
        },
    ),
]


def create_contacto(apps, schema_editor):
    from wagtail.models import Page

    from apps.home.models import ContactoPage

    home = Page.objects.filter(slug="home").first()
    if home is None or ContactoPage.objects.filter(slug="contacto").exists():
        return
    page = ContactoPage(title="Contacto", slug="contacto", body=SEED_BODY)
    home.add_child(instance=page)
    page.save_revision().publish()


def remove_contacto(apps, schema_editor):
    from apps.home.models import ContactoPage

    ContactoPage.objects.filter(slug="contacto").delete()


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0009_contactopage"),
        # El seed crea una página -> dispara el indexado de búsqueda de Wagtail.
        ("wagtailsearch", "0010_add_text_fields"),
    ]

    operations = [
        migrations.RunPython(create_contacto, remove_contacto),
    ]
