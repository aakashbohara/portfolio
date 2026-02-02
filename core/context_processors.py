"""
Portfolio Context Processors
"""

from .models import ProfileSetting, Service


def site_context(request):
    return {
        'profile': ProfileSetting.get_profile(),
        'footer_services': Service.objects.filter(is_active=True).order_by('order')[:5],
    }
