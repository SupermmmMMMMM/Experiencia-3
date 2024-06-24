from django import forms
from .models import Producto
from PIL import Image
from django.core.files.base import ContentFile
from resizeimage import resizeimage
from io import BytesIO
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Cliente

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Cliente
        fields = ('rut', 'nombre', 'apellido', 'celular', 'direccion', 'password1', 'password2')

class EditarPerfilForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'celular', 'direccion']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'


    def clean_imagen(self):
        imagen = self.cleaned_data.get('imagen')
        if imagen:
            # Abrir la imagen y redimensionarla
            img = Image.open(imagen)
            img = resizeimage.resize_cover(img, [100, 100])
            
            # Guardar la imagen redimensionada en un buffer
            buffer = BytesIO()
            img.save(buffer, format='JPEG')
            buffer.seek(0)
            
            # Sobrescribir el archivo de imagen original con el redimensionado
            imagen = ContentFile(buffer.getvalue(), imagen.name)
            
        return imagen
    
