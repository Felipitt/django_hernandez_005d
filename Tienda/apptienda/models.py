from django.db import models

# Create your models here.


class Cliente(models.Model):

    rut=models.CharField(max_length=40, primary_key=True, verbose_name='Rut')
    nombre= models.CharField(max_length=20,  verbose_name='Nombres')
    apellidos= models.CharField(max_length=40, verbose_name='Apellidos')
    telefono=models.IntegerField(max_length=9, verbose_name='Telefono')
    direccion=models.CharField(max_length=40, verbose_name='Direccion')
    def str(self):
        return self.rut

class Categoria (models.Model): 
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de Categoría')
    nombreCategoria= models.CharField(max_length=50, verbose_name='Nombre de Categoría')

    def __str__(self):
        return self.nombreCategoria


class Producto(models.Model):
    nombre = models.CharField(max_length=6, verbose_name='nombre')
    codigo_barra= models.CharField(max_length=20, primary_key=True, verbose_name='codigo_barra')
    edad_animal=models.IntegerField(max_length=2, verbose_name='Edadanimal')
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.codigo_barra
