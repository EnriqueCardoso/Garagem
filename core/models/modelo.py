from django.db import models

class Modelo(models.Model):
    nome = models.TextField(max_length=80)
    marca = models.TextField(max_length=80, null=True, blank=True)
    categorias = models.TextField(max_length=80, null=True, blank=True)

    def __str__(self):
        return f"{self.id} - {self.nome.upper()} - {self.marca.upper()}"