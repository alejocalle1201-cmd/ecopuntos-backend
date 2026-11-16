from django.db import models

# Create your models here.

# 1. Modelo para los puntos de reciclaje (Creado por Alejandro)
class PuntoAcopio(models.Model):
    nombre = models.CharField(max_length=100) # Nombre del punto de reciclaje
    direccion = models.CharField(max_length=200) # Dirección del punto de reciclaje

    # Esta función hace que Django muestre el nombre real del punto
    def __str__(self):
        return self.nombre


# 2. Modelo para las entregas de material reciclable (Tu parte - Relación 1 a Muchos)
class Entrega(models.Model):
    # Llave foránea (ForeignKey): Conecta cada Entrega con un PuntoAcopio
    punto_acopio = models.ForeignKey(
        PuntoAcopio,
        on_delete=models.CASCADE,
        related_name='entregas'
    )
    material = models.CharField(max_length=100) # Tipo de material (Ej: Plástico, Cartón, Vidrio)
    peso_kg = models.FloatField() # Cantidad entregada en kilogramos
    fecha = models.DateField(auto_now_add=True) # Guarda automáticamente la fecha en que se registra

    # Esta función hace que Django muestre una descripción clara de la entrega
    def __str__(self):
        return f"{self.material} ({self.peso_kg} kg) - {self.punto_acopio.nombre}"