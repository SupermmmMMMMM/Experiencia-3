from django.shortcuts import render

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
