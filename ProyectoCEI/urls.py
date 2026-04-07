"""
URL configuration for ProyectoCEI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from homeApp.views import *
from newsPortal import views
from publications.views import *
from research.views import *
from membersApp.views import *
from intranetApp.views import *
from intranetApp.views import CustomLoginView 

# Personalización del admin (lugar seguro)
admin.site.site_header = "Panel CEI"
admin.site.site_title = "Administración CEI"
admin.site.index_title = "Bienvenido/a"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),  
    path('accounts/', include("django.contrib.auth.urls")),
    path('members/', miembros, name='miembros'),
    path('infoMembers/<int:id>', infoMiembro, name='infoMembers'),
    path('newsPortal/', views.newsPortal, name='news'),
    path('news/<int:id>', views.newCei, name='new'),
    path('pub/', publications, name='pub'),
    path('research/', research, name='research'),
    path('lineResearch/<int:id>', lineResearch, name='lineResearch'),
    path('intranet/', intranet, name='intranet'),
    path('script/', script, name='script'),
    path('data/', data, name='data'),
    path('manuals/', manual, name='manuals'),
    path('protocol/', protocol, name='protocol'),
    path('eliminarDoc/<int:id>/', eliminarDoc, name='eliminarDoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
