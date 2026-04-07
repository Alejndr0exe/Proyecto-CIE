from django.shortcuts import render
from publications.models import Publication

# Create your views here.
def publications(request):
    publications = Publication.objects.all().order_by('-fecha')
    data = {
        'publications' : publications
    }
    return render(request,"publications/publications.html", data)