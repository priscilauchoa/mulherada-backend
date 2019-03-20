from django.db import models

class Vagas(models.model):
    titulo = models.CharField(max_length=50)
    empresa = models.CharField(max_length=20)
    cidade = models.CharField(max_length=20)
    salario = models.DecimalField()
    descricao = models.CharField(max_length=2000)
    contato = models.CharField(CharField(max_length=250)

    def __str__(self):
        return self.profissao