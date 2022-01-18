from django.db import models
from django.utils.timezone import now
# Create your models here.

class Inquilinos(models.Model):
    nome = models.CharField(max_length=255)
    idade = models.CharField(max_length=3)
    sexo = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    email = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Unidades(models.Model):
    identicacao = models.CharField(max_length=255)
    proprietario = models.CharField(max_length=3)
    condominio = models.CharField(max_length=100)
    endereco = models.CharField(max_length=15)

    def __str__(self):
        return self.identicacao

class Despesa(models.Model):
    unidade = models.CharField(max_length=255)
    descricao = models.TextField()
    tipo_despesa = models.CharField(max_length=3)
    valor = models.FloatField()
    vencimento_fatura = models.DateField(default=now)
    status_pagamento = models.CharField(max_length=255)

    def __str__(self):
        return self.unidade


