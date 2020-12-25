from django.contrib import admin

from .models import Libro, Prestamo, Autor

admin.site.register(Libro)
admin.site.register(Prestamo)
admin.site.register(Autor)


