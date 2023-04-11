from django.db import models

# Create your models here.


# class  cliente, contem os dados do cliente que consultado
class Cliente(models.Model):
    nome =models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nome


#Classe perguntas referente ao paciente.
class Pergunta(models.Model):
    titulo = models.CharField(max_length=200)
    peso = models.IntegerField()
    cliente = models.ForeignKey(Cliente,on_delete=models.DO_NOTHING)


    def __str__(self) -> str:
        return self.titulo
