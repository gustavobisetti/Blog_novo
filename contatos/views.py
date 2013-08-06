from django.shortcuts import render
from django.http import HttpResponseRedirect
from models import ContatoForm

def contato(request):
    mostrar = ''
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.enviar()
            mostrar = 'Contato enviado!'
            forms = ContatoForm()
    else:
        form = ContatoForm()

    return render(request, "contatos/contato.html", {
        'form': form,'mostrar': mostrar
    })
