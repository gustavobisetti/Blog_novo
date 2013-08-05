# -*- coding:utf-8 -*-

from django.db import models

class Artigo(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.CharField(max_length=200)
    data = models.DateTimeField('data da publicação')

def __unicode__(self):
    return u'{titulo} {conteudo} {data}'.format(titulo=self.titulo, conteudo=self.conteudo, data=self.data)
