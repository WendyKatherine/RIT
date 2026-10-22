"""Ajustes globales del sitio, editables desde el admin de Wagtail.

No son contenido de una página (no viven en el árbol): son interruptores
globales. Wagtail los expone en Settings y quedan cacheados por request.
"""

from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting


@register_setting(icon="cog")
class SiteSettings(BaseSiteSetting):
    """Interruptores globales del sitio."""

    show_preloader = models.BooleanField(
        default=False,
        verbose_name="Mostrar preloader",
        help_text=(
            "Animación de carga al entrar al sitio. Dejalo apagado: compite "
            "visualmente con el popup de evento."
        ),
    )

    panels = [  # noqa: RUF012
        FieldPanel("show_preloader"),
    ]

    class Meta:
        verbose_name = "Ajustes del sitio"
