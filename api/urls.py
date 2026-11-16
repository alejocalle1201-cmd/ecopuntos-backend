from django.urls import path, include # Importamos las funciones necesarias para definir URLs en Django
from rest_framework.routers import DefaultRouter # Importamos el enrutador por defecto de Django REST Framework para crear rutas automáticamente
from .views import PuntoAcopioViewSet # Importamos la vista PuntoAcopioViewSet desde el archivo views.py

# El Router crea las direcciones automáticamente para nuestro ViewSet
router = DefaultRouter() # Creamos una instancia del enrutador por defecto
# Al registrar 'puntos', la URL será: /api/puntos/
router.register(r'puntos', PuntoAcopioViewSet) # Registramos la vista PuntoAcopioViewSet en el enrutador con la ruta 'puntos'

urlpatterns = [ # Definimos las URLs de nuestra aplicación
    path('', include(router.urls)), # Incluimos las URLs generadas por el enrutador en la ruta raíz de nuestra aplicación
]