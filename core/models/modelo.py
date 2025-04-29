from django.db import models

class Modelo(models.Model):
    nome = models.TextField()
    marca = models.TextField().null
    categorias = models.TextField().null

    def __str__(self):
        return f"{self.id} - {self.nome} - {self.marca}"