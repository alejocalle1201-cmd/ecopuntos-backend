from django.urls import path, include # Importamos las funciones necesarias para definir URLs en Django
from rest_framework.routers import DefaultRouter # Importamos el enrutador por defecto de Django REST Framework
from .views import PuntoAcopioViewSet, EntregaViewSet # Importamos ambas vistas desde views.py

# El Router crea las direcciones automáticamente para nuestros ViewSets
router = DefaultRouter()

# Al registrar 'puntos', la URL será: /api/puntos/ (Alejandro)
router.register(r'puntos', PuntoAcopioViewSet)

# Al registrar 'entregas', la URL será: /api/entregas/ (Tu parte)
router.register(r'entregas', EntregaViewSet)

urlpatterns = [ # Definimos las URLs de nuestra aplicación
    path('', include(router.urls)), # Incluimos las URLs generadas por el enrutador
]