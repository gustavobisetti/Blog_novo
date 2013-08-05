# -*- coding:utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render

from artigos.models import Artigo

def index(request):
    ultimos_artigos = Artigo.objects.all().order_by('data')[:5]
    context = {'ultimos_artigos': ultimos_artigos}
    return render(request, 'index.html', context)
