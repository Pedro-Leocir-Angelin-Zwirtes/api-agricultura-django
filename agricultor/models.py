from django.db import models

class Agricultor(models.Model):

    nome = models.CharField(max_length=180)
    cpf = models.CharField(max_length=11, unique=True)
    telefone = models.CharField(max_length=13)
    data_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome