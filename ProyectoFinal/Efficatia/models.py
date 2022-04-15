from django.db import models
from django.forms import CharField

# Create your models here.

class Consulta(models.Model):
    nombre=models.CharField(max_length=30)
    email=models.EmailField()
    consultaa=models.CharField(max_length= 500)

    def __str__(self) -> str:
        return f'{self.nombre}, {self.email}, {self.consulta}'