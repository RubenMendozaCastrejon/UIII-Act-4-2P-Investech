Te ayudo a implementar la segunda parte del proyecto con el modelo Portafolio. Voy a crear toda la estructura necesaria:

## 1. Primero, actualicemos el navbar

**app_investech/templates/navbar.html** (actualizado):
```html
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container">
        <a class="navbar-brand" href="{% url 'inicio' %}">
            <i class="fas fa-chart-bar me-2"></i>Investech
        </a>
        
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
            <span class="navbar-toggler-icon"></span>
        </button>
        
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav me-auto">
                <li class="nav-item">
                    <a class="nav-link" href="{% url 'inicio' %}">
                        <i class="fas fa-home me-1"></i>Inicio
                    </a>
                </li>
                
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" id="usuarioDropdown" role="button" data-bs-toggle="dropdown">
                        <i class="fas fa-users me-1"></i>Usuario
                    </a>
                    <ul class="dropdown-menu">
                        <li><a class="dropdown-item" href="{% url 'agregar_usuario' %}">Agregar Usuario</a></li>
                        <li><a class="dropdown-item" href="{% url 'inicio_usuario' %}">Ver Usuario</a></li>
                    </ul>
                </li>
                
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" id="portafolioDropdown" role="button" data-bs-toggle="dropdown">
                        <i class="fas fa-briefcase me-1"></i>Portafolio
                    </a>
                    <ul class="dropdown-menu">
                        <li><a class="dropdown-item" href="{% url 'agregar_portafolio' %}">Agregar Portafolio</a></li>
                        <li><a class="dropdown-item" href="{% url 'inicio_portafolio' %}">Ver Portafolio</a></li>
                        <li><hr class="dropdown-divider"></li>
                        <li><a class="dropdown-item" href="#">Actualizar Portafolio</a></li>
                        <li><a class="dropdown-item" href="#">Borrar Portafolio</a></li>
                    </ul>
                </li>
                
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" id="activoDropdown" role="button" data-bs-toggle="dropdown">
                        <i class="fas fa-coins me-1"></i>Activo
                    </a>
                    <ul class="dropdown-menu">
                        <li><a class="dropdown-item" href="#">Agregar Activo</a></li>
                        <li><a class="dropdown-item" href="#">Ver Activo</a></li>
                        <li><hr class="dropdown-divider"></li>
                        <li><a class="dropdown-item" href="#">Actualizar Activo</a></li>
                        <li><a class="dropdown-item" href="#">Borrar Activo</a></li>
                    </ul>
                </li>
            </ul>
        </div>
    </div>
</nav>
```

## 2. Agregar las vistas para Portafolio

**app_investech/views.py** (agregar estas funciones):
```python
# ... después de las funciones de Usuario ...

def inicio_portafolio(request):
    portafolios = Portafolio.objects.all()
    return render(request, 'portafolio/ver_portafolio.html', {'portafolios': portafolios})

def agregar_portafolio(request):
    if request.method == 'POST':
        usuario_id = request.POST.get('usuario')
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        valor_total = request.POST.get('valor_total', 0.00)
        riesgo = request.POST.get('riesgo')
        
        usuario = Usuario.objects.get(id=usuario_id)
        portafolio = Portafolio(
            usuario=usuario,
            nombre=nombre,
            descripcion=descripcion,
            valor_total=valor_total,
            riesgo=riesgo
        )
        portafolio.save()
        return redirect('inicio_portafolio')
    
    usuarios = Usuario.objects.all()
    return render(request, 'portafolio/agregar_portafolio.html', {'usuarios': usuarios})

def actualizar_portafolio(request, portafolio_id):
    portafolio = get_object_or_404(Portafolio, id=portafolio_id)
    usuarios = Usuario.objects.all()
    return render(request, 'portafolio/actualizar_portafolio.html', {
        'portafolio': portafolio,
        'usuarios': usuarios
    })

def realizar_actualizacion_portafolio(request, portafolio_id):
    if request.method == 'POST':
        portafolio = get_object_or_404(Portafolio, id=portafolio_id)
        usuario_id = request.POST.get('usuario')
        portafolio.usuario = Usuario.objects.get(id=usuario_id)
        portafolio.nombre = request.POST.get('nombre')
        portafolio.descripcion = request.POST.get('descripcion')
        portafolio.valor_total = request.POST.get('valor_total', 0.00)
        portafolio.riesgo = request.POST.get('riesgo')
        portafolio.save()
        return redirect('inicio_portafolio')
    
    return redirect('inicio_portafolio')

def borrar_portafolio(request, portafolio_id):
    portafolio = get_object_or_404(Portafolio, id=portafolio_id)
    if request.method == 'POST':
        portafolio.delete()
        return redirect('inicio_portafolio')
    
    return render(request, 'portafolio/borrar_portafolio.html', {'portafolio': portafolio})
```

## 3. Actualizar las URLs

**app_investech/urls.py** (actualizado):
```python
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
```

## 4. Crear los templates para Portafolio

### agregar_portafolio.html
**app_investech/templates/portafolio/agregar_portafolio.html**:
```html
{% extends 'base.html' %}

{% block content %}
<div class="row">
    <div class="col-md-8 mx-auto">
        <div class="card">
            <div class="card-header bg-success text-white">
                <h4 class="mb-0"><i class="fas fa-briefcase me-2"></i>Agregar Nuevo Portafolio</h4>
            </div>
            <div class="card-body">
                <form method="POST">
                    {% csrf_token %}
                    <div class="mb-3">
                        <label for="usuario" class="form-label">Usuario</label>
                        <select class="form-select" id="usuario" name="usuario" required>
                            <option value="">Seleccionar usuario...</option>
                            {% for usuario in usuarios %}
                            <option value="{{ usuario.id }}">{{ usuario.nombre }} {{ usuario.apellido }}</option>
                            {% endfor %}
                        </select>
                    </div>
                    
                    <div class="mb-3">
                        <label for="nombre" class="form-label">Nombre del Portafolio</label>
                        <input type="text" class="form-control" id="nombre" name="nombre" required>
                    </div>
                    
                    <div class="mb-3">
                        <label for="descripcion" class="form-label">Descripción</label>
                        <textarea class="form-control" id="descripcion" name="descripcion" rows="3"></textarea>
                    </div>
                    
                    <div class="row">
                        <div class="col-md-6 mb-3">
                            <label for="valor_total" class="form-label">Valor Total</label>
                            <input type="number" class="form-control" id="valor_total" name="valor_total" step="0.01" value="0.00">
                        </div>
                        <div class="col-md-6 mb-3">
                            <label for="riesgo" class="form-label">Nivel de Riesgo</label>
                            <select class="form-select" id="riesgo" name="riesgo" required>
                                <option value="">Seleccionar riesgo...</option>
                                <option value="bajo">Bajo</option>
                                <option value="medio">Medio</option>
                                <option value="alto">Alto</option>
                            </select>
                        </div>
                    </div>
                    
                    <div class="d-grid gap-2 d-md-flex justify-content-md-end">
                        <a href="{% url 'inicio_portafolio' %}" class="btn btn-secondary me-md-2">Cancelar</a>
                        <button type="submit" class="btn btn-success">
                            <i class="fas fa-save me-1"></i>Guardar Portafolio
                        </button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>
{% endblock %}
```

### ver_portafolio.html
**app_investech/templates/portafolio/ver_portafolio.html**:
```html
{% extends 'base.html' %}

{% block content %}
<div class="d-flex justify-content-between align-items-center mb-4">
    <h2><i class="fas fa-briefcase me-2"></i>Lista de Portafolios</h2>
    <a href="{% url 'agregar_portafolio' %}" class="btn btn-success">
        <i class="fas fa-plus me-1"></i>Agregar Portafolio
    </a>
</div>

<div class="card">
    <div class="card-body">
        {% if portafolios %}
        <div class="table-responsive">
            <table class="table table-striped table-hover">
                <thead class="table-dark">
                    <tr>
                        <th>ID</th>
                        <th>Nombre</th>
                        <th>Usuario</th>
                        <th>Valor Total</th>
                        <th>Riesgo</th>
                        <th>Fecha Creación</th>
                        <th>Acciones</th>
                    </tr>
                </thead>
                <tbody>
                    {% for portafolio in portafolios %}
                    <tr>
                        <td>{{ portafolio.id }}</td>
                        <td>{{ portafolio.nombre }}</td>
                        <td>{{ portafolio.usuario.nombre }} {{ portafolio.usuario.apellido }}</td>
                        <td>${{ portafolio.valor_total }}</td>
                        <td>
                            <span class="badge 
                                {% if portafolio.riesgo == 'bajo' %}bg-success
                                {% elif portafolio.riesgo == 'medio' %}bg-warning
                                {% else %}bg-danger{% endif %}">
                                {{ portafolio.get_riesgo_display }}
                            </span>
                        </td>
                        <td>{{ portafolio.fecha_creacion|date:"d/m/Y" }}</td>
                        <td>
                            <div class="btn-group btn-group-sm">
                                <a href="#" class="btn btn-info" title="Ver">
                                    <i class="fas fa-eye"></i>
                                </a>
                                <a href="{% url 'actualizar_portafolio' portafolio.id %}" class="btn btn-warning" title="Editar">
                                    <i class="fas fa-edit"></i>
                                </a>
                                <a href="{% url 'borrar_portafolio' portafolio.id %}" class="btn btn-danger" title="Borrar">
                                    <i class="fas fa-trash"></i>
                                </a>
                            </div>
                        </td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
        {% else %}
        <div class="text-center py-4">
            <i class="fas fa-briefcase fa-3x text-muted mb-3"></i>
            <h4>No hay portafolios registrados</h4>
            <p class="text-muted">Comienza agregando el primer portafolio al sistema.</p>
            <a href="{% url 'agregar_portafolio' %}" class="btn btn-success">Agregar Primer Portafolio</a>
        </div>
        {% endif %}
    </div>
</div>
{% endblock %}
```

### actualizar_portafolio.html
**app_investech/templates/portafolio/actualizar_portafolio.html**:
```html
{% extends 'base.html' %}

{% block content %}
<div class="row">
    <div class="col-md-8 mx-auto">
        <div class="card">
            <div class="card-header bg-warning text-dark">
                <h4 class="mb-0"><i class="fas fa-edit me-2"></i>Actualizar Portafolio: {{ portafolio.nombre }}</h4>
            </div>
            <div class="card-body">
                <form method="POST" action="{% url 'realizar_actualizacion_portafolio' portafolio.id %}">
                    {% csrf_token %}
                    <div class="mb-3">
                        <label for="usuario" class="form-label">Usuario</label>
                        <select class="form-select" id="usuario" name="usuario" required>
                            {% for usuario in usuarios %}
                            <option value="{{ usuario.id }}" {% if usuario.id == portafolio.usuario.id %}selected{% endif %}>
                                {{ usuario.nombre }} {{ usuario.apellido }}
                            </option>
                            {% endfor %}
                        </select>
                    </div>
                    
                    <div class="mb-3">
                        <label for="nombre" class="form-label">Nombre del Portafolio</label>
                        <input type="text" class="form-control" id="nombre" name="nombre" value="{{ portafolio.nombre }}" required>
                    </div>
                    
                    <div class="mb-3">
                        <label for="descripcion" class="form-label">Descripción</label>
                        <textarea class="form-control" id="descripcion" name="descripcion" rows="3">{{ portafolio.descripcion }}</textarea>
                    </div>
                    
                    <div class="row">
                        <div class="col-md-6 mb-3">
                            <label for="valor_total" class="form-label">Valor Total</label>
                            <input type="number" class="form-control" id="valor_total" name="valor_total" step="0.01" value="{{ portafolio.valor_total }}">
                        </div>
                        <div class="col-md-6 mb-3">
                            <label for="riesgo" class="form-label">Nivel de Riesgo</label>
                            <select class="form-select" id="riesgo" name="riesgo" required>
                                <option value="bajo" {% if portafolio.riesgo == 'bajo' %}selected{% endif %}>Bajo</option>
                                <option value="medio" {% if portafolio.riesgo == 'medio' %}selected{% endif %}>Medio</option>
                                <option value="alto" {% if portafolio.riesgo == 'alto' %}selected{% endif %}>Alto</option>
                            </select>
                        </div>
                    </div>
                    
                    <div class="d-grid gap-2 d-md-flex justify-content-md-end">
                        <a href="{% url 'inicio_portafolio' %}" class="btn btn-secondary me-md-2">Cancelar</a>
                        <button type="submit" class="btn btn-warning">
                            <i class="fas fa-save me-1"></i>Actualizar Portafolio
                        </button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>
{% endblock %}
```

### borrar_portafolio.html
**app_investech/templates/portafolio/borrar_portafolio.html**:
```html
{% extends 'base.html' %}

{% block content %}
<div class="row">
    <div class="col-md-6 mx-auto">
        <div class="card">
            <div class="card-header bg-danger text-white">
                <h4 class="mb-0"><i class="fas fa-trash me-2"></i>Eliminar Portafolio</h4>
            </div>
            <div class="card-body text-center">
                <i class="fas fa-exclamation-triangle fa-3x text-warning mb-3"></i>
                <h5>¿Estás seguro de que deseas eliminar este portafolio?</h5>
                <p class="text-muted">Esta acción no se puede deshacer.</p>
                
                <div class="card mb-3">
                    <div class="card-body">
                        <h6>{{ portafolio.nombre }}</h6>
                        <p class="mb-1"><strong>Usuario:</strong> {{ portafolio.usuario.nombre }} {{ portafolio.usuario.apellido }}</p>
                        <p class="mb-1"><strong>Valor Total:</strong> ${{ portafolio.valor_total }}</p>
                        <p class="mb-1"><strong>Riesgo:</strong> {{ portafolio.get_riesgo_display }}</p>
                        <p class="mb-0"><strong>Descripción:</strong> {{ portafolio.descripcion|truncatewords:10 }}</p>
                    </div>
                </div>
                
                <form method="POST">
                    {% csrf_token %}
                    <div class="d-grid gap-2 d-md-flex justify-content-md-center">
                        <a href="{% url 'inicio_portafolio' %}" class="btn btn-secondary me-md-2">Cancelar</a>
                        <button type="submit" class="btn btn-danger">Sí, Eliminar Portafolio</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>
{% endblock %}
```

## 5. Actualizar el admin.py

**app_investech/admin.py** (ya debería estar registrado, pero verifica):
```python
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
```

## 6. Ejecutar migraciones

```bash
# Realizar migraciones
python manage.py makemigrations
python manage.py migrate

# Ejecutar servidor
python manage.py runserver 8640
```

## 7. Estructura final de carpetas

```
UIII_investech_0640/
├── app_investech/
│   ├── templates/
│   │   ├── usuario/
│   │   │   ├── agregar_usuario.html
│   │   │   ├── ver_usuario.html
│   │   │   ├── actualizar_usuario.html
│   │   │   └── borrar_usuario.html
│   │   ├── portafolio/                    ← NUEVA CARPETA
│   │   │   ├── agregar_portafolio.html    ← NUEVO
│   │   │   ├── ver_portafolio.html        ← NUEVO
│   │   │   ├── actualizar_portafolio.html ← NUEVO
│   │   │   └── borrar_portafolio.html     ← NUEVO
│   │   ├── base.html
│   │   ├── header.html
│   │   ├── navbar.html
│   │   ├── footer.html
│   │   └── inicio.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── manage.py
```

Ahora el proyecto estará completamente funcional para el modelo Portafolio. Puedes acceder a:
- `http://localhost:8640/portafolios/` para ver la lista
- `http://localhost:8640/portafolios/agregar/` para agregar nuevos portafolios

Los colores son suaves y atractivos, y toda la funcionalidad CRUD está implementada.
