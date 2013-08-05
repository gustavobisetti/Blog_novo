# -*- coding:utf-8 -*-

from django.shortcuts import render
from artigos.models import Artigo

def artigo(request, pk):
    individual = Artigo.objects.get(pk=pk)
    context = {'individual': individual}
    return render(request, 'artigos/artigo.html',context)

