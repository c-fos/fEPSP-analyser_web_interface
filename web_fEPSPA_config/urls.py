from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^individual/(?P<path>.+)/$', 'analyser.views.individual'),
    url(r'^sheduler/(?P<path>.+)/$', 'analyser.views.sheduler'),
    url(r'^R/$', 'Rinterface.views.rtest'),
    url(r'^admin/', include(admin.site.urls)),
)
