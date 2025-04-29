from django.db import models

class Acessorios(models.Model):
    descricao = models.TextField(max_length=100)

    def __str__(self):
        return f"{self.id} - {self.descricao}"