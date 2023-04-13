from django.db import models
from django.utils import timezone

# Create your models here.
class Paciente(models.Model):
    nomedoPaciente = models.CharField(max_length=255)
    sobreNome = models.CharField(max_length=255)
    nomeClinica =  models.CharField(max_length=255)
    idadePaciente =  models.CharField(max_length=3)

    def __str__(self) -> str:
        return self.nomedoPaciente

class Form(models.Model):
    
    dado_paciente = models.ForeignKey(Paciente, on_delete=models.DO_NOTHING)

    mutacaoGenetica =  models.CharField(max_length=5)
    opc_bilateral = models.CharField(max_length=5)
    opc_ovario = models.CharField(max_length=5)


    cancer_mama = models.CharField(max_length=5)
    cancer_diagnostico =  models.CharField(max_length=5)
    cancer_histologico = models.CharField(max_length=5)


    tipo_molecular = models.CharField(max_length=5)
    tam_cancer = models.CharField(max_length=5)
    qtd_parent_1 = models.CharField(max_length=5)
    qtd_parent_2 = models.CharField(max_length=5)

    parent_seg_grau =  models.CharField(max_length=5)
    parent_pri_grau =  models.CharField(max_length=5)


    asc_judia =  models.CharField(max_length=5)

    def __str__(self) -> str:
        return self.dado_paciente



    



    