from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

<<<<<<< Updated upstream

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




=======
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
>>>>>>> Stashed changes
