from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from membersApp import forms
from membersApp.models import Members

# Create your views here.

def miembros(request):

    members = Members.objects.all()
    data = {
        'members' : members
    }

    return render(request,"members/members.html", data)

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
