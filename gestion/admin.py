from django.contrib import admin
from .models import Usuario, Perfil, Genero, EstadoCivil
# Register your models here.

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'nombre', 'apellido','email')
    fields = ('username', 'email', 'nombre', 'apellido',)

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'rut')
    fields =('usuario', 'es_representante', 'rut', 'rol', 'asamblea', 'comuna', 'genero', 'calle', 'numero_casa', 'fecha_creacion', 'fecha_modificacion', 'estado_civil', 'resumen', )