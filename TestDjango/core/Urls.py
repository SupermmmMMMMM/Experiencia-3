from django.urls import path
from .views import Index,ofertas,quienes,reserva,reclamos
from .views import iniciar_sesion,registrar_cliente
from django.urls import path, include
from . import views
urlpatterns =[
    path('',Index,name="Index"),
    path('ofertas',ofertas,name="ofertas"),
    path('quienes',quienes,name="quienes"),
    path('reserva',reserva,name="reserva"),
    path('reclamos',reclamos,name="reclamos"),
    
    # core/urls.py

    path('<int:id>/', views.detalle_producto, name='detalle_producto'),
    
    path('ola', views.ingresar_producto, name='nuevo_producto'),

     path('list/', views.producto_list, name='producto_list'),
   
    path('productos/<int:idProducto>/editar/', views.producto_update, name='producto_update'),
    path('productos/<int:idProducto>/eliminar/', views.eliminar_producto, name='producto_delete'),
     
 
    # Otras URLs si las tienes
<<<<<<< Updated upstream
]

=======
    path('iniciar_sesion/', iniciar_sesion, name='iniciar_sesion'),
    path('registro/', registrar_cliente, name='registro'),
]
>>>>>>> Stashed changes
