"""Quita la cedula del representante legal de las politicas publicadas.

El documento del cliente incluye "C.C: 12.991.662 de San Juan (Pasto)" en la
firma. Es un dato personal de identificacion y no debe publicarse, asi que se
elimina del cuerpo de todas las paginas de politica (incluidas las ya creadas).
"""

import re

from django.db import migrations

# Tolerante a puntos/espacios variables y mayusculas.
CEDULA = re.compile(
    r"\s*C\.?\s*C\.?\s*:?\s*12[.\s]*991[.\s]*662\s*de\s*San\s*Juan\s*\(\s*Pasto\s*\)",
    re.IGNORECASE,
)


def _limpiar(texto: str) -> str:
    sin_cedula = CEDULA.sub("", texto)
    # Colapsa espacios dobles que deja el corte, sin tocar el HTML.
    return re.sub(r"[ \t]{2,}", " ", sin_cedula)


def quitar_cedula(apps, schema_editor):
    from apps.home.models import PoliticaPage

    for page in PoliticaPage.objects.all():
        body = page.body or ""
        limpio = _limpiar(body)
        if limpio != body:
            page.body = limpio
            page.save(update_fields=["body"])


class Migration(migrations.Migration):
    dependencies = [("home", "0042_create_terminos_condiciones")]

    operations = [
        migrations.RunPython(quitar_cedula, migrations.RunPython.noop),
    ]
