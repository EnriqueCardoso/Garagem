from django.db import models

class Acessorios(models.Model):
    nome = models.TextField()

    def __str__(self):
        return f"{self.id} - {self.nome}"