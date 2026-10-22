from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Page
from wagtail.snippets.models import register_snippet

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
    QuoteBlock,
    SectorsBlock,
    ServicesBlock,
    SplitBulletsBlock,
    StatsBlock,
    StoryBlock,
    TabsBlock,
    TimelineBlock,
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
            ("story", StoryBlock()),
            ("cards", CardsBlock()),
            ("checklist", ChecklistBlock()),
            ("accordion", AccordionBlock()),
            ("highlight", HighlightBlock()),
            ("badges", BadgesBlock()),
            ("allies", AlliesBlock()),
            ("timeline", TimelineBlock()),
            ("split_bullets", SplitBulletsBlock()),
            ("quote", QuoteBlock()),
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


class SeccionIndexPage(Page):
    """Índice de sección (/productos/, /servicios/, /consultoria/) — hub con lista de hijos."""

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

    template = "home/seccion_index.html"

    class Meta:
        verbose_name = "Índice de sección"


class InteriorPage(Page):
    """Página interior genérica (Productos / Servicios / Consultoría)."""

    body = StreamField(
        [
            ("page_hero", PageHeroBlock()),
            ("story", StoryBlock()),
            ("cards", CardsBlock()),
            ("tabs", TabsBlock()),
            ("checklist", ChecklistBlock()),
            ("accordion", AccordionBlock()),
            ("highlight", HighlightBlock()),
            ("badges", BadgesBlock()),
            ("allies", AlliesBlock()),
            ("timeline", TimelineBlock()),
            ("split_bullets", SplitBulletsBlock()),
            ("quote", QuoteBlock()),
            ("cta", CTABandBlock()),
        ],
        blank=True,
        use_json_field=True,
    )

    # Lista declarativa de Wagtail (config, nunca se muta) — RUF012 es falso positivo aquí
    content_panels = [*Page.content_panels, FieldPanel("body")]  # noqa: RUF012

    template = "home/interior_page.html"

    class Meta:
        verbose_name = "Página interior"


class PoliticaPage(Page):
    """Documento legal (política) — página independiente enlazada desde el footer."""

    codigo = models.CharField(blank=True, max_length=40, verbose_name="Código")
    version_doc = models.CharField(blank=True, max_length=10, verbose_name="Versión")
    fecha_doc = models.CharField(blank=True, max_length=40, verbose_name="Fecha")

    body = RichTextField(blank=True, verbose_name="Contenido")

    # Lista declarativa de Wagtail (config, nunca se muta) — RUF012 es falso positivo aquí
    content_panels = [  # noqa: RUF012
        *Page.content_panels,
        MultiFieldPanel(
            [FieldPanel("codigo"), FieldPanel("version_doc"), FieldPanel("fecha_doc")],
            heading="Documento",
        ),
        FieldPanel("body"),
    ]

    template = "home/politica_page.html"

    class Meta:
        verbose_name = "Página de Política"


@register_snippet
class EventPopup(models.Model):
    """Popup de evento — se muestra una vez por sesión."""

    title = models.CharField(max_length=120, verbose_name="Nombre interno")
    subtitle = models.CharField(max_length=120, blank=True, default="", verbose_name="Subtítulo")
    title_tag_line = models.CharField(
        max_length=120, blank=True, default="", verbose_name="Tagline"
    )
    tag_1 = models.CharField(max_length=60, blank=True, default="", verbose_name="Tag 1")
    tag_2 = models.CharField(max_length=60, blank=True, default="", verbose_name="Tag 2")
    tag_3 = models.CharField(max_length=60, blank=True, default="", verbose_name="Tag 3")
    is_active = models.BooleanField(default=True)
    logo = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    day_start = models.CharField(max_length=20, blank=True, default="", verbose_name="Día inicial")
    day_finish = models.CharField(max_length=20, blank=True, default="", verbose_name="Día final")
    month = models.CharField(max_length=40, blank=True, default="", verbose_name="Mes")
    place = models.CharField(max_length=120, verbose_name="Lugar")
    address = models.CharField(max_length=160, verbose_name="Dirección")
    map_url = models.URLField(blank=True, verbose_name="URL de ubicación")
    city = models.CharField(max_length=80, verbose_name="Ciudad")
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    partner_logo = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    foot_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        verbose_name="Imagen del pie",
        on_delete=models.SET_NULL,
        related_name="+",
    )
    site_url = models.CharField(max_length=120, default="www.ritenterprise.com.co")

    panels = [  # noqa: RUF012
        FieldPanel("title"),
        FieldPanel("subtitle"),
        FieldPanel("title_tag_line"),
        FieldPanel("tag_1"),
        FieldPanel("tag_2"),
        FieldPanel("tag_3"),
        FieldPanel("is_active"),
        FieldPanel("logo"),
        FieldPanel("day_start"),
        FieldPanel("day_finish"),
        FieldPanel("month"),
        FieldPanel("place"),
        FieldPanel("address"),
        FieldPanel("map_url"),
        FieldPanel("city"),
        FieldPanel("image"),
        FieldPanel("partner_logo"),
        FieldPanel("foot_image"),
        FieldPanel("site_url"),
    ]

    class Meta:
        verbose_name = "Popup de evento"
        verbose_name_plural = "Popups de evento"
