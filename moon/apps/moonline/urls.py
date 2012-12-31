from django.conf.urls import patterns, include, url

urlpatterns = patterns('moonline.views',
    url(r'^$', 'index', name='home'),    
)
