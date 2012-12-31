from django.conf.urls import patterns, include, url

urlpatterns = patterns('moonline.views',
    url(r'^answer$', 'index', name='answer'),
    url(r'^read$', 'index', name='read'),    
)
