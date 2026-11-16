from rest_framework import serializers # Importamos la librería de Django REST Framework para crear serializadores
from .models import PuntoAcopio, Entrega # Importamos ambos modelos desde models.py

# Traductor para el modelo PuntoAcopio (Desarrollado por Alejandro)
class PuntoAcopioSerializer(serializers.ModelSerializer):
    class Meta: # Aquí le decimos a Django que este serializador está relacionado con el modelo PuntoAcopio
        model = PuntoAcopio
        # '__all__' le dice a Django: "Traduce todos los campos de este modelo, 
        # incluyendo el 'id' que se crea automáticamente".
        fields = '__all__'


# Traductor para el modelo Entrega (Tu parte - Incluye la llave foránea punto_acopio)
class EntregaSerializer(serializers.ModelSerializer):
    # Campo adicional de solo lectura para enviar también el nombre del punto de acopio en el JSON
    punto_acopio_nombre = serializers.ReadOnlyField(source='punto_acopio.nombre')

    class Meta:
        model = Entrega
        # '__all__' incluye: id, punto_acopio (la ForeignKey), material, peso_kg, fecha y punto_acopio_nombre
        fields = '__all__'