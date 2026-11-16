from rest_framework import viewsets # Importamos la librería de Django REST Framework para crear vistas basadas en clases
from .models import PuntoAcopio, Entrega # Importamos ambos modelos desde models.py
from .serializers import PuntoAcopioSerializer, EntregaSerializer # Importamos ambos serializadores

# Vista para PuntoAcopio (Desarrollada por Alejandro)
class PuntoAcopioViewSet(viewsets.ModelViewSet):
    # 1. Le decimos a qué datos de la base de datos va a acceder
    queryset = PuntoAcopio.objects.all()
    
    # 2. Le decimos qué traductor va a utilizar para esos datos
    serializer_class = PuntoAcopioSerializer


# Vista para Entrega (Tu parte - CRUD completo con relación ForeignKey)
class EntregaViewSet(viewsets.ModelViewSet):
    # 1. Obtiene todas las entregas registradas en la base de datos
    queryset = Entrega.objects.all()
    
    # 2. Usa EntregaSerializer para convertir las entregas entre Python y JSON
    serializer_class = EntregaSerializer