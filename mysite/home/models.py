from django.db import models
from wagtail.core import blocks

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock

from website_blocks.blocks import HeroText


class HomePage(Page):
    body = StreamField([
        ('heading', blocks.CharBlock(form_classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('button', blocks.CharBlock()),
        ('HeroText',HeroText())
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
