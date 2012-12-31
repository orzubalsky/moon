from django.conf.urls import patterns, include, url

urlpatterns = patterns('moonline.views',
    url(r'^answer$', 'answer', name='answer'),
    url(r'^read$', 'read', name='read'),    
)
