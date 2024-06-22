from django.shortcuts import render, redirect,get_object_or_404
from .models import Producto
from .forms import ProductoForm

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



def ingresar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producto_list')  # Redirige a la lista de productos (debe ser definida en urls.py)
    else:
        form = ProductoForm()
    
    return render(request, 'core/formulario_producto.html', {'form': form})
def producto_list(request):
    productos = Producto.objects.all()
    return render(request, 'core/producto_list.html', {'productos': productos})

def producto_create(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('producto_list')
    else:
        form = ProductoForm()
    return render(request, 'core/formulario_producto.html', {'form': form})

def producto_update(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('producto_list')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'core/formulario_producto.html', {'form': form})


def producto_delete(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('producto_list')
    return render(request, 'core/producto_confirm_delete.html', {'producto': producto})
def detalle_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'core/detalle_producto.html', {'producto': producto})