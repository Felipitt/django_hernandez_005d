from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import Cliente, Producto, Categoria


class ClienteForm(forms.ModelForm):

    class Meta: 
        model= Cliente
        fields = ['nombre', 'apellidos', 'rut' , 'telefono' , 'direccion']
        labels ={
            'nombre': 'Nombre', 
            'apellidos': 'Apellidos', 
            'rut': 'Rut',
            'telefono': 'Telefono',
            'direccion': 'Direccion',
        }
        widgets={
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre', 
                    'id': 'nombre'
                }
            ), 
            'apellidos': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese apellidos', 
                    'id': 'apellidos'
                }
            ), 
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese rut', 
                    'id': 'rut'
                }
            ),             
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese telefono', 
                    'id': 'telefono'
                }
            ),    
             'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese direccion', 
                    'id': 'direccion'
                
                }
            )

        }
    
class ProductoForm(forms.ModelForm):

    class Meta: 
        model= Producto
        fields = ['nombre', 'codigo_barra', 'edad_animal', 'categoria']
        labels ={
            'nombre': 'Nombre', 
            'codigo_barra': 'Codigo_barra', 
            'edad_animal': 'Edad_animal', 
            'categoria': 'Categoría',
        }
        widgets={
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre', 
                    'id': 'nombre'
                }
            ), 
            'codigo_barra': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Codigo barra', 
                    'id': 'codigo_barra'
                }
            ), 
            'edad_animal': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese edad animal', 
                    'id': 'edad_animal'
                }
            ), 
            'categoria': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'categoria',
                }
            )

        }

 
    
     


