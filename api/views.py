from rest_framework import viewsets # Importamos la librería de Django REST Framework para crear vistas basadas en clases
from .models import PuntoAcopio # Importamos el modelo PuntoAcopio desde el archivo models.py
from .serializers import PuntoAcopioSerializer # Importamos el serializador PuntoAcopioSerializer desde el archivo serializers.py

# Vista para PuntoAcopio (Tu parte del CRUD completo)
class PuntoAcopioViewSet(viewsets.ModelViewSet): # esto significa que vamos a crear una vista basada en clases que nos permitirá hacer operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre el modelo PuntoAcopio
    # 1. Le decimos a qué datos de la base de datos va a acceder
    queryset = PuntoAcopio.objects.all()
    
    # 2. Le decimos qué traductor va a utilizar para esos datos
    serializer_class = PuntoAcopioSerializer