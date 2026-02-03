from django.db import models

class Director(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)
    biografia = models.TextField(blank=True)
    foto = models.ImageField(upload_to='directores/', blank=True, null=True)

    def __str__(self):
        return self.nombre



class Pelicula(models.Model):
    titulo = models.CharField(max_length=200)
    estreno = models.DateField()
    genero = models.CharField(max_length=50)
    sinopsis = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='peliculas/', blank=True, null=True)
    director = models.ForeignKey(Director, related_name='peliculas', on_delete=models.CASCADE)


    def __str__(self):
        return self.titulo