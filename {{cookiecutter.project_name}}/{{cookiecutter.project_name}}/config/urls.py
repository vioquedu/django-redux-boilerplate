# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

urlpatterns = patterns('',
      # Uncomment the next line to enable the admin:
      url(r'^admin/', include(admin.site.urls)),
      url(r'^accounts/login/', 'rest_framework_jwt.views.obtain_jwt_token'),
      # User management
      url(r'$', include("apps.common.urls", namespace="common")),

      # Docs
      url(r'^docs/', include('docs.urls')),


) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
