"""Actualiza los stats del Home con los datos reales del cliente.

El bloque de stats del Home tenía métricas viejas (7 años · 47% · 24/7 · 120); el
cliente confirmó los datos reales: +2000 proyectos · +120 clientes · +11 años
como Partner Directo de DELL · +10 años de experiencia de los ingenieros.
"""
from django.db import migrations

HOME_STATS = [
    {"count": 2000, "pre": "+", "post": "", "label": "Proyectos"},
    {"count": 120, "pre": "+", "post": "", "label": "Clientes felices"},
    {"count": 11, "pre": "+", "post": "", "label": "años como Partner Directo de DELL"},
    {"count": 10, "pre": "+", "post": "", "label": "años de experiencia de nuestros ingenieros"},
]


def apply(apps, schema_editor):
    from apps.home.models import HomePage

    home = HomePage.objects.first()
    if home is None:
        return
    body = home.body
    for block in body:
        if block.block_type == "stats":
            block.value["stats"] = HOME_STATS
    home.body = body
    home.save_revision().publish()


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0026_update_textos_cliente"),
    ]

    operations = [
        migrations.RunPython(apply, migrations.RunPython.noop),
    ]
