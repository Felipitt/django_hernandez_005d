from tokenize import Name
from unicodedata import name
from django.urls import path
 
from .views import  eliminar_producto, from_crear_productos, index, modificar_producto, mostrar_producto, somos,FormularioR, FormularioC, galeria, Validacion, ValidacionC, Feriados, Registro, Mostrarclientes, form_del_cliente, form_crear_cliente, form_modificarcliente, form_cliente, form_producto

urlpatterns = [

    path('', index, name="index"),
    path('somos/', somos, name="somos" ),
    path('FormularioR/', FormularioR, name="FormularioR"),
    path('FormularioC/', FormularioC, name="FormularioC"),
    path('galeria/', galeria, name="galeria"),
    path('Validacion/', Validacion, name="Validacion"),
    path('ValidacionC/', ValidacionC, name="ValidacionC"),
    path('Feriados/', Feriados, name="Feriados"),
    path('Registro/', Registro, name="Registro"),
    path('Mostrarclientes/', Mostrarclientes, name="Mostrarclientes"),
    path('form_modificarcliente/<id>', form_modificarcliente, name="form_modificarcliente"),
    path('form_cliente/', form_cliente, name="form_cliente"),
    path('form_del_cliente/<id>', form_del_cliente, name="form_del_cliente"),
    path('form_crear_cliente/', form_crear_cliente, name="form_crear_cliente"),
    path('mostrar_producto/', mostrar_producto, name="mostrar_producto"),
    path('from_crear_productos/', from_crear_productos, name="from_crear_productos"),
    path('modificar_producto/<id>' ,modificar_producto, name="modificar_producto"),
    path('eliminar_producto/<id>' ,eliminar_producto, name="eliminar_producto"),
    path('form_producto/<id>' ,form_producto, name="form_producto")
]
