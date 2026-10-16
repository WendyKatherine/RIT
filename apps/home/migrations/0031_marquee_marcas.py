"""Reemplaza el texto del marquee (slider tras el hero) por las marcas (logos)."""

from django.db import migrations

ITEMS = [
    "Dell",
    "Epson",
    "Logitech",
    "Microsoft",
    "Lenovo",
    "QNAP",
    "Samsung",
    "Ricoh",
    "Veeam",
    "Cisco",
    "HP",
]


def apply(apps, schema_editor):
    from apps.home.models import HomePage

    home = HomePage.objects.first()
    if home is None:
        return
    body = home.body
    for b in body:
        if b.block_type == "marquee":
            b.value["items"] = ITEMS
    home.body = body
    home.save_revision().publish()


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0030_alter_homepage_body"),
    ]

    operations = [
        migrations.RunPython(apply, migrations.RunPython.noop),
    ]
