from django.db import models

# Create your models here.

class Familiar(models.Model):
    nombre=models.CharField(max_length=60)
    apellido=models.CharField(max_length=50)
    edad=models.IntegerField()

    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {str(self.edad)}"


class Direcciones(models.Model):
    calle=models.CharField(max_length=30)
    numero=models.IntegerField()

class Puesto(models.Model):
    profesion=models.CharField(max_length=60)
    antiguedad=models.IntegerField()