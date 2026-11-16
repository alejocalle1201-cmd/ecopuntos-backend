from django.db import models

# Create your models here.

# 1. Moldelo para los puntos de reciclaje
class PuntoAcopio(models.Model):
    nombre = models.CharField(max_length=100) # Nombre del punto de reciclaje
    direccion = models.CharField(max_length=200) # Dirección del punto de reciclaje
    # Esta función hace que Django muestre el nombre real del punto
    def __str__(self):
        return self.nombre
    