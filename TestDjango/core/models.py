from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth import get_user_model
import os



class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True, verbose_name='ID del producto')
    nombre = models.CharField(max_length=30, verbose_name='Nombre del producto')
    descripcion = models.CharField(max_length=50, verbose_name='Descripción del producto')
    imagen = models.ImageField(upload_to="Producto", null=True)
    precio = models.IntegerField(verbose_name='Precio del producto')
    stock = models.IntegerField(verbose_name='Stock del producto')
    categoria = models.CharField(max_length=20, verbose_name='Categoría del producto')

    def __str__(self):
        return self.nombre
    def delete(self, *args, **kwargs):
        if self.imagen:
            if os.path.isfile(self.imagen.path):
                os.remove(self.imagen.path)
        super().delete(*args, **kwargs)

class ClienteManager(BaseUserManager):
    def create_user(self, rut, nombre, apellido, celular, direccion, password=None):
        if not rut:
            raise ValueError('El usuario debe tener un RUT')
        
        user = self.model(
            rut=rut,
            nombre=nombre,
            apellido=apellido,
            celular=celular,
            direccion=direccion,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, rut, nombre, apellido, celular, direccion, password=None):
        user = self.create_user(
            rut=rut,
            nombre=nombre,
            apellido=apellido,
            celular=celular,
            direccion=direccion,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class Cliente(AbstractBaseUser):
    rut = models.CharField(max_length=12, primary_key=True, unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    celular = models.CharField(max_length=15)
    direccion = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = ClienteManager()

    USERNAME_FIELD = 'rut'
    REQUIRED_FIELDS = ['nombre', 'apellido', 'celular', 'direccion']

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
Cliente = get_user_model()

class Carrito(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    creado_en = models.DateTimeField(auto_now_add=True)

class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, related_name='items', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

class Boleta(models.Model):
    ESTADO_CHOICES = [
        ('recibido', 'Recibido'),
        ('en_proceso', 'En Proceso'),
        ('enviado', 'Enviado'),
        ('entregado', 'Entregado'),
    ]
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_compra = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='recibido')
    total = models.DecimalField(max_digits=10, decimal_places=2)

class DetalleBoleta(models.Model):
    boleta = models.ForeignKey(Boleta, related_name='detalles', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)