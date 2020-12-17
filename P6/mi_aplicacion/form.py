from django import forms
from .models import Libro, Autor, Prestamo
from django.core.exceptions import ValidationError
from django.utils import timezone

class Add_LibroForm(forms.Form):
    titulo  = forms.CharField(help_text="Inserte el título del libro: ")
    portada = forms.ImageField(help_text="Inserte la portada del libro: ". required = False)

class Add_PrestamoForm(forms.Form):
    libro   = forms.CharField("Inserte el título del libro: ")
    fecha   = forms.DateField("Inserte la fecha del préstamo: ")
    usuario = forms.CharField("Inserte el nombre del solicitante: ")

    def clean_fecha(self):
        fecha = self.cleaned_data['fecha']

        if fecha < timezone.now():
            raise ValidationError(_("Fecha inválida"))
    
class Add_AutorForm(forms.Form):
    nombre  = forms.CharField(help_text="Inserte el nombre del autor: ")
