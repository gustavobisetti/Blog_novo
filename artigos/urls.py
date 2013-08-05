from django.conf.urls import patterns, url

from artigos import views

urlpatterns = patterns('',
    url(r'^$', 'gustavo.views.index', name='index'),
    url(r'^(?P<pk>\d+)/$', 'artigos.views.artigo', name='individual'),
)
