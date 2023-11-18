from django.db import models
#Los modelos corresponden a libros leidos (Leidos) libros abandonados (Abandonados) lectura actual (Leyendo) libros por leer (Por_Leer)
#Todos los modelos contienen 3 atributos, titulo, autor y año de publicación.
class Leidos(models.Model):
    titulo=models.CharField(max_length=50)
    autor=models.CharField(max_length=30)
    año_publicacion=models.CharField(max_length=4)
class Abandonados(models.Model):
    titulo=models.CharField(max_length=50)
    autor=models.CharField(max_length=30)
    año_publicacion=models.CharField(max_length=4)
class Por_Leer(models.Model):
    titulo=models.CharField(max_length=50)
    autor=models.CharField(max_length=30)
    año_publicacion=models.CharField(max_length=4)
class Leyendo(models.Model):
    titulo=models.CharField(max_length=50)
    autor=models.CharField(max_length=30)
    año_publicacion=models.CharField(max_length=4)

