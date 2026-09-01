"""Bloques StreamField de la Home — secciones editables del mockup V1.

Cada bloque corresponde a una sección del Home aprobado por el cliente.
Los valores por defecto (seed) se cargan desde la migración de datos
0003_seed_home_content, con el contenido del front antiguo (data.py).
"""

from wagtail import blocks


class HeroSlideBlock(blocks.StructBlock):
    pre = blocks.CharBlock(help_text="Texto antes del highlight (gradiente)")
    hi = blocks.CharBlock(help_text="Texto resaltado con gradiente")
    kicker = blocks.TextBlock(help_text="Frase corta bajo el título")
    index = blocks.CharBlock(default="01", help_text="Índice del slide (01, 02…)")
    sub = blocks.TextBlock(help_text="Párrafo lateral del slide")


class HeroBlock(blocks.StructBlock):
    slides = blocks.ListBlock(HeroSlideBlock(), min_num=1)
    pills = blocks.ListBlock(blocks.CharBlock(), max_num=3, help_text="Hasta 3 pills")

    class Meta:
        icon = "placeholder"
        label = "Hero (carrusel)"
        template = "home/blocks/hero.html"


class MarqueeBlock(blocks.StructBlock):
    items = blocks.ListBlock(blocks.CharBlock(), help_text="Tecnologías del marquee")

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


class ServicesBlock(blocks.StructBlock):
    cards = blocks.ListBlock(
        ServiceCardBlock(),
        min_num=1,
        max_num=4,
        help_text="Máx. 4 (carrusel CSS atado a 4)",
    )

    class Meta:
        icon = "placeholder"
        label = "Servicios (02)"
        template = "home/blocks/services.html"


class PartnersBlock(blocks.StructBlock):
    row_a = blocks.ListBlock(blocks.CharBlock())
    row_b = blocks.ListBlock(blocks.CharBlock())

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
    stats = blocks.ListBlock(StatBlock(), min_num=1)

    class Meta:
        icon = "placeholder"
        label = "Resultados (04)"
        template = "home/blocks/stats.html"


class CaseBlock(blocks.StructBlock):
    tag = blocks.CharBlock()
    title = blocks.CharBlock()
    body = blocks.TextBlock()
    result = blocks.CharBlock(help_text="Métrica de resultado, ej. '-30% en costos'")


class CasesBlock(blocks.StructBlock):
    cases = blocks.ListBlock(CaseBlock(), min_num=1)

    class Meta:
        icon = "placeholder"
        label = "Casos de éxito (05)"
        template = "home/blocks/cases.html"


class ContactRowBlock(blocks.StructBlock):
    k = blocks.CharBlock(help_text="Clave, ej. EMAIL")
    v = blocks.CharBlock(help_text="Valor, ej. hola@ritenterprise.com.co")


class ContactBlock(blocks.StructBlock):
    rows = blocks.ListBlock(ContactRowBlock(), help_text="Datos de contacto")

    class Meta:
        icon = "placeholder"
        label = "Contacto (06)"
        template = "home/blocks/contact.html"
