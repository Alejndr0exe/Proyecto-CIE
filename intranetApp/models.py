from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria (models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre


class Documento (models.Model):
    documento = models.FileField(upload_to='docs/', unique=True )
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE) 
    investigador = models.CharField(max_length=50)
    proyecto =  models.CharField(max_length=50, blank=True)
    descripcion = models.CharField(max_length=150, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def delete(self):
        self.documento.delete()
        super().delete()

class Reserva(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    responsable = models.CharField(max_length=100) # El nombre editable que pediste
    inicio = models.DateTimeField()
    fin = models.DateTimeField()
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.responsable} ({self.inicio})"




