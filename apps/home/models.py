from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.models import Page

from apps.home.blocks import (
    CasesBlock,
    ContactBlock,
    HeroBlock,
    MarqueeBlock,
    NosotrosBlock,
    PartnersBlock,
    ServicesBlock,
    StatsBlock,
)


class HomePage(Page):
    """Página de inicio — secciones editables vía StreamField (mockup V1).

    Cada sección del mockup (hero, marquee, nosotros, servicios, aliados,
    resultados, casos, contacto) es un bloque que el cliente edita desde el
    admin de Wagtail. Contenido inicial cargado por la migración de seed.
    """

    body = StreamField(
        [
            ("hero", HeroBlock()),
            ("marquee", MarqueeBlock()),
            ("nosotros", NosotrosBlock()),
            ("services", ServicesBlock()),
            ("partners", PartnersBlock()),
            ("stats", StatsBlock()),
            ("cases", CasesBlock()),
            ("contact", ContactBlock()),
        ],
        blank=True,
        use_json_field=True,
    )

    # Lista declarativa de Wagtail (config, nunca se muta) — RUF012 es falso positivo aquí
    content_panels = [*Page.content_panels, FieldPanel("body")]  # noqa: RUF012

    max_count = 1

    class Meta:
        verbose_name = "Página de inicio"
