from django.conf.urls import url, include

from django.views.generic import TemplateView

urlpatterns = [
        url(r'^', TemplateView.as_view(template_name='common/pages/frontpage.html'), name='frontpage')
        ]
