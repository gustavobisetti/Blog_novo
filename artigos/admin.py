from artigos.models import Artigo
from django.contrib import admin

class ArtigoAdmin(admin.ModelAdmin):
    fields = ['data', 'titulo', 'conteudo']

admin.site.register(Artigo, ArtigoAdmin)
