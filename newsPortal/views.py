from django.shortcuts import render
from newsPortal.models import Noticias
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

# Create your views here.
def newsPortal(request):
    news = Noticias.objects.all().order_by('-fecha')
    data = {
        'news' : news
    }

    return render(request,"news/news.html", data) 

def newCei (request, id):
    timestamp = timezone.now().timestamp()
    noticia = get_object_or_404(Noticias, id=id)
    parrafos = noticia.parrafos.all()
    portada = noticia.portada.url
    imgs = noticia.imgs.all()
    videos = noticia.videos.all()
    news = Noticias.objects.exclude(id=id)

    data = {
        'timestamp': timestamp,
        'noticia': noticia,
        'parrafos': parrafos,
        'portada': portada,
        'news' : news,
        'imgs' : imgs,
        'videos' : videos
    }

    return render(request, "news/new.html", data)

