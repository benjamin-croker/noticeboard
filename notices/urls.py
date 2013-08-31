from django.conf.urls import patterns, include, url

urlpatterns = patterns('notices.views',
    url(r'^$', 'notices'),
    url(r'^new/$', 'new'),
    url(r'^(?P<notice_id>\d+)/delete/$', 'delete'),
    url(r'^(?P<notice_id>\d+)/edit/$', 'edit'),
)