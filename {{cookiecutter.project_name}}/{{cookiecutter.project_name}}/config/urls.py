# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
      # Uncomment the next line to enable the admin:
      url(r'^admin/', include(admin.site.urls)),
      url(r'^accounts/login/', obtain_jwt_token),

      # Docs
      url(r'^docs/', include('docs.urls')),

      # User management
      url(r'^', include("apps.common.urls", namespace="common")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
