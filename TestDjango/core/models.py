from django.db import models


class Producto(models.Model):
    idProducto=models.IntegerField(primary_key=True,verbose_name='id del producto')
    nombre=models.CharField(max_length=30,verbose_name='nombre del producto')
    descripcion=models.CharField(max_length=50,verbose_name='descripcion del producto')
    imagen=models.ImageField(upload_to="Producto",null=True)
    precio=models.IntegerField(verbose_name='precio del producto')
    stock=models.IntegerField(verbose_name='stock del producto')
    categoria=models.CharField(max_length=20,verbose_name='categoria del producto')



    
        
    def __str__(self):
        return self.nombre




