from django.contrib.sitemaps import Sitemap
from .models import Topic, Service, Feature, Client


class NewsSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.4

    def items(self):
        items = []
        for model in [Topic, Service, Feature]:
            items.extend(model.objects.all())
        return items

    def lastmod(self, item):
        return item.pub_date
