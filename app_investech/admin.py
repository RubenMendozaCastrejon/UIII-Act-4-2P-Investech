from django.contrib import admin
from .models import Usuario, Portafolio, Activo

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'pais', 'saldo_disponible', 'fecha_registro')
    list_filter = ('pais', 'fecha_registro')
    search_fields = ('nombre', 'apellido', 'email')

@admin.register(Portafolio)
class PortafolioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'usuario', 'valor_total', 'riesgo', 'fecha_creacion')
    list_filter = ('riesgo', 'fecha_creacion')

@admin.register(Activo)
class ActivoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'simbolo', 'tipo', 'precio_actual', 'mercado')
    list_filter = ('tipo', 'mercado')