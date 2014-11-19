from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    (r'^$', include('forum.urls')),
    (r'^accounts/', include('registration.backends.default.urls')),
    (r'^forum/', include('forum.urls')),
)
