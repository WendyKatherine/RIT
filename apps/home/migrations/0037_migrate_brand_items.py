"""Convierte las marcas de aliados y del marquee al bloque con logo opcional.

Los datos viejos guardaban solo el nombre (string). El nuevo bloque espera
`{"name": ..., "logo": None}` para poder subir una imagen por marca sin perder
los logos estáticos que ya resuelve `marcas.py`.
"""

import json

from django.db import migrations


def _convert_item_value(value: object) -> object:
    if isinstance(value, str):
        return {"name": value, "logo": None}
    return value


def _convert_block(block: dict) -> bool:
    block_type = block.get("type")
    value = block.get("value")
    if not isinstance(value, dict):
        return False

    changed = False
    if block_type == "marquee":
        for item in value.get("items") or []:
            if isinstance(item, dict) and isinstance(item.get("value"), str):
                item["value"] = _convert_item_value(item["value"])
                changed = True
    elif block_type == "partners":
        for key in ("row_a", "row_b"):
            for item in value.get(key) or []:
                if isinstance(item, dict) and isinstance(item.get("value"), str):
                    item["value"] = _convert_item_value(item["value"])
                    changed = True
    return changed


def _convert_body(body: object) -> bool:
    changed = False
    for block in body or []:  # type: ignore[union-attr]
        if isinstance(block, dict) and _convert_block(block):
            changed = True
    return changed


def forwards(apps, schema_editor) -> None:
    connection = schema_editor.connection
    with connection.cursor() as cursor:
        cursor.execute("SELECT page_ptr_id, body FROM home_homepage")
        for page_id, body in cursor.fetchall():
            if isinstance(body, str):
                body = json.loads(body)
            if _convert_body(body):
                cursor.execute(
                    "UPDATE home_homepage SET body = %s::jsonb WHERE page_ptr_id = %s",
                    [json.dumps(body, ensure_ascii=False), page_id],
                )

        cursor.execute("SELECT id, content FROM wagtailcore_revision")
        for revision_id, content in cursor.fetchall():
            if isinstance(content, str):
                content = json.loads(content)
            if isinstance(content, dict) and _convert_body(content.get("body")):
                cursor.execute(
                    "UPDATE wagtailcore_revision SET content = %s::jsonb WHERE id = %s",
                    [json.dumps(content, ensure_ascii=False), revision_id],
                )


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0036_remove_eventpopup_dates_eventpopup_day_finish_and_more"),
    ]

    operations = [
        migrations.RunPython(forwards, migrations.RunPython.noop),
    ]
