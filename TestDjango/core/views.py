from django.shortcuts import render, redirect,get_object_or_404
from .models import Producto
from .forms import ProductoForm
<<<<<<< Updated upstream

from django.core.files.base import ContentFile

=======
from django.contrib.auth import login, authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.files.base import ContentFile
from django.contrib.auth.forms import AuthenticationForm
>>>>>>> Stashed changes
from django.urls import reverse

# Create your views here.
def Index(request):
    return render(request,'core/Index.html')
def ofertas(request):
    return render(request,'core/ofertas.html')
def quienes(request):
    return render(request,'core/quienes-somos.html')
def reserva(request):
    return render(request,'core/reserva-pan.html')
def reclamos(request):
    return render(request,'core/reclamos-sugerencias.html')
<<<<<<< Updated upstream

=======
def iniciar_sesion(request):
    return render(request,'core/iniciar-sesion.html')
>>>>>>> Stashed changes


def ingresar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('producto_list')  # Redirige a la lista de productos (debe ser definida en urls.py)
    else:
        form = ProductoForm()
    
    return render(request, 'core/formulario_producto.html', {'form': form})
def producto_list(request):
    productos = Producto.objects.all()
    return render(request, 'core/producto_list.html', {'productos': productos})



def producto_update(request, idProducto):
    producto = get_object_or_404(Producto, idProducto=idProducto)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('producto_list')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'core/formulario_producto.html', {'form': form})


def eliminar_producto(request, idProducto):
    producto = get_object_or_404(Producto, idProducto=idProducto)
    if request.method == 'POST':
        producto.delete()
        return redirect('producto_list')  # Redirige a la lista de productos después de la eliminación
    return render(request, 'core/producto_delete.html', {'producto': producto})

def detalle_producto(request, id):
    producto = get_object_or_404(Producto, idProducto=id)
    return render(request, 'core/detalle_producto.html', {'producto': producto})

<<<<<<< Updated upstream


=======
def registrar_cliente(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password1'))
            login(request, user)
            return redirect('Index')
    else:
        form = UserCreationForm()
    return render(request, 'core/registro.html', {'form': form})
>>>>>>> Stashed changes
