from django.db import models

class Familia(models.Model):
    """
    Estructura de modelo familia

    nombre: Primer nombre de la persona
    apellido: Primer apellido de la persona
    edad: Edad de la persona
    fecha_nacimiento: Fecha de nacimiento de la persona
    """
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    edad=models.IntegerField()
    fecha_nacimiento=models.DateTimeField()
