from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from bs4 import BeautifulSoup

from .models import Toc


class TocPlugin(CMSPluginBase):
    model = Toc
    name = _("TOC Plugin")
    render_template = "toc_plugin.html"

    def render(self, context, instance, placeholder):
        context['instance'] = instance

        raw_html = BeautifulSoup(instance.content_source.body)

        toc_entries = []
        missing_ids = False

        for title in raw_html.find_all('h2'):
            entry = {}
            entry['text'] = title.text
            try:
                entry['anchor'] = title['id']
            except KeyError:
                entry['anchor'] = ""
                missing_ids = True
            
            toc_entries.append(entry)

        context['toc_entries'] = toc_entries
        context['missing_ids'] = missing_ids
        return context

plugin_pool.register_plugin(TocPlugin)
