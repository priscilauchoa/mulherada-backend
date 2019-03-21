from django.db import models

class Vagas(models.Model):
    titulo = models.CharField(max_length=50)
    empresa = models.CharField(max_length=20)
    cidade = models.CharField(max_length=20)
    salario = models.DecimalField(decimal_places=2, max_digits=10)
    descricao = models.CharField(max_length=2000)
    contato = models.CharField(max_length=250)
