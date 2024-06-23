from django.contrib import admin
<<<<<<< Updated upstream
from .models import Producto



admin.site.register(Producto)
# Register your models here.
=======
from django.contrib.auth.admin import UserAdmin
from .models import Cliente, Producto

class ClienteAdmin(UserAdmin):
    list_display = ('rut', 'nombre', 'apellido', 'celular', 'direccion', 'is_admin')
    search_fields = ('rut', 'nombre', 'apellido')
    readonly_fields = ('rut',)
    ordering = ('rut',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Producto)
>>>>>>> Stashed changes
