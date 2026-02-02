from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import BlogPost, Project, Service

class StaticViewSitemap(Sitemap):
    priority = 1.0
    changefreq = 'daily'

    def items(self):
        return ['home', 'about', 'contact', 'projects', 'services', 'blog']

    def location(self, item):
        return reverse(item)

class BlogPostSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        return BlogPost.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.updated_at

class ProjectSitemap(Sitemap):
    priority = 0.9
    changefreq = 'monthly'

    def items(self):
        return Project.objects.filter(is_active=True)

    def lastmod(self, obj):
        return obj.updated_at

class ServiceSitemap(Sitemap):
    priority = 0.8
    changefreq = 'monthly'

    def items(self):
        return Service.objects.filter(is_active=True)

    def lastmod(self, obj):
        return obj.updated_at
