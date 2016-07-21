from django.conf import settings


def site_info(request):
    return {
        'site_name': settings.SITE_NAME,
    }
