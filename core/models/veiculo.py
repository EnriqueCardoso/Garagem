from django.db import models

class Veiculo(models.Model):
    ano = models.IntegerField(default=0).null
    preco = models.DecimalField(max_digits=10, decimal_places=2).null
    modelo = models.ForeignKey('Modelo', on_delete=models.CASCADE)
    cor = models.ForeignKey('Cor', on_delete=models.CASCADE)
    acessorios = models.ManyToManyField('Acessorios', blank=True)

    def __str__(self):
        return f"{self.id} - {self.modelo.nome.upper()} - {self.cor.nome.upper()} - {self.ano}"