from django.db import models

# Create your models here.

#clases correspondientes para posterior manipulacion

#class Category para los tipos de libros
class Categoria(models.Model):
    Id = models.IntegerField(primary_key=True, editable=False)
    Nombre = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.Nombre}"

#class Pais para los autores

class Pais(models.Model):
    Id = models.IntegerField(primary_key=True, editable=False)
    Nombre = models.CharField(max_length=50)

    
    def __str__(self) -> str:
        return f"{self.Nombre}"

#class Autor para la comprobacion en Libros

class Autor(models.Model):
    Nombre = models.CharField(max_length=50)
    Pais = models.ForeignKey(
        Pais, on_delete=models.CASCADE
    )
    
    def __str__(self) -> str:
        return f"{self.Nombre}"

#Class Libro modelo principal donde se manipulara los 3 modelos

class Libro(models.Model):
    Id = models.CharField(primary_key=True, max_length=10)
    Titulo = models.CharField(max_length=50)
    Año = models.DateField()
    Descripcion = models.TextField()
    Categoria = models.ManyToManyField(Categoria)
    Autor = models.ForeignKey(
        Autor, on_delete=models.CASCADE
    )

    
    def __str__(self) -> str:
        return f"{self.Titulo}"