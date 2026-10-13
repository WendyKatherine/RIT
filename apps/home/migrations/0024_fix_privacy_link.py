"""Corrige el enlace de privacidad del formulario de contacto.

Antes apuntaba a `/politica-de-privacidad/` (página inexistente) → ahora apunta a la
política real de tratamiento de datos (`/politicas/tratamiento-datos/`).
"""
from django.db import migrations

OLD = "/politica-de-privacidad/"
NEW = "/politicas/tratamiento-datos/"


def _fix_body(body):
    changed = False
    for block in body:
        value = getattr(block, "value", None)
        if value is not None and "privacy_href" in value and value.get("privacy_href") == OLD:
            value["privacy_href"] = NEW
            changed = True
    return changed


def fix_privacy_links(apps, schema_editor):
    from apps.home.models import ContactoPage, HomePage

    for model in (ContactoPage, HomePage):
        for page in model.objects.all():
            body = page.body
            if _fix_body(body):
                page.body = body
                page.save_revision().publish()


def revert_privacy_links(apps, schema_editor):
    from apps.home.models import ContactoPage, HomePage

    for model in (ContactoPage, HomePage):
        for page in model.objects.all():
            body = page.body
            changed = False
            for block in body:
                value = getattr(block, "value", None)
                if (
                    value is not None
                    and "privacy_href" in value
                    and value.get("privacy_href") == NEW
                ):
                    value["privacy_href"] = OLD
                    changed = True
            if changed:
                page.body = body
                page.save_revision().publish()


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0023_create_politicas"),
    ]

    operations = [
        migrations.RunPython(fix_privacy_links, revert_privacy_links),
    ]
