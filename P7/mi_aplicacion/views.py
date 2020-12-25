# mi_aplicacion/views.py

from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .form import *
from .models import Libro, Autor, Prestamo

# Create your views here.

# Hello world
def index(request):
    return HttpResponse('Hello World!')

#------ Página de inicio ----------------

def p4(request):
    return render(request, "base.html")

#------ Mostrar tablas por pantalla -----

def libros(request):
    libros = Libro.objects.all()
    return render(request, "lista_libros.html", {'libros': libros})

def prestamos(request):
    prestamos = Prestamo.objects.all()
    return render(request, "lista_prestamos.html", {'prestamos': prestamos})

def autores(request):
    autores = Autor.objects.all()
    return render(request, "lista_autores.html", {'autores': autores})

#------ Añadir objetos -----

def add_libro(request):
    # Rellenando los campos
    if request.method == 'POST':
        form = Libro_form(request.POST, request.FILES)

        # Comprueba que los datos introducidos sean válidos
        if form.is_valid():
            form.save() # guarda los datos del formulario
            return redirect(libros) # redirige a la lista de libros

        # Mostrando el formulario
    else:
        form = Libro_form() 
    return render(request, 'add_libro.html', {'form': form, 'titulo': "Introduzca un nuevo libro:"})

def add_prestamo(request):

    if request.method == 'POST':
        form = Prestamo_form(request.POST)

        if form.is_valid():
            form.save()
            return redirect(prestamos)
    else:
        form = Prestamo_form()
    return render(request, 'add_prestamo.html', {'form': form , 'titulo': "Introduzca un nuevo préstamo:"})

def add_autor(request):

    if request.method == 'POST':
        form = Autor_form(request.POST)

        if form.is_valid():
            form.save()
            return redirect(autores)
    else:
        form = Autor_form()
    return render(request, 'add_autor.html', {'form': form , 'titulo': "Introduzca un nuevo autor:"})

# ------- Modificar objeto ---------

def modif_libro(request, pk):
    # Obtiene el libro con ese Id y rellena los datos del formulario con él
    libro = Libro.objects.get(id=pk)
    form = Libro_form(instance=libro)

    # Si se modifica el formulario
    if request.method == "POST":
        form = Libro_form(request.POST, request.FILES, instance=libro)

        # Se comprueba que se rellenó con datos válidos
        if form.is_valid():
            form.save() # guarda los datos del formulario
        return redirect(libros)  # redirige a la lista de libros

    # Muestra el formulario con los datos originales rellenos
    return render(request, "modif_libro.html", {'form': form , 'titulo': "Modifique el libro", 'pk': pk })

def modif_prestamo(request, pk):
    prestamo = Prestamo.objects.get(id=pk)
    form = Prestamo_form(instance=prestamo)
    
    if request.method == "POST":
        form = Prestamo_form(request.POST, instance=prestamo)
        if form.is_valid():
            form.save()
        return redirect(prestamos)
    return render(request, "modif_prestamo.html", {'form': form , 'titulo': "Modifique el prestamo", 'pk': pk })


def modif_autor(request, pk):
    autor = Autor.objects.get(id=pk)
    form = Autor_form(instance=autor)
    
    if request.method == "POST":
        form = Autor_form(request.POST, instance=autor)
        if form.is_valid():
            form.save()
        return redirect(autores)
    return render(request, "modif_autor.html", {'form': form , 'titulo': "Modifique el autor", 'pk': pk })


#-------- Eliminar objeto -------------

def borrar_libro(request, pk):
    # Busca el libro con ese Id y lo elimina
    libro = Libro.objects.get(id=pk)
    libro.delete()
    return redirect(libros) # redirige a la lista de libros

def borrar_prestamo(request, pk):
    prestamo = Prestamo.objects.get(id=pk)
    prestamo.delete()
    return redirect(prestamos)

def borrar_autor(request, pk):
    autor = Autor.objects.get(id=pk)
    autor.delete()
    return redirect(autores)
