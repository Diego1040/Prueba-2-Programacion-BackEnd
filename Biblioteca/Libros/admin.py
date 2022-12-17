from django.contrib import admin
from .models import *

# Register your models here.

#admin.site.register para tenerlo en el panel de administrador con cuenta de admin en django
#python manage.py makemigrations

admin.site.register(Categoria)

admin.site.register(Pais)

admin.site.register(Autor)

admin.site.register(Libro)