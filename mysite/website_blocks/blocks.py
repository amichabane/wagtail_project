from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class HeroText(blocks.StructBlock):
    title = blocks.RichTextBlock(default="Title", required=False)
    description = blocks.RichTextBlock(default="Description", required=False)
    button = blocks.CharBlock(default="Button", required=False)
    image = ImageChooserBlock(help_text="Dimension mininum :660 x 980px")

    class Meta:
        template = 'website_blocks/hero_text.html'
        icon = 'image'


class CardBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False, help_text="Add your title")

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=False)),
                ("title", blocks.CharBlock(required=False, max_length=40)),
                ("text", blocks.TextBlock(required=False, max_length=200)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                ("button_url", blocks.URLBlock(required=False,
                                               help_text="If the button page above is selected, that will be used first.")),
            ]
        )
    )
    class Meta:  # noqa
        template = "streams/card_block.html"
        icon = "placeholder"
