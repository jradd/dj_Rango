# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_tutorial_blog_ng.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # Blog URLs
    url(r'', include('blogengine.urls')),

    # Flat pages
   # url(r'', include('django.contrib.flatpages.urls')),

    # FauxDeux Page include
    (r'^fauxdeux/', include('fauxdeux.urls')),

    (r'^$', RedirectView.as_view(url='/fauxdeux/list/')), # Just for ease of use.
)