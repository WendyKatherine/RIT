"""Agrega el bloque editable del listado a la página /soluciones/.

La sección del listado estaba hardcodeada en la plantilla. Ahora es un bloque
StreamField; esta migración lo inserta al inicio del cuerpo existente para que
el editor pueda cambiar la etiqueta y el título sin perder el listado.
"""

import json
import uuid

from django.db import migrations

LISTING_BLOCK = {
    "type": "index_listing",
    "value": {"badge": "Soluciones", "title": "Nuestras soluciones"},
}


def _has_listing(body: object) -> bool:
    return any(
        isinstance(block, dict) and block.get("type") == "index_listing"
        for block in body or []  # type: ignore[union-attr]
    )


def _add_listing(body: object) -> bool:
    if not isinstance(body, list):
        return False
    if _has_listing(body):
        return False
    block = dict(LISTING_BLOCK)
    block["id"] = str(uuid.uuid4())
    body.insert(0, block)
    return True


def forwards(apps, schema_editor) -> None:
    connection = schema_editor.connection
    with connection.cursor() as cursor:
        cursor.execute("SELECT page_ptr_id, body FROM home_solucionesindexpage")
        for page_id, body in cursor.fetchall():
            if isinstance(body, str):
                body = json.loads(body)
            if _add_listing(body):
                cursor.execute(
                    "UPDATE home_solucionesindexpage SET body = %s::jsonb WHERE page_ptr_id = %s",
                    [json.dumps(body, ensure_ascii=False), page_id],
                )

        cursor.execute(
            "SELECT id FROM django_content_type WHERE app_label = %s AND model = %s",
            ["home", "solucionesindexpage"],
        )
        row = cursor.fetchone()
        if row is None:
            return
        content_type_id = row[0]

        cursor.execute(
            "SELECT id, content FROM wagtailcore_revision WHERE content_type_id = %s",
            [content_type_id],
        )
        for revision_id, content in cursor.fetchall():
            if isinstance(content, str):
                content = json.loads(content)
            if not isinstance(content, dict):
                continue
            body = content.get("body")
            if isinstance(body, str):
                body = json.loads(body)
            if _add_listing(body):
                content["body"] = body
                cursor.execute(
                    "UPDATE wagtailcore_revision SET content = %s::jsonb WHERE id = %s",
                    [json.dumps(content, ensure_ascii=False), revision_id],
                )


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0039_remove_solucionesindexpage_index_badge_and_more"),
    ]

    operations = [
        migrations.RunPython(forwards, migrations.RunPython.noop),
    ]
