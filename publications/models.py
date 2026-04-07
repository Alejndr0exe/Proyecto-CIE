from django.db import models

# Create your models here.
class Publication(models.Model):
    autors = models.TextField()
    titulo = models.TextField()
    fecha = models.DateField()
    magazine = models.TextField()
    doi = models.URLField()
    url = models.URLField()

    def __str__(self):
        return self.titulo