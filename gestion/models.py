from django.db import models

# Create your models here.

class SeccionIndividual(models.Model):
    titulo = models.CharField(max_length=100)
    texto = models.TextField(max_length=2000)
    fecha_modificacion = models.DateField(null=True, blank=True)
    fecha_creacion = models.DateField( null=True, blank=True)
    id_fk_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, null=True) '''clave foranea desde Usuario'''
    id_fk_tema = models.ForeignKey('Tema', on_delete=models.CASCADE, null=True) '''clave foranea desde Tema'''
    
    class Meta:
        ordering = ['titulo', 'texto', 'fecha_modificacion', 'fecha_creacion', ]

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return '{0}, {1}'.format(self.last_name, self.first_name)
    
class Usuario(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    password = models.CharField(max_length=50, default='1234')
    
    class Meta:
            ordering = ['username', 'email', 'nombre', 'apellido', ]
    
class Perfil(models.Model):
    rut = models.CharField(max_length=10)
    resumen = models.TextField(default='Ingrese un breve resumen')
    email = models.EmailField(max_length=60)
    sexo = models.CharField(max_length=10)
    estado_civil = models.CharField(max_length=10)
    direccion_calle = models.CharField(max_length=20)
    direccion_numero = models.IntegerField(max_length=5)
    es_representante = models.CharField(max_length=10)
    fecha_creacion = models.DateField( null=True, blank=True)
    fecha_modificacion = models.DateField( null=True, blank=True)
    id_fk_Asamblea = models.ForeignKey('Asamblea', on_delete=models.CASCADE, null=True) '''clave foranea desde Tema'''
    id_fk_rol = models.ForeignKey('Rol', on_delete=models.CASCADE, null=True) '''clave foranea desde Tema'''
    id_fk_comuna = models.ForeignKey('comuna', on_delete=models.CASCADE, null=True) '''clave foranea desde Tema'''
    usuario = models.OneToOneField ('Usuario', on_delete = models.CASCADE, primary_key = True)

    class Meta:
        ordering = ['usuario', 'sexo', 'fecha_modificacion', 'fecha_creacion', ]
        
class Rol(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(default='Ingrese un breve descripcion')
    
    class Meta:
        ordering = ['nombre', 'descripcion', ]

class AprobacionPA(models.Model):
    tipo = models.CharField(max_length=50, default='aprueba o rechaza')
    comentario = models.TextField(default='Ingrese un breve comentario')
    fecha_creacion = models.DateField( null=True, blank=True)
    fecha_modificacion = models.DateField( null=True, blank=True)
    id_fk_propuesta_asamblea = models.ForeignKey('PropuestaAsamblea', on_delete=models.CASCADE, null=True) '''clave foranea desde Tema'''
    usuario = models.OneToOneField ('Usuario', on_delete = models.CASCADE, primary_key = True)
    
    class Meta:
        ordering = ['tipo', 'fecha_modificacion', 'fecha_creacion', ]
        
class Asamblea(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=300, default='Ingrese un breve descripcion')
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=60)
    direccion_calle = models.CharField(max_length=20)
    direccion_numero = models.IntegerField(max_length=5)
    fecha_creacion = models.DateField( null=True, blank=True)
    fecha_modificacion = models.DateField( null=True, blank=True)
    id_fk_comuna = models.ForeignKey('Comuna', on_delete=models.CASCADE, null=True) '''clave foranea desde Tema'''
    
    class Meta:
        ordering = ['nombre', 'telefono', 'fecha_modificacion', 'fecha_creacion', ]
        
class Comuna(models.Model):
    nombre = models.CharField(max_length=20)
    region = models.CharField(max_length=20)
    id_fk_distrito = models.ForeignKey('Distrito', on_delete=models.CASCADE, null=True) '''clave foranea desde Tema'''
    
    class Meta:
        ordering = ['nombre', 'region', ]
        
class Distrito(models.Model):
    nombre = models.CharField(max_length=20)
    numero = models.IntegerField(max_length=5)
    
    class Meta:
        ordering = ['nombre', 'numero', ]
    
class PropuestaAsamblea(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=300, default='Ingrese un breve descripcion')
    fecha_creacion = models.DateField( null=True, blank=True)
    fecha_modificacion = models.DateField( null=True, blank=True)
    asamblea = models.OneToOneField ('Asamblea', on_delete = models.CASCADE, primary_key = True)
    
    class Meta:
        ordering = ['titulo', 'fecha_creacion', 'fecha_modificacion', ]
        
class Seccion(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField(max_length=2000, default='Ingrese um texto')
    fecha_creacion = models.DateField( null=True, blank=True)
    fecha_modificacion = models.DateField( null=True, blank=True)
    id_fk_propuesta_asamblea = models.ForeignKey('PropuestaAsamblea', on_delete=models.CASCADE, null=True) '''clave foranea desde Tema'''
    id_fk_tema = models.ForeignKey('Tema', on_delete=models.CASCADE, null=True) '''clave foranea desde Tema'''

    class Meta:
        ordering = ['titulo', 'fecha_creacion', 'fecha_modificacion', ]
        
class Tema(models.Model):
    nombre = models.CharField(max_length=20)
    fecha_creacion = models.DateField( null=True, blank=True)
    fecha_modificacion = models.DateField( null=True, blank=True)
    
    class Meta:
        ordering = ['nombre', 'fecha_creacion', 'fecha_modificacion', ]
    