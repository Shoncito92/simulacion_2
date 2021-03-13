from django.contrib import admin

# Register your models here.

from .models import Usuario, Perfil, Genero, EstadoCivil


admin.site.register(Genero)
admin.site.register(EstadoCivil)
admin.site.register(Usuario)





class UsuarioAdmin(admin.ModelAdmin):
    """Administration object for Author models.
    Defines:
     - fields to be displayed in list view (list_display)
     - orders fields in detail view (fields),
       grouping the date fields horizontally
     - adds inline addition of books in author view (inlines)
    """
    list_display = ('apellido',
                    'nombre')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]



class PerfilAdmin(admin.ModelAdmin):
    """Administration object for Book models.
    Defines:
     - fields to be displayed in list view (list_display)
     - adds inline addition of book instances in book view (inlines)
    """
    list_display = ('usuario', 'email', 'rut')



admin.site.register(Perfil, PerfilAdmin)
