from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from membersApp import forms
from membersApp.models import Members
from django.db.models import Q 


# Create your views here.

def miembros(request):
    busqueda = request.GET.get('q')
    sort_by = request.GET.get('sort')
    members = Members.objects.all()

    if busqueda:
        members = members.filter(
            Q(nombre__icontains=busqueda) | 
            Q(puesto__icontains=busqueda) |
            Q(area__nombre__icontains=busqueda) |
            Q(titulo__icontains=busqueda) | 
            Q(academic_rank__icontains=busqueda) |
            Q(email__icontains=busqueda) | 
            Q(universidad__icontains=busqueda) 
        )

    if sort_by == 'name':
        members = members.order_by('nombre')
    elif sort_by == 'rank':
        members = members.order_by('academic_rank')
    elif sort_by == 'position':
        members = members.order_by('-puesto')
    else:
        members = members.order_by('nombre')

    data = {
        'members': members
    }
    return render(request, "members/members.html", data)

def addMiembro(request):
    form = forms.addMember()

    if request.method == 'POST':
        form = forms.addMember(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('addMember'))


    context = {'form': form }

    return render(request, "members/addMembers.html", context)

def infoMiembro(request, id):

    member = Members.objects.get(id = id)
    related_members = Members.objects.filter(area=member.area).exclude(id=member.id)

    data = {
        'member' : member,
        'related_members' : related_members
    }

    return render(request,"members/infoMember.html", data)
