# mi_aplicacion/urls.py

from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
    
  path('libro_add', views.Libro_add, name='Libro_add'),
  path('prestamo_add', views.Prestamo_add, name='Prestamo_add'),
  path('autor_add', views.Autor_add, name='Autor_add'),

  path('libro_modif', views.Libro_modif, name='Libro_modif'),
  path('prestamo_modif', views.Prestamo_modif, name='Prestamo_modif'),
  path('autor_modif', views.Autor_modif, name='Autor_modif'),

  path('libro_borrar', views.Libro_borrar, name='Libro_borrar'),
  path('prestamo_borrar', views.Prestamo_borrar, name='Prestamo_borrar'),
  path('autor_borrar', views.Autor_borrar, name='Autor_borrar'),
]
