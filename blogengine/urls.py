from django.conf.urls import patterns, urls
from django.views.generic import ListView
from blogengine.models import Post

urlpatterns = patterns('',
    # Index
    url('^$', ListView.as_view(
        model=Post,
        )),
)