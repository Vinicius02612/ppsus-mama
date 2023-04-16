from django.db import models
from django.utils import timezone

# Create your models here.

""" Furmulario referente as questões para treinar o modelo """
class Form(models.Model):
    nomePaciente = models.CharField(max_length=255, blank=False)
    sobrenome = models.CharField(max_length=255, blank=False)
    nomeclinica =  models.CharField(max_length=255, blank=False)

    tuplesexo = (
        ("M", "Feminino"),
        ("F", "Matutino"),
    )
    sexo = models.CharField("Sexo",  max_length=2,choices=tuplesexo , blank=False)
    idadepaciente =  models.CharField(max_length=3, blank=False)

    
    tupleMutacao = (
        ("1", "BRCA1"),
        ("2", "BRCA2"),
        ("3", "TP54"),
        ("4", "CDH1"),
        ("5", "STK11"),
        ("6", "PTEN"),
        ("7", "PALB2"),
        ("8", "VUS")
    )
    mutacaoGenetica =  models.CharField("Teste genético apresenta mutação do tipo:",max_length=1, choices=tupleMutacao)

    tupleOpcao = (
        ("1", "SIM"),
        ("2", "NAO"),
    )

    opc_bilateral = models.CharField("Historico Pessoal de cancer de mama bilateral:",max_length=1, choices=tupleOpcao)
    opc_ovario = models.CharField("Tem historico Pessoal de cançer de ovario?",max_length=1, choices=tupleOpcao)




    temcancer = models.CharField("Tem câncer de mama?",max_length=2, choices=tupleOpcao)

    tupleCancer = (
        ("1", "Carcinoma ductal insitu"),
        ("2", "Carcinoma não epecial"),
        ("3", "Lobural"),
        ("4", "Medular"),
        ("5", "Metaplatico"),
        ("6", "Mucinoso"),
    )

    cancer_mama = models.CharField("Se tem câncer de mama, qual tipo histologico?",max_length=2, choices=tupleCancer)

    cancer_diagnostico =  models.CharField(max_length=2)
    cancer_histologico = models.CharField(max_length=2)


    tipo_molecular = models.CharField(max_length=25)
    tam_cancer = models.CharField(max_length=25)
    qtd_parent_1 = models.CharField(max_length=25)
    qtd_parent_2 = models.CharField(max_length=25)

    parent_seg_grau =  models.CharField(max_length=25)
    parent_pri_grau =  models.CharField(max_length=25)


    asc_judia =  models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.dado_paciente



    



    