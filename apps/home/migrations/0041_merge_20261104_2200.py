"""Fusiona las dos ramas del grafo de migraciones de `home`.

Al mergear #32 (rama de Wendy, basada en main anterior) quedaron dos hojas:
`0037_remove_eventpopup_...` y `0040_add_index_listing_block`. Esta migración
vacía une ambas ramas para que `makemigrations --check` vuelva a estar limpio.
"""

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0037_remove_eventpopup_address_remove_eventpopup_city_and_more"),
        ("home", "0040_add_index_listing_block"),
    ]

    operations = []
