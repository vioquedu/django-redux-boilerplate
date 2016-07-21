from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_GET, require_POST

def make_view_mixin(class_name, decorator):
    mixin = type(class_name, (object, ), {})
    dispatch = lambda self, *a, **k: super(mixin, self).dispatch(*a, **k)
    mixin.dispatch = method_decorator(decorator)(dispatch)
    return mixin

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
