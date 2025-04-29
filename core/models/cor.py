from django.db import models

class Cor(models.Model):
    nome = models.TextField(max_length=40)

    def __str__(self):
        return f"{self.id} - {self.nome}"