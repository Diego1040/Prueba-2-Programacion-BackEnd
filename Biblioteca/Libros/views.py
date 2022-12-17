from django.shortcuts import render
from Libros.models import *
from .forms import CreateBookForm
from django.views.generic.edit import CreateView

# Create your views here.

#Clase BookCreate que importa los forms y el CreateView es un vista generica de Creacion de formularios para importarlo a las urls

class BookCreate(CreateView):
    template_name = 'Libros/templates/book_create.html'
    model = Libro
    form_class = CreateBookForm
