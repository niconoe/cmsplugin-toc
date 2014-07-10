from cms.models.pluginmodel import CMSPlugin

from django.db import models
from cms.plugins.text.models import Text


class Toc(CMSPlugin):
    content_source = models.ForeignKey(Text)
