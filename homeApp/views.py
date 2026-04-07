from django.shortcuts import render
from newsPortal.models import Noticias

# Create your views here.
def index(request):

    news = Noticias.objects.order_by('-fecha')[:4]
    data = {
        'news' : news
    }

    return render(request,"homeApp/index.html", data)
 