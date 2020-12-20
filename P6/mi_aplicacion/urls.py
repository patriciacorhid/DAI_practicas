# mi_aplicacion/urls.py

from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('p4', views.p4, name='p4'),

  # URLs para mostrar la lista de objetos
  path('lista_libros', views.libros, name='libros'),
  path('lista_prestamos', views.prestamos, name='prestamos'),
  path('lista_autores', views.autores, name='autores'),

  # URLs para añadir un objeto
  path('add_libro', views.add_libro, name='add_libro'),
  path('add_prestamo', views.add_prestamo, name='add_prestamo'),
  path('add_autor', views.add_autor, name='add_autor'),

    # URLs para mostrar la modificar un objeto por el campo Id (pk = primary key, que es el Id del objeto)
  path('modif_libro/<int:pk>', views.modif_libro, name='modif_libro'),
  path('modif_prestamo/<int:pk>', views.modif_prestamo, name='modif_prestamo'),
  path('modif_autor/<int:pk>', views.modif_autor, name='modif_autor'),

  # URLs para mostrar la borrar un objeto por el campo Id
  path('borrar_libro/<int:pk>', views.borrar_libro, name='borrar_libro'),
  path('borrar_prestamo/<int:pk>', views.borrar_prestamo, name='borrar_prestamo'),
  path('borrar_autor/<int:pk>', views.borrar_autor, name='borrar_autor'),
]
