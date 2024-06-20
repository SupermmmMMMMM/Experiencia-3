from django.urls import path
from .views import Index,ofertas,quienes,reserva,reclamos
from django.contrib import admin
from django.urls import path, include
urlpatterns =[
    path('',Index,name="Index"),
    path('ofertas',ofertas,name="ofertas"),
    path('quienes',quienes,name="quienes"),
    path('reserva',reserva,name="reserva"),
    path('reclamos',reclamos,name="reclamos")
]