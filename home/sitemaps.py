from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

class ViewSitemaps(Sitemap):
    def items(self):
        return ['about', 'projects', 'contact', 'home']
    
    def location(self, item):
        return reverse(item)