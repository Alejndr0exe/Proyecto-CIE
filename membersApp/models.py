from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
class Area(models.Model):
    nombre = models.CharField(max_length=50)
    fragmento = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True)
    responsable = models.ForeignKey('Members', on_delete=models.SET_NULL, null=True, blank=True, related_name='areas_responsable')
    portada = models.ImageField(upload_to='areas/', blank=True, null=True)
    icono = models.FileField(
        upload_to='areas/iconos/', blank=True, null=True, validators=[FileExtensionValidator(allowed_extensions=['svg'])])
    def __str__(self):
        return self.nombre

class Members(models.Model):
    nombre = models.CharField(max_length=50)
    titulo = models.CharField(max_length=50, blank=True)
    academic_rank = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=50, blank=True)
    g_scholar = models.CharField(max_length=100, blank=True)
    img = models.ImageField(upload_to='members/')
    descripcion = models.TextField()
    puesto = models.CharField(max_length=50, blank=True)
    universidad = models.CharField(max_length=50, blank=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name='miembros', blank=True)

    def __str__(self):
        return self.nombre