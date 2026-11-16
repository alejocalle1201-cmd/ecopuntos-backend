from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), # Ruta para acceder al panel de administración de Django
    # Conectamos las rutas principales con las rutas de tu app "api"
    path('api/', include('api.urls')), # Incluimos las URLs definidas en la aplicación "api" bajo la ruta 'api/'
]
