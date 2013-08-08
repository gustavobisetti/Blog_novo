from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'gustavo.views.index', name='home'),
    url(r'^artigos/', include('artigos.urls')),
    url(r'^contato/', include('contatos.urls')),
    url(r'^galerias/', include('galerias.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
