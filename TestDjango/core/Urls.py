from django.urls import path
from .views import Index,ofertas,quienes,reserva,reclamos
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Index, name='Index'),
    path('ofertas', views.ofertas, name='ofertas'),
    path('quienes', views.quienes, name='quienes'),
    path('reserva', views.reserva, name='reserva'),
    path('reclamos', views.reclamos, name='reclamos'),
    path('productos/<int:idProducto>/', views.detalle_producto, name='detalle_producto'),
    path('productos/', views.producto_list, name='producto_list'),
    path('productos/<int:idProducto>/editar/', views.producto_update, name='producto_update'),
    path('productos/<int:idProducto>/eliminar/', views.producto_delete, name='producto_delete'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('productos/nuevo/', views.nuevo_producto, name='nuevo_producto'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),
   # path('comprar/<int:id>/', views.comprar_producto, name='comprar_producto'),
    path('productos/', views.ver_productos, name='ver_productos'),
    path('profile/', views.user_profile, name='profile'),
    path('logout/', views.user_logout, name='logout'),
    path('carrito/agregar/<int:idProducto>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('carrito/eliminar/<int:item_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('realizar-compra/', views.realizar_compra, name='realizar_compra'),
    path('boleta/<int:boleta_id>/', views.ver_boleta, name='ver_boleta'),
    path('carrito/actualizar/<int:item_id>/', views.actualizar_cantidad, name='actualizar_cantidad'),
]