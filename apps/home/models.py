from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.models import Page

from apps.home.blocks import (
    AccordionBlock,
    AlliesBlock,
    BadgesBlock,
    CardsBlock,
    CasesBlock,
    ChecklistBlock,
    ContactBlock,
    ContactFormBlock,
    ContactInfoBlock,
    CTABandBlock,
    HeroBlock,
    HighlightBlock,
    InteriorStatsBlock,
    MapBlock,
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
    """Página de inicio — secciones editables vía StreamField (mockup V1)."""

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
    """Página Nosotros — secciones editables vía StreamField (contenido real RIT)."""

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


class ContactoPage(Page):
    """Página Contacto — secciones editables vía StreamField (contenido real RIT)."""

    body = StreamField(
        [
            ("page_hero", PageHeroBlock()),
            ("contact_info", ContactInfoBlock()),
            ("contact_form", ContactFormBlock()),
            ("map", MapBlock()),
            ("cta", CTABandBlock()),
        ],
        blank=True,
        use_json_field=True,
    )

    # Lista declarativa de Wagtail (config, nunca se muta) — RUF012 es falso positivo aquí
    content_panels = [*Page.content_panels, FieldPanel("body")]  # noqa: RUF012

    max_count = 1

    template = "home/contacto_page.html"

    class Meta:
        verbose_name = "Página Contacto"


class SolucionesIndexPage(Page):
    """Índice /soluciones/ — nodo padre (hub) de las páginas de solución."""

    body = StreamField(
        [
            ("page_hero", PageHeroBlock()),
            ("cta", CTABandBlock()),
        ],
        blank=True,
        use_json_field=True,
    )

    # Lista declarativa de Wagtail (config, nunca se muta) — RUF012 es falso positivo aquí
    content_panels = [*Page.content_panels, FieldPanel("body")]  # noqa: RUF012

    max_count = 1

    template = "home/soluciones_index.html"

    class Meta:
        verbose_name = "Índice de Soluciones"


class SolucionPage(Page):
    """Página de solución (hija de /soluciones/) — secciones editables vía StreamField."""

    body = StreamField(
        [
            ("page_hero", PageHeroBlock()),
            ("cards", CardsBlock()),
            ("checklist", ChecklistBlock()),
            ("accordion", AccordionBlock()),
            ("highlight", HighlightBlock()),
            ("badges", BadgesBlock()),
            ("allies", AlliesBlock()),
            ("cta", CTABandBlock()),
        ],
        blank=True,
        use_json_field=True,
    )

    # Lista declarativa de Wagtail (config, nunca se muta) — RUF012 es falso positivo aquí
    content_panels = [*Page.content_panels, FieldPanel("body")]  # noqa: RUF012

    template = "home/solucion_page.html"

    class Meta:
        verbose_name = "Página de Solución"
