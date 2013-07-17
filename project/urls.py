from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from project.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'project.views.index'),
    url(r'^events/$', EventList.as_view(), name='event-list'),
    url(r'^events/new/$', EventCreate.as_view()),
    url(r'^events/(?P<pk>\d*)/delete/$', EventDelete.as_view()),
    url(r'^events/(?P<event_pk>\d*)/add/$', ParticipantCreate.as_view()),
    url(r'^events/(?P<event_pk>\d*)/participant/(?P<pk>\d*)/delete/$', ParticipantDelete.as_view()),
    url(r'^events/(?P<event_pk>\d*)/participant/(?P<pk>\d*)/pdf/$', Certificate.as_view()),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': settings.MEDIA_ROOT}),
)
