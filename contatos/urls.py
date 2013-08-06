from django.conf.urls import patterns, url

from contatos import views

urlpatterns = patterns('',
    url(r'^$', 'contatos.views.contato', name='contact'),
)
