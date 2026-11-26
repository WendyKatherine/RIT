"""Pulido de las paginas de politica: firma, guiones y negritas legales.

- Quita las lineas de guiones bajos usadas como linea de firma.
- Envuelve la firma del representante legal en un bloque `.doc-firma`.
- Pone en negrita las referencias normativas (Ley/Decreto/Resolucion ... de AAAA).
Es idempotente: si el cuerpo ya esta limpio, no lo toca.
"""

import re

from django.db import migrations

GUIONES = re.compile(r"_{5,}")
ESPACIOS = re.compile(r"[ \t]{2,}")
FIRMA = re.compile(
    r"(JUAN\s+ALVARO\s+ROJAS)\s*(Representante\s+Legal\s+Gerente\s+General)",
    re.IGNORECASE,
)
NORMAS = re.compile(
    r"(?<!<strong>)\b(Ley|Decreto|Resoluci[oó]n|Acuerdo)\s+\d{1,4}\s+de\s+\d{4}(?!</strong>)",
    re.IGNORECASE,
)


def _pulir(body: str) -> str:
    texto = GUIONES.sub(" ", body)
    texto = ESPACIOS.sub(" ", texto)
    texto = FIRMA.sub(
        r'<span class="doc-firma"><strong>\1</strong><br>\2</span>',
        texto,
    )
    texto = NORMAS.sub(r"<strong>\1</strong>", texto)
    return texto


def pulir_politicas(apps, schema_editor):
    from apps.home.models import PoliticaPage

    for page in PoliticaPage.objects.all():
        body = page.body or ""
        nuevo = _pulir(body)
        if nuevo != body:
            page.body = nuevo
            page.save(update_fields=["body"])


class Migration(migrations.Migration):
    dependencies = [("home", "0043_quitar_cedula_politicas")]

    operations = [
        migrations.RunPython(pulir_politicas, migrations.RunPython.noop),
    ]
