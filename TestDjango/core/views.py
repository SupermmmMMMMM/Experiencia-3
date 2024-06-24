from django.shortcuts import render, redirect,get_object_or_404
from .models import Producto, Carrito, ItemCarrito, Boleta, DetalleBoleta
from .forms import ProductoForm,UserProfileForm,CustomUserCreationForm,EditarPerfilForm
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.db.models import F
from django.contrib import messages

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

def nuevo_producto(request):
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


def producto_delete(request, idProducto):
    producto = get_object_or_404(Producto, idProducto=idProducto)
    if request.method == 'POST':
        producto.delete()
        return redirect('producto_list')  # Redirige a la lista de productos después de la eliminación
    return render(request, 'core/producto_delete.html', {'producto': producto})

def detalle_producto(request, idProducto):
    producto = get_object_or_404(Producto, idProducto=idProducto)
    return render(request, 'core/detalle_producto.html', {'producto': producto})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('Index')  # Redirige a la página principal después del registro
    else:
        form = CustomUserCreationForm()
    return render(request, 'core/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form})

def es_admin(user):
    return user.is_admin

@login_required
@user_passes_test(es_admin)
def admin_dashboard(request):
    # Lógica para el dashboard de administrador
    return render(request, 'core/admin_dashboard.html')


@login_required
def user_profile(request):
    usuario = request.user
    return render(request, 'core/profile.html', {'usuario': usuario})

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditarPerfilForm(instance=request.user)
    return render(request, 'core/editar_perfil.html', {'form': form})


def ver_productos(request):
    productos = Producto.objects.all()
    return render(request, 'core/ver_productos.html', {'productos': productos})

def user_logout(request):
    logout(request)
    return redirect('Index')

@login_required
def agregar_al_carrito(request, idProducto):
    producto = get_object_or_404(Producto, idProducto=idProducto)
    carrito, created = Carrito.objects.get_or_create(cliente=request.user)
    item, item_created = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)
    
    if item.cantidad < producto.stock:
        if not item_created:
            item.cantidad = F('cantidad') + 1
            item.save()
        messages.success(request, "Producto añadido al carrito.")
    else:
        messages.error(request, "No hay suficiente stock disponible.")
    
    return redirect('ver_carrito')

@login_required
def actualizar_cantidad(request, item_id):
    item = get_object_or_404(ItemCarrito, id=item_id, carrito__cliente=request.user)
    nueva_cantidad = int(request.POST.get('cantidad', 1))
    
    if nueva_cantidad > 0 and nueva_cantidad <= item.producto.stock:
        item.cantidad = nueva_cantidad
        item.save()
        messages.success(request, "Cantidad actualizada.")
    else:
        messages.error(request, "Cantidad no válida o insuficiente stock.")
    
    return redirect('ver_carrito')

@login_required
def ver_carrito(request):
    carrito, created = Carrito.objects.get_or_create(cliente=request.user)
    items = carrito.items.all()
    total = sum(item.producto.precio * item.cantidad for item in items)
    return render(request, 'core/carrito.html', {'items': items, 'total': total})

@login_required
def eliminar_del_carrito(request, item_id):
    item = get_object_or_404(ItemCarrito, id=item_id, carrito__cliente=request.user)
    item.delete()
    return redirect('ver_carrito')

@login_required
def realizar_compra(request):
    carrito, created = Carrito.objects.get_or_create(cliente=request.user)
    items = carrito.items.all()
    
    if not items:
        return redirect('ver_carrito')
    
    for item in items:
        if item.cantidad > item.producto.stock:
            messages.error(request, f"No hay suficiente stock para {item.producto.nombre}")
            return redirect('ver_carrito')
    
    total = sum(item.producto.precio * item.cantidad for item in items)
    
    boleta = Boleta.objects.create(cliente=request.user, total=total)
    
    for item in items:
        DetalleBoleta.objects.create(
            boleta=boleta,
            producto=item.producto,
            cantidad=item.cantidad,
            precio_unitario=item.producto.precio
        )
        
        # Descontar stock
        item.producto.stock -= item.cantidad
        item.producto.save()
    
    # Limpiar el carrito
    carrito.delete()
    
    messages.success(request, "Compra realizada con éxito.")
    return redirect('ver_boleta', boleta_id=boleta.id)


@login_required
def ver_boleta(request, boleta_id):
    boleta = get_object_or_404(Boleta, id=boleta_id, cliente=request.user)
    return render(request, 'core/boleta.html', {'boleta': boleta})

def carrito_items_count(request):
    if request.user.is_authenticated:
        carrito, created = Carrito.objects.get_or_create(cliente=request.user)
        return {'carrito_items_count': carrito.items.count()}
    return {'carrito_items_count': 0}