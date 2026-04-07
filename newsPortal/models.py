from django.db import models

# Create your models here.
class Noticias (models.Model):
    encabezado = models.CharField(max_length=225)
    bajada = models.TextField(blank=True)
    fecha=models.DateField()
    portada = models.ImageField(upload_to='news/')

    def delete(self):
        self.portada.delete()
        super().delete()

class Parrafos (models.Model):
    subtitulo = models.CharField(max_length=225, blank=True)
    cuerpo = models.TextField()
    noticia = models.ForeignKey(Noticias, on_delete=models.CASCADE, related_name='parrafos')
    def __str__(self):
        return self.cuerpo
    
    
class Imgs (models.Model):
    img = models.ImageField(upload_to='news/')
    descricion = models.CharField(max_length=255)
    noticia = models.ForeignKey(Noticias, on_delete=models.CASCADE, related_name='imgs')
    def __str__(self):
        return self.descricion
    
    def delete(self):
        self.img.delete()
        super().delete()
    

class Videos (models.Model):
    video = models.FileField(upload_to='news/')
    descricion = models.CharField(max_length=255)
    noticia = models.ForeignKey(Noticias, on_delete=models.CASCADE, related_name='videos')
    def __str__(self):
        return self.descricion
    
    def delete(self):
        self.video.delete()
        super().delete()
