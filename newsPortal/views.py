from django.shortcuts import render
from newsPortal.models import Noticias
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.db.models import Q 

# Create your views here.
def newsPortal(request):
    busqueda = request.GET.get('q')
    object_list = Noticias.objects.all()

    if busqueda:
        object_list = object_list.filter(
            Q(encabezado__icontains=busqueda) | 
            Q(bajada__icontains=busqueda)
        )

    object_list = object_list.order_by('-fecha')
    data = { 'news' : object_list }
    return render(request, "news/news.html", data)

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

