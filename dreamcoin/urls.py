# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from . import views

from django.contrib import admin

admin.autodiscover()

urlpatterns =  [
    url(r'^$', views.home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
]
