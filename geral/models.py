from django.db import models

class produto(models.Model):
    nome = models.CharField(max_length=30)
    preco = models.CharField(max_length=30)
    quantidade = models.CharField(max_length=30)



