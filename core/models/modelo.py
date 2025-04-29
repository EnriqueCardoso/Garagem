from django.db import models

class Modelo(models.Model):
    nome = models.TextField(80)
    marca = models.TextField(80).null
    categorias = models.TextField(80).null

    def __str__(self):
        return f"{self.id} - {self.nome.upper()} - {self.marca.upper()}"