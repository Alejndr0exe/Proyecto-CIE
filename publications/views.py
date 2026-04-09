from django.shortcuts import render
from publications.models import Publication
from django.db.models import Q 

def publications(request):
    busqueda = request.GET.get('q')
    orden = request.GET.get('sort')
    
    # Base de la consulta
    object_list = Publication.objects.all()

    # Lógica de búsqueda
    if busqueda:
        object_list = object_list.filter(
            Q(titulo__icontains=busqueda) | 
            Q(autors__icontains=busqueda) |
            Q(magazine__icontains=busqueda)
        )

    # Lógica de ordenamiento
    if orden == 'oldest':
        object_list = object_list.order_by('fecha')
    else:
        object_list = object_list.order_by('-fecha') # Por defecto más recientes

    data = { 'publications' : object_list }
    return render(request, "publications/publications.html", data)