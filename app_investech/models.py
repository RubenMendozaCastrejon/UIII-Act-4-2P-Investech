from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    pais = models.CharField(max_length=50)
    saldo_disponible = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Portafolio(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="portafolios")
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    valor_total = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    riesgo = models.CharField(max_length=50, choices=[('bajo', 'Bajo'), ('medio', 'Medio'), ('alto', 'Alto')])
    activos = models.ManyToManyField('Activo', related_name="portafolios")

    def __str__(self):
        return f"{self.nombre} ({self.usuario.nombre})"

class Activo(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50, choices=[
        ('accion', 'Acción'),
        ('bono', 'Bono'),
        ('cripto', 'Criptomoneda'),
        ('fondo', 'Fondo de inversión'),
        ('otro', 'Otro'),
    ])
    simbolo = models.CharField(max_length=10)
    precio_actual = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    mercado = models.CharField(max_length=100)
    volatilidad = models.DecimalField(max_digits=5, decimal_places=2, help_text="Porcentaje de volatilidad")

    def __str__(self):
        return f"{self.nombre} ({self.simbolo})"