from django.db import models
from django import forms
from django.core.mail import send_mail

class ContatoForm(forms.Form):
    nome = forms.CharField(max_length=100)
    mensagem = forms.Field(widget=forms.Textarea)
    email = forms.EmailField(required=False)

    def enviar(self):
        titulo = 'Mensagem enviada pelo site'
        destino = 'gustavodjango@gmail.com'
        texto="""
        Nome: %(nome)s
        E-mail: &(email)s
        Mensagem:
        %(mensagem)s
        """ % self.cleaned_data

        send_mail(
            subject=titulo,
            message=texto,
            from_email=destino,
            recipient_list=[destino],
            )


