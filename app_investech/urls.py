from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    
    # URLs para Usuario
    path('usuarios/', views.inicio_usuario, name='inicio_usuario'),
    path('usuarios/agregar/', views.agregar_usuario, name='agregar_usuario'),
    path('usuarios/actualizar/<int:usuario_id>/', views.actualizar_usuario, name='actualizar_usuario'),
    path('usuarios/realizar_actualizacion/<int:usuario_id>/', views.realizar_actualizacion_usuario, name='realizar_actualizacion_usuario'),
    path('usuarios/borrar/<int:usuario_id>/', views.borrar_usuario, name='borrar_usuario'),
    
    # URLs para Portafolio
    path('portafolios/', views.inicio_portafolio, name='inicio_portafolio'),
    path('portafolios/agregar/', views.agregar_portafolio, name='agregar_portafolio'),
    path('portafolios/actualizar/<int:portafolio_id>/', views.actualizar_portafolio, name='actualizar_portafolio'),
    path('portafolios/realizar_actualizacion/<int:portafolio_id>/', views.realizar_actualizacion_portafolio, name='realizar_actualizacion_portafolio'),
    path('portafolios/borrar/<int:portafolio_id>/', views.borrar_portafolio, name='borrar_portafolio'),
]