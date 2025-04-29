from django.db import models

class Acessorios(models.Model):
    descricao = models.TextField(100)

    def __str__(self):
        return f"{self.id} - {self.descricao}"