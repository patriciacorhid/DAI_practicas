# mi_aplicacion/views.py

from django.shortcuts import render, HttpResponse, get_object_or_404

from .forms import *

# Create your views here.

def index(request):
    return HttpResponse('Hello World!')

def Libro_add(request):

    if request.method == 'POST':
        form = Add_LibroForm(request.POST)

        if form.is_valid():
            post.save()
            return render('add_libros.html')
    else:
        form = Add_LibroForm()
    return render(request, 'add_libros.html', {'form': form})

def Prestamo_add(request):

    if request.method == 'POST':
        form = Add_PrestamoForm(request.POST)

        if form.is_valid():
            post.save()
            return render('add_prestamo.html')
    else:
        form = Add_LibroForm()
    return render(request, 'add_prestamo.html', {'form': form})

def Autor_add(request):

    if request.method == 'POST':
        form = Add_AutorForm(request.POST)

        if form.is_valid():
            post.save()
            return render('add_autor.html')
    else:
        form = Add_LibroForm()
    return render(request, 'add_autor.html', {'form': form})
