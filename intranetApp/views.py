from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from intranetApp import forms
from intranetApp.models import Documento, Categoria
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class CustomLoginForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        # Puedes agregar lógica adicional si quieres
        pass


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = CustomLoginForm

    def form_invalid(self, form):
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')
        error_message = "Error de autenticación."

        if not User.objects.filter(username=username).exists():
            error_message = "Perfil no encontrado."
        elif not authenticate(username=username, password=password):
            error_message = "Contraseña incorrecta."

        return self.render_to_response(
            self.get_context_data(form=form, error_message=error_message)
        )


# Create your views here.
@login_required
def intranet (request):
    form = forms.addDoc()

    docs = Documento.objects.all()

    if request.method == 'POST':
        form = forms.addDoc(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('intranet'))
        
    context = { 
        'form' : form ,
        'docs' : docs
    }

    return render(request, "intranetApp/intranet.html", context)

@login_required
def script (request):

    categoria_d = Categoria.objects.get(nombre="Scripts")
    scripts = Documento.objects.filter(categoria=categoria_d)

    data = {
        'scripts': scripts
    }

    return render(request, "intranetApp/scripts.html", data)

@login_required
def manual (request):

    categoria_d = Categoria.objects.get(nombre="Manual")
    manuals = Documento.objects.filter(categoria=categoria_d)

    data = {
        'manuals': manuals
    }

    return render(request, "intranetApp/Manuals.html", data)

@login_required
def protocol (request):

    categoria_d = Categoria.objects.get(nombre="Protocolo")
    protocolos = Documento.objects.filter(categoria=categoria_d)

    data = {
        'protocolos': protocolos
    }

    return render(request, "intranetApp/protocol.html", data)

@login_required
def data (request):

    categoria_d = Categoria.objects.get(nombre="Datos")
    datos = Documento.objects.filter(categoria=categoria_d)

    data = {
        'datos': datos
    }

    return render(request, "intranetApp/data.html", data)


@login_required
def eliminarDoc(request, id):
    doc = get_object_or_404(Documento, id=id)
    doc.delete()
    return HttpResponseRedirect(reverse('intranet'))

