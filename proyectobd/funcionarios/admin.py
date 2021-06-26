from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Funcionario, Marcacion

# Register your models here.
@register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'cedula', 'email', 'telefono', 'direccion', 'fecha_nacimiento', 'activo']
    list_display_links = ['nombre', 'apellido', 'cedula', 'email', 'telefono', 'direccion', 'fecha_nacimiento', 'activo']

#@register(Marcacion)
#class MarcacionAdmin(admin.ModelAdmin):
#    list_display = ['funcionario', 'fecha', 'hora', 'temperatura', 'imagen_tag']
#    list_display = ['funcionario', 'fecha', 'hora', 'temperatura', 'imagen_tag']
