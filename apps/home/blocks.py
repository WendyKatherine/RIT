"""Bloques StreamField de la Home — secciones editables del mockup V1.

Cada bloque corresponde a una sección del Home aprobado por el cliente.
Los valores por defecto (seed) se cargan desde la migración de datos
0003_seed_home_content, con el contenido del front antiguo (data.py).
"""

from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class HeroSlideBlock(blocks.StructBlock):
    pre = blocks.CharBlock(help_text="Texto antes del highlight (gradiente)")
    hi = blocks.CharBlock(help_text="Texto resaltado con gradiente")
    kicker = blocks.TextBlock(help_text="Frase corta bajo el título")
    index = blocks.CharBlock(default="01", help_text="Índice del slide (01, 02…)")
    sub = blocks.TextBlock(help_text="Párrafo lateral del slide")
    image = ImageChooserBlock(
        required=False,
        help_text="Foto de fondo (eventos, sede, equipo…). Si no hay, se ve el fondo de marca.",
    )


class HeroBlock(blocks.StructBlock):
    slides = blocks.ListBlock(HeroSlideBlock(), min_num=1)
    pills = blocks.ListBlock(blocks.CharBlock(), max_num=3, help_text="Hasta 3 pills")
    badge = blocks.CharBlock(
        required=False,
        default="Soluciones TI empresariales",
        help_text="Etiqueta superior del hero",
    )
    cta_primary_label = blocks.CharBlock(
        required=False, default="Conocer servicios", help_text="Botón principal"
    )
    cta_primary_href = blocks.CharBlock(required=False, default="/servicios/")
    cta_secondary_label = blocks.CharBlock(required=False, default="Hablar con un experto")
    cta_secondary_href = blocks.CharBlock(required=False, default="/contacto")
    autoplay_seconds = blocks.IntegerBlock(
        default=10, min_value=0, max_value=30, help_text="Segundos por slide. 0 = sin autoplay."
    )

    class Meta:
        icon = "placeholder"
        label = "Hero (carrusel)"
        template = "home/blocks/hero.html"


class BrandItemBlock(blocks.StructBlock):
    name = blocks.CharBlock(
        help_text="Nombre de la marca. Si no subes logo, se usa el logo estático con este nombre."
    )
    logo = ImageChooserBlock(
        required=False,
        help_text=(
            "Logo de la marca (PNG/SVG con fondo transparente). Opcional: "
            "si se deja vacío se usa el logo estático por nombre."
        ),
    )

    class Meta:
        icon = "image"
        label = "Marca"

    def get_prep_value(self, value: object) -> object:
        """Permite leer datos viejos (solo el nombre) sin romper migraciones."""
        if isinstance(value, str):
            return value
        return super().get_prep_value(value)


class MarqueeBlock(blocks.StructBlock):
    items = blocks.ListBlock(BrandItemBlock(), help_text="Marcas del marquee")

    class Meta:
        icon = "placeholder"
        label = "Marquee de tecnologías"
        template = "home/blocks/marquee.html"


class ValueCardBlock(blocks.StructBlock):
    num = blocks.CharBlock(default="01")
    title = blocks.CharBlock()
    body = blocks.TextBlock()
    icon = blocks.CharBlock(
        default="server",
        help_text="server | shield | cloud | chat | headset | …",
    )


class NosotrosBlock(blocks.StructBlock):
    leads = blocks.ListBlock(blocks.TextBlock(), min_num=1, help_text="Párrafos de presentación")
    cards = blocks.ListBlock(ValueCardBlock(), min_num=1, help_text="Tarjetas de valor")
    badge = blocks.CharBlock(required=False, default="01 · Nosotros")
    title_pre = blocks.CharBlock(required=False, default="Expertos en TI,")
    title_hi = blocks.CharBlock(required=False, default="aliados", help_text="Parte con gradiente")
    title_post = blocks.CharBlock(required=False, default="de tu negocio")

    class Meta:
        icon = "placeholder"
        label = "Nosotros (01)"
        template = "home/blocks/nosotros.html"


class ServiceCardBlock(blocks.StructBlock):
    n = blocks.CharBlock(default="01")
    tag = blocks.CharBlock()
    title = blocks.CharBlock()
    body = blocks.TextBlock()
    icon = blocks.CharBlock(default="server")
    cta_label = blocks.CharBlock(required=False, default="Conocer más")
    cta_href = blocks.CharBlock(required=False, default="/servicios/")


class ServicesBlock(blocks.StructBlock):
    badge = blocks.CharBlock(required=False, default="03 · Servicios")
    title_pre = blocks.CharBlock(required=False, default="Soluciones que")
    title_hi = blocks.CharBlock(required=False, default="impulsan", help_text="Parte con gradiente")
    title_post = blocks.CharBlock(required=False, default="tu empresa")
    cards = blocks.ListBlock(
        ServiceCardBlock(),
        min_num=1,
        max_num=8,
        help_text="El carrusel se adapta a la cantidad (1 y 8)",
    )

    class Meta:
        icon = "placeholder"
        label = "Servicios (02)"
        template = "home/blocks/services.html"


class PartnersBlock(blocks.StructBlock):
    badge = blocks.CharBlock(required=False, default="04 · Aliados")
    title_pre = blocks.CharBlock(required=False, default="Trabajamos con los")
    title_hi = blocks.CharBlock(required=False, default="mejores", help_text="Parte con gradiente")
    title_post = blocks.CharBlock(required=False, default="del mundo")
    row_a = blocks.ListBlock(BrandItemBlock())
    row_b = blocks.ListBlock(BrandItemBlock())

    class Meta:
        icon = "placeholder"
        label = "Aliados (03)"
        template = "home/blocks/partners.html"


class StatBlock(blocks.StructBlock):
    count = blocks.IntegerBlock()
    pre = blocks.CharBlock(required=False, default="", help_text="Prefijo, ej. '+'")
    post = blocks.CharBlock(required=False, default="", help_text="Sufijo, ej. '%'")
    label = blocks.CharBlock()


class StatsBlock(blocks.StructBlock):
    badge = blocks.CharBlock(required=False, default="02 · Resultados")
    title_pre = blocks.CharBlock(required=False, default="Números que respaldan nuestra")
    title_hi = blocks.CharBlock(
        required=False, default="experiencia.", help_text="Parte con gradiente"
    )
    stats = blocks.ListBlock(StatBlock(), min_num=1)

    class Meta:
        icon = "placeholder"
        label = "Resultados (04)"
        template = "home/blocks/stats.html"


class CaseBlock(blocks.StructBlock):
    tag = blocks.CharBlock()
    title = blocks.CharBlock()
    body = blocks.TextBlock()
    result = blocks.CharBlock(
        required=False, help_text="Métrica de resultado, ej. '-30% en costos'"
    )
    image = ImageChooserBlock(required=False, help_text="Imagen del caso (16:9 recomendado)")


class CasesBlock(blocks.StructBlock):
    badge = blocks.CharBlock(required=False, default="05 · Casos de éxito")
    title = blocks.CharBlock(required=False, default="Proyectos que transforman negocios")
    link_label = blocks.CharBlock(required=False, default="Leer más")
    link_href = blocks.CharBlock(required=False, default="/nosotros/")
    cases = blocks.ListBlock(CaseBlock(), min_num=1)

    class Meta:
        icon = "placeholder"
        label = "Casos de éxito (05)"
        template = "home/blocks/cases.html"


class ContactRowBlock(blocks.StructBlock):
    k = blocks.CharBlock(help_text="Clave, ej. EMAIL")
    v = blocks.CharBlock(help_text="Valor, ej. hola@ritenterprise.com.co")


class ContactBlock(blocks.StructBlock):
    badge = blocks.CharBlock(required=False, default="06 · Contacto")
    title = blocks.CharBlock(required=False, default="¿Listo para transformar tu tecnología?")
    intro = blocks.TextBlock(
        required=False,
        default="Cuéntanos tu reto y te respondemos en menos de 24 horas.",
    )
    submit_label = blocks.CharBlock(required=False, default="Enviar mensaje")
    rows = blocks.ListBlock(ContactRowBlock(), help_text="Datos de contacto")

    class Meta:
        icon = "placeholder"
        label = "Contacto (06)"
        template = "home/blocks/contact.html"


# ============================================================
# Bloques de páginas interiores (ej. Nosotros)
# ============================================================


class PageHeroBlock(blocks.StructBlock):
    badge = blocks.CharBlock(help_text="Etiqueta superior, ej. 'Nosotros'")
    title_pre = blocks.CharBlock(help_text="Título (parte normal)")
    title_hi = blocks.CharBlock(required=False, help_text="Parte resaltada con gradiente")
    lead = blocks.TextBlock(required=False)
    cta_label = blocks.CharBlock(required=False)
    cta_href = blocks.CharBlock(required=False, default="/contacto/")

    class Meta:
        icon = "doc-full"
        label = "Hero de página interior"
        template = "home/blocks/page_hero.html"


class IndexListingBlock(blocks.StructBlock):
    badge = blocks.CharBlock(required=False, default="Soluciones")
    title = blocks.CharBlock(required=False, default="Nuestras soluciones")

    class Meta:
        icon = "list-ul"
        label = "Listado de páginas hijas"
        template = "home/blocks/index_listing.html"


class StoryBlock(blocks.StructBlock):
    badge = blocks.CharBlock()
    title_pre = blocks.CharBlock()
    title_hi = blocks.CharBlock(required=False)
    paragraphs = blocks.ListBlock(blocks.TextBlock(), min_num=1)

    class Meta:
        icon = "doc-full"
        label = "Historia / Quiénes somos"
        template = "home/blocks/story.html"


class InteriorStatsBlock(blocks.StructBlock):
    badge = blocks.CharBlock()
    title = blocks.CharBlock()
    stats = blocks.ListBlock(StatBlock(), min_num=1)

    class Meta:
        icon = "doc-full"
        label = "Números (interior)"
        template = "home/blocks/interior_stats.html"


class SectorCardBlock(blocks.StructBlock):
    num = blocks.CharBlock(default="01")
    title = blocks.CharBlock()
    tag = blocks.CharBlock(required=False, help_text="Tecnologías / etiqueta")
    points = blocks.ListBlock(blocks.TextBlock(), min_num=1)


class SectorsBlock(blocks.StructBlock):
    badge = blocks.CharBlock()
    title = blocks.CharBlock()
    cards = blocks.ListBlock(SectorCardBlock(), min_num=1)

    class Meta:
        icon = "doc-full"
        label = "Experiencia por sector"
        template = "home/blocks/sectors.html"


class MissionVisionBlock(blocks.StructBlock):
    badge = blocks.CharBlock()
    title_pre = blocks.CharBlock()
    title_hi = blocks.CharBlock(required=False)
    mission = blocks.TextBlock()
    vision = blocks.TextBlock()
    mission_label = blocks.CharBlock(required=False, default="Misión")
    vision_label = blocks.CharBlock(required=False, default="Visión")

    class Meta:
        icon = "doc-full"
        label = "Misión y Visión"
        template = "home/blocks/mission_vision.html"


class ValueItemBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    body = blocks.TextBlock()


class ValuesBlock(blocks.StructBlock):
    badge = blocks.CharBlock()
    title = blocks.CharBlock()
    items = blocks.ListBlock(ValueItemBlock(), min_num=1)

    class Meta:
        icon = "doc-full"
        label = "Valores"
        template = "home/blocks/values.html"


class CTABandBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    body = blocks.TextBlock(required=False)
    cta_label = blocks.CharBlock(default="Contáctenos ahora")
    cta_href = blocks.CharBlock(default="/contacto/")

    class Meta:
        icon = "doc-full"
        label = "Banda CTA"
        template = "home/blocks/cta_band.html"


# ============================================================
# Bloques de la página Contacto
# ============================================================


class ContactCardBlock(blocks.StructBlock):
    k = blocks.CharBlock(help_text="Etiqueta, ej. Oficina")
    v = blocks.CharBlock(help_text="Valor, ej. AV Kra 9 # 115-06 OF 1207")
    href = blocks.CharBlock(required=False, help_text="Enlace opcional (mailto:, tel:, URL)")


class ContactInfoBlock(blocks.StructBlock):
    badge = blocks.CharBlock()
    title = blocks.CharBlock()
    cards = blocks.ListBlock(ContactCardBlock(), min_num=1)

    class Meta:
        icon = "doc-full"
        label = "Datos de contacto"
        template = "home/blocks/contact_info.html"


class ContactFormBlock(blocks.StructBlock):
    badge = blocks.CharBlock()
    title = blocks.CharBlock()
    note = blocks.CharBlock(required=False, help_text="Nota legal (Habeas Data)")
    privacy_href = blocks.CharBlock(required=False, default="/politicas/tratamiento-datos/")
    submit_label = blocks.CharBlock(required=False, default="Enviar mensaje")

    class Meta:
        icon = "doc-full"
        label = "Formulario de contacto"
        template = "home/blocks/contact_form.html"


class MapBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    query = blocks.CharBlock(help_text="Dirección para el mapa")

    class Meta:
        icon = "doc-full"
        label = "Mapa"
        template = "home/blocks/map.html"


# ============================================================
# Bloques reutilizables de páginas de Soluciones
# ============================================================


class IconCardBlock(blocks.StructBlock):
    badge = blocks.CharBlock(required=False, help_text="Etiqueta superior de la tarjeta")
    icon = blocks.CharBlock(required=False, default="server")
    title = blocks.CharBlock()
    body = blocks.TextBlock()
    bullets = blocks.ListBlock(blocks.CharBlock(), required=False)
    cta_label = blocks.CharBlock(required=False)
    cta_href = blocks.CharBlock(required=False)


class CardsBlock(blocks.StructBlock):
    badge = blocks.CharBlock(required=False)
    title = blocks.CharBlock(required=False)
    intro = blocks.TextBlock(required=False)
    cards = blocks.ListBlock(IconCardBlock(), min_num=1)

    class Meta:
        icon = "doc-full"
        label = "Tarjetas"
        template = "home/blocks/cards.html"


class ChecklistBlock(blocks.StructBlock):
    badge = blocks.CharBlock(required=False)
    title = blocks.CharBlock(required=False)
    items = blocks.ListBlock(blocks.CharBlock(), min_num=1)

    class Meta:
        icon = "doc-full"
        label = "Checklist (2 columnas)"
        template = "home/blocks/checklist.html"


class AccordionItemBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    body = blocks.TextBlock()


class AccordionBlock(blocks.StructBlock):
    badge = blocks.CharBlock(required=False)
    title = blocks.CharBlock(required=False)
    items = blocks.ListBlock(AccordionItemBlock(), min_num=1)

    class Meta:
        icon = "doc-full"
        label = "Acordeón"
        template = "home/blocks/accordion.html"


class HighlightBlock(blocks.StructBlock):
    badge = blocks.CharBlock(required=False)
    title = blocks.CharBlock()
    body = blocks.TextBlock(required=False)
    bullets = blocks.ListBlock(blocks.CharBlock(), required=False)
    cta_label = blocks.CharBlock(required=False)
    cta_href = blocks.CharBlock(required=False)

    class Meta:
        icon = "doc-full"
        label = "Destacado (dark)"
        template = "home/blocks/highlight.html"


class BadgesBlock(blocks.StructBlock):
    badge = blocks.CharBlock(required=False)
    title = blocks.CharBlock(required=False)
    subtitle = blocks.CharBlock(required=False)
    items = blocks.ListBlock(blocks.CharBlock(), min_num=1)

    class Meta:
        icon = "doc-full"
        label = "Credenciales (badges)"
        template = "home/blocks/badges.html"


class AlliesBlock(blocks.StructBlock):
    badge = blocks.CharBlock(required=False)
    title = blocks.CharBlock(required=False)
    subtitle = blocks.CharBlock(required=False)
    items = blocks.ListBlock(blocks.CharBlock(), min_num=1)

    class Meta:
        icon = "doc-full"
        label = "Aliados"
        template = "home/blocks/allies.html"


class TimelineStepBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    body = blocks.TextBlock(required=False)


class TimelineBlock(blocks.StructBlock):
    badge = blocks.CharBlock(required=False)
    title = blocks.CharBlock(required=False)
    steps = blocks.ListBlock(TimelineStepBlock(), min_num=1)

    class Meta:
        icon = "doc-full"
        label = "Timeline (pasos)"
        template = "home/blocks/timeline.html"


class SplitItemBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    body = blocks.TextBlock()


class SplitBulletsBlock(blocks.StructBlock):
    badge = blocks.CharBlock(required=False)
    title = blocks.CharBlock(required=False)
    intro = blocks.TextBlock(required=False)
    items = blocks.ListBlock(SplitItemBlock(), min_num=1)
    note = blocks.TextBlock(required=False)

    class Meta:
        icon = "doc-full"
        label = "Split con bullets"
        template = "home/blocks/split_bullets.html"


class QuoteBlock(blocks.StructBlock):
    badge = blocks.CharBlock(required=False)
    text = blocks.TextBlock()

    class Meta:
        icon = "doc-full"
        label = "Cita / propósito"
        template = "home/blocks/quote.html"


class TabItemBlock(blocks.StructBlock):
    label = blocks.CharBlock(help_text="Texto de la pestaña")
    title = blocks.CharBlock()
    body = blocks.TextBlock()


class TabsBlock(blocks.StructBlock):
    badge = blocks.CharBlock(required=False)
    title = blocks.CharBlock(required=False)
    subtitle = blocks.CharBlock(required=False)
    tabs = blocks.ListBlock(TabItemBlock(), min_num=1)

    class Meta:
        icon = "doc-full"
        label = "Pestañas (tabs)"
        template = "home/blocks/tabs.html"
