from rest_framework import serializers # Importamos la librería de Django REST Framework para crear serializadores
from .models import PuntoAcopio # Importamos el modelo PuntoAcopio desde el archivo models.py

# Traductor para el modelo PuntoAcopio (Desarrollado por ti)
class PuntoAcopioSerializer(serializers.ModelSerializer):
    class Meta: # Aquí le decimos a Django que este serializador está relacionado con el modelo PuntoAcopio
        model = PuntoAcopio #
        # '__all__' le dice a Django: "Traduce todos los campos de este modelo, 
        # incluyendo el 'id' que se crea automáticamente".
        fields = '__all__'