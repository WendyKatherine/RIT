from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.models import Page

from apps.home.blocks import (
    CasesBlock,
    ContactBlock,
    CTABandBlock,
    HeroBlock,
    InteriorStatsBlock,
    MarqueeBlock,
    MissionVisionBlock,
    NosotrosBlock,
    PageHeroBlock,
    PartnersBlock,
    SectorsBlock,
    ServicesBlock,
    StatsBlock,
    StoryBlock,
    ValuesBlock,
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


class NosotrosPage(Page):
    """Página Nosotros — secciones editables vía StreamField.

    Contenido real de RIT (ver `nosotros.txt`) cargado por la migración de seed.
    Cada sección (hero, historia, números, sectores, misión/visión, valores, CTA)
    es un bloque editable desde el admin de Wagtail.
    """

    body = StreamField(
        [
            ("page_hero", PageHeroBlock()),
            ("story", StoryBlock()),
            ("stats", InteriorStatsBlock()),
            ("sectors", SectorsBlock()),
            ("mission_vision", MissionVisionBlock()),
            ("values", ValuesBlock()),
            ("cta", CTABandBlock()),
        ],
        blank=True,
        use_json_field=True,
    )

    # Lista declarativa de Wagtail (config, nunca se muta) — RUF012 es falso positivo aquí
    content_panels = [*Page.content_panels, FieldPanel("body")]  # noqa: RUF012

    max_count = 1

    template = "home/nosotros_page.html"

    class Meta:
        verbose_name = "Página Nosotros"
