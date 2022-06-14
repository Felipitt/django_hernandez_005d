
from django.shortcuts import render, redirect
from django.views.decorators import csrf 
from .models import Cliente, Producto
from .forms import ClienteForm, ProductoForm

# Create your views here. 
def index(request):
    return render (request, 'index.html')
def somos (request):
    return render (request, "somos.html")
def galeria(request):
    return render (request, "galeria.html")    
def FormularioC(request):
    return render (request, "FormularioC.html")
def FormularioR(request):
    return render (request, "FormularioR.html")
def Validacion(request):
    return render (request, "Validacion.html")
def ValidacionC(request):
    return render (request, "ValidacionC.html")
def Feriados(request):
    return render (request, "Feriados.html")                  
def Registro(request):
    return render (request, "Registro.html")

def form_crear_cliente(request):

    return render(request,'form_crear_cliente.html')

def from_crear_productos(request):

    return render(request,'from_crear_productos.html')


def login(request):

    return render(request,'login.html')




def Mostrarclientes(request):
    cliente = Cliente.objects.all()
 

    datos = {
        'cliente' : cliente
    }
    return render(request, 'Mostrarclientes.html', datos)


def form_cliente(request): 

    if request.method=='POST':
        cliente_form = ClienteForm(request.POST)
        if cliente_form.is_valid():
            cliente_form.save()
            return redirect ('Mostrarclientes.html')
    else:
        cliente_form = ClienteForm()
    return render(request, 'form_crear_cliente.html', {'cliente_form': cliente_form})


def form_modificarcliente(request, id):
    cliente = Cliente.objects.get(rut=id)
    datos = {
        'form': ClienteForm(instance = cliente)
    }
    if request.method=='POST':
        formulario = ClienteForm(data=request.POST, instance = cliente)
        if formulario.is_valid():
            formulario.save()
            return redirect ('Mostrarclientes')
        
    return render(request, 'form_modificarcliente.html', datos)


def form_del_cliente(request,id):
    cliente = Cliente.objects.get(rut=id)
    cliente.delete()
    return redirect('Mostrarclientes')




    


def mostrar_producto(request):
    producto = Producto.objects.all()
 

    datos = {
        'producto' : producto
    }
    return render(request, 'mostrar_producto.html', datos)


def form_producto(request): 

    if request.method=='POST':
        producto_form = ProductoForm(request.POST)
        if producto_form.is_valid():
            producto_form.save()
            return redirect ('mostrar_productos.html')
    else:
        producto_form = ProductoForm()
    return render(request, 'from_crear_productos.html', {'producto_form': producto_form})


def modificar_producto(request, id):
    producto = Producto.objects.get(codigo_barra=id)
    datos = {
        'form': ProductoForm(instance = producto)
    }
    if request.method=='POST':
        formulario = ProductoForm(data=request.POST, instance = producto)
        if formulario.is_valid():
            formulario.save()
            return redirect ('mostrar_producto')
        
    return render(request, 'mostrar_producto.html', datos)


def eliminar_producto(request,id):
    producto = Producto.objects.get(codigo_barra=id)
    producto.delete()
    return redirect('mostrar_producto')