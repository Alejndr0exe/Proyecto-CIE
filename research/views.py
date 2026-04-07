from django.shortcuts import render
from membersApp.models import Area
from django.shortcuts import get_object_or_404

# Create your views here.
def research (request):
    areas = Area.objects.all()
    context = {
        "areas": areas
    }
    return render(request, "research/research.html", context)

def lineResearch (request, id):
    area = get_object_or_404(Area, id=id)
    members = area.miembros.all()

    data = {
        'area': area,
        'members': members,
    }

    return render(request, "research/lineResearch.html", data)