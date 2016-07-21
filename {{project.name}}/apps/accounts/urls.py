
from django.conf.urls import url, include

from apps.accounts.views import ViewTest

urlpatterns = [
    url(r'^test-template/', ViewTest.as_view(), name='test-template'),
]
