from django import forms
from .models import Libro, Autor, Prestamo
from django.core.exceptions import ValidationError
import datetime

#------ Formularios objetos --------

class Libro_form(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ('titulo', 'portada',)

class Prestamo_form(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ('libro', 'fecha', 'usuario',)

    def clean_fecha(self):
        fecha = self.cleaned_data['fecha']

        if fecha < datetime.date.today():
            raise ValidationError("Fecha inválida")
        return fecha
    
class Autor_form(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ('nombre', 'libros',)
