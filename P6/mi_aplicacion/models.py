from django.db import models
from django.utils import timezone

class Libro(models.Model):
  titulo = models.CharField(max_length=200)
  portada = models.ImageField(upload_to='portadas', default='error.jpeg')

  def __str__(self):
    return self.titulo

class Prestamo(models.Model):
  libro   = models.ForeignKey(Libro, on_delete=models.CASCADE)
  fecha   = models.DateField(default=timezone.now)
  usuario = models.CharField(max_length=100)

  def __str__(self):
    return self.libro + " - " + self.usuario

class Autor(models.Model):
  nombre = models.CharField(max_length=200)
  libros = models.ManyToManyField(Libro)

  def __str__(self):
    return self.nombre
