from django.db import models
from django.forms import CharField

# Create your models here.

class Consulta(models.Model):
    nombre=models.CharField(max_length=30)
    email=models.EmailField()
    consultaa=models.CharField(max_length= 500)

    def __str__(self) -> str:
        return f'{self.nombre}, {self.email}, {self.consultaa}'

class Cliente(models.Model):
    nombre=models.CharField(max_length=30)
    email=models.EmailField()
    empresa=models.CharField(max_length= 500)

class Lote(models.Model):
    campo=models.CharField(max_length=30)
    lote=models.CharField(max_length=30)
    id_cliente=models.ForeignKey(Cliente, on_delete=models.CASCADE)
    link=models.CharField(max_length=1000, blank=True, null=True)

