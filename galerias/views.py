from django.shortcuts import render, get_object_or_404

from models import Album, Imagem

def albuns(request):
    return render(request, 'galerias/albuns.html', {'albuns': Album.objects.all()})

def album(request, slug):
    album_ = get_object_or_404(Album, slug=slug)
    return render(
        request,
        'galerias/album.html',
        {
            'album': album_,
            'imagens': Imagem.objects.filter(album=album_),
            'capa': Imagem.objects.filter(pk=1)
        }
    )

def imagem(request, slug):
    imagem_ = get_object_or_404(Imagem, slug=slug)
    return render(
        request,
        'galerias/imagem.html',
        {
            'imagem': imagem_
        }
    )
