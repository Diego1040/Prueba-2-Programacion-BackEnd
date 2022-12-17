from django import forms
from django.forms import ModelForm
from .models import Libro

#Class CreateBookForm para los inputs de la plantilla

class CreateBookForm(ModelForm):

    class Meta:
        #modelo de libro
        model = Libro
        #campos para definir
        fields = ['Id', 'Titulo', 'Año', 'Descripcion', 'Categoria', 'Autor']
        #inputs para desplegar en el html
        widgets = {
            'Id': forms.TextInput(attrs={"class":"form-control", "pleaceholder": "Isbn"}),
            'Titulo': forms.TextInput(attrs={"class":"form-control", "pleaceholder": "Title"}),
            'Año': forms.DateInput(attrs={"class":"form-control", "type": "date"}),
            'Descripcion': forms.Textarea(attrs={"class":"form-control"}),
            'Categoria': forms.SelectMultiple(attrs={"class":"select form-control"}),
            'Autor': forms.Select(attrs={"class":"form-control"})
        }