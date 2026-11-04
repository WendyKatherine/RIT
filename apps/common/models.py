"""Ajustes globales del sitio, editables desde el admin de Wagtail.

No son contenido de una página (no viven en el árbol): son interruptores
globales. Wagtail los expone en Settings y quedan cacheados por request.
"""

from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting


@register_setting(icon="cog")
class SiteSettings(BaseSiteSetting):
    """Interruptores globales del sitio."""

    site_name = models.CharField(
        max_length=120,
        blank=True,
        default="",
        verbose_name="Nombre del sitio",
        help_text=(
            "Se usa en el título de las pestañas y en los metadatos. "
            "Vacío = RIT Enterprise Solutions."
        ),
    )

    show_preloader = models.BooleanField(
        default=False,
        verbose_name="Mostrar preloader",
        help_text=(
            "Animación de carga al entrar al sitio. Dejalo apagado: compite "
            "visualmente con el popup de evento."
        ),
    )

    panels = [  # noqa: RUF012
        FieldPanel("site_name"),
        FieldPanel("show_preloader"),
    ]

    class Meta:
        verbose_name = "Ajustes del sitio"


@register_setting(icon="site")
class FooterSettings(BaseSiteSetting):
    """Contenido editable del footer.

    Todos los campos son opcionales: si quedan vacíos, la plantilla usa el
    texto/valores actuales para que el sitio nunca se vea incompleto.
    """

    tagline = models.CharField(
        max_length=240,
        blank=True,
        default="",
        verbose_name="Frase del footer",
        help_text="Claim que aparece junto al logo. Vacío = texto actual.",
    )
    phone = models.CharField(
        max_length=40,
        blank=True,
        default="",
        verbose_name="Teléfono",
    )
    email = models.EmailField(
        blank=True,
        default="",
        verbose_name="Email",
    )
    address = models.CharField(
        max_length=200,
        blank=True,
        default="",
        verbose_name="Dirección",
    )
    facebook_url = models.URLField(
        blank=True,
        default="",
        verbose_name="Facebook",
        help_text="Si se deja vacío, el icono de Facebook no se muestra.",
    )
    linkedin_url = models.URLField(
        blank=True,
        default="",
        verbose_name="LinkedIn",
        help_text="Si se deja vacío, el icono de LinkedIn no se muestra.",
    )

    panels = [  # noqa: RUF012
        MultiFieldPanel(
            [
                FieldPanel("tagline"),
                FieldPanel("phone"),
                FieldPanel("email"),
                FieldPanel("address"),
            ],
            heading="Marca y contacto",
        ),
        MultiFieldPanel(
            [
                FieldPanel("facebook_url"),
                FieldPanel("linkedin_url"),
            ],
            heading="Redes sociales",
        ),
    ]

    class Meta:
        verbose_name = "Footer del sitio"
