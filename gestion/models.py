from django.db import models
from django.urls import reverse
# Create your models here.


class Genero(models.Model):
    """Modelo que representa el sexo del usuario."""
    name = models.CharField(max_length=200,
                              help_text="Seleccione un genero")

    def __str__(self):
        return self.name


class EstadoCivil(models.Model):
    """Modelo que representa el estado civil de un usuario."""
    name = models.CharField(
        max_length=200,
        help_text="Seleccione un estado civil"
    )

    def __str__(self):
        return self.name


class Usuario(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    password = models.CharField(max_length=50, default='1234')

    class Meta:
        ordering = ['username', 'email', 'nombre', 'apellido', ]

    def get_absolute_url(self):
        return reverse('usuario-detail', args=[str(self.id)])

    def __str__(self):
        return self.username


class Tema(models.Model):
    nombre = models.CharField(max_length=20)
    fecha_creacion = models.DateField(null=True, blank=True)
    fecha_modificacion = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['nombre', 'fecha_creacion', 'fecha_modificacion', ]

    def __str__(self):
        return self.nombre


class SeccionIndividual(models.Model):
    titulo = models.CharField(max_length=100)
    texto = models.TextField(max_length=2000)
    fecha_modificacion = models.DateField(null=True, blank=True)
    fecha_creacion = models.DateField(null=True, blank=True)
    id_fk_usuario = models.ForeignKey(
        Usuario, on_delete=models.CASCADE, null=True)
    id_fk_tema = models.ForeignKey(Tema, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['titulo', 'texto',
                    'fecha_modificacion', 'fecha_creacion', ]

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return self.titulo


class Distrito(models.Model):
    nombre = models.CharField(max_length=20)
    numero = models.IntegerField()

    class Meta:
        ordering = ['nombre', 'numero', ]

    def __str__(self):
        return self.nombre


class Comuna(models.Model):
    nombre = models.CharField(max_length=20)
    region = models.CharField(max_length=20)
    distrito = models.ForeignKey(
        Distrito, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['nombre', 'region', ]

    def __str__(self):
        return self.nombre


class Rol(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(default='Ingrese un breve descripcion')

    class Meta:
        ordering = ['nombre', 'descripcion', ]

    def __str__(self):
        return self.nombre


class Asamblea(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(
        max_length=300, default='Ingrese un breve descripcion')
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=60)
    direccion_calle = models.CharField(max_length=20)
    direccion_numero = models.IntegerField()
    fecha_creacion = models.DateField(null=True, blank=True)
    fecha_modificacion = models.DateField(null=True, blank=True)
    id_fk_comuna = models.ForeignKey(
        Comuna, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['nombre', 'telefono',
                    'fecha_modificacion', 'fecha_creacion', ]

    def __str__(self):
        return self.nombre


class Perfil(models.Model):
    usuario = models.OneToOneField( Usuario, on_delete=models.CASCADE, primary_key=True)
    es_representante = models.CharField(max_length=10)
    rut = models.CharField(max_length=10)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, null=False)
    asamblea = models.ForeignKey(Asamblea, on_delete=models.CASCADE, null=False)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, null=False)
    genero = models.ManyToManyField(Genero, help_text="Seleccione Genero/Sexo")
    calle = models.CharField(max_length=20)
    numero_casa = models.IntegerField()
    fecha_creacion = models.DateField(null=True, blank=True)
    fecha_modificacion = models.DateField(null=True, blank=True)
    estado_civil = models.ManyToManyField(EstadoCivil, help_text="Seleccione Estado Civil")
    resumen = models.TextField(default='Ingrese un breve resumen')

    def display_genero(self):
        """Creates a string for the Genre. This is required to display genre in Admin."""
        return ', '.join([genero.name for genero in self.genero.all()[:3]])

    display_genero.short_description = 'Genero'

    class Meta:
        ordering = ['usuario',
                    'fecha_modificacion', 'fecha_creacion', ]

    def get_absolute_url(self):
        """Retorna la url para acceder a una instancia de perfil en particular"""
        return reverse('perfil-detail', args=[str(self.id)])

    def __str__(self):
        return '{0}, {1}'.format(self.usuario.username, self.nombre)


class PropuestaAsamblea(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(
        max_length=300, default='Ingrese un breve descripcion')
    fecha_creacion = models.DateField(null=True, blank=True)
    fecha_modificacion = models.DateField(null=True, blank=True)
    asamblea = models.OneToOneField(
        Asamblea, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        ordering = ['titulo', 'fecha_creacion', 'fecha_modificacion', ]

    def __str__(self):
        return self.titulo


class AprobacionPA(models.Model):
    tipo = models.CharField(max_length=50, default='aprueba o rechaza')
    comentario = models.TextField(default='Ingrese un breve comentario')
    fecha_creacion = models.DateField(null=True, blank=True)
    fecha_modificacion = models.DateField(null=True, blank=True)
    propuesta_asamblea = models.ForeignKey(
        PropuestaAsamblea, on_delete=models.CASCADE, null=True)
    usuario = models.OneToOneField(
        Usuario, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        ordering = ['tipo', 'fecha_modificacion', 'fecha_creacion', ]

    def __str__(self):
        return self.tipo


class Seccion(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField(max_length=2000, default='Ingrese um texto')
    fecha_creacion = models.DateField(null=True, blank=True)
    fecha_modificacion = models.DateField(null=True, blank=True)
    propuesta_asamblea = models.ForeignKey(
        PropuestaAsamblea, on_delete=models.CASCADE, null=True)
    Tema = models.ForeignKey(Tema, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['titulo', 'fecha_creacion', 'fecha_modificacion', ]

    def __str__(self):
        return self.titulo
