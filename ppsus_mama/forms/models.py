from django.db import models
from django.utils import timezone

# Create your models here.

""" Furmulario referente as questões para treinar o modelo """
class Form(models.Model):
    nomePaciente = models.CharField("Nome do paciente:",max_length=255, blank=False)
    sobrenome = models.CharField("Sobrenome:",max_length=255, blank=False)
    nomeclinica =  models.CharField("Nome da clinica:",max_length=255, blank=False)

    tuplesexo = (
        ("M", "Feminino"),
        ("F", "Masculino"),
    )
    sexo = models.CharField("Sexo",  max_length=2,choices=tuplesexo , blank=False)
    idadepaciente =  models.CharField("Idade do paciente:",max_length=3, blank=False)

    
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

    tupleIdadeCancer = (
        ("1","Maior que 60 anos"),
        ("2", "Entre 55 e 60 anos"),
        ("3", "Entre 45 e 55 anos"),
        ("4", "Entre 35 e 45 anos"),
        ("5", "Entre 30 e 35 anos"),
        ("6", "Menor que 30 anos"),
        
    )
    idade_diagnostico =  models.CharField("Faixa de idade do diagnostico de câncer de mama:",max_length=2, choices=tupleIdadeCancer)

    
    tupleTipoMolecular = (
        ("1", "Lumial"),
        ("2", "Lumial HEr2"),
        ("3", "HEr2"),
        ("4", "Triplo Negativo"),
    )


    tipo_molecular = models.CharField(" Tipo molecular de câncer de mama:",max_length=2, choices=tupleTipoMolecular)

    tupleTamanhoDoCancer = (
        ("1", "Insitu"),
        ("2", "T1"),
        ("3", "T2"),
        ("4", "T3"),
        ("5", "T4"),
    )
    tam_cancer = models.CharField("Se tem câncer, qual o tamanho do tumor:",max_length=2,choices=tupleTamanhoDoCancer)
    
    tupleQtdParente = (
        ("1", "Um"),
        ("2", "Dois"),
        ("3", "Três ou Mais"),
        ("4", "Desconhece"),
    )
    qtd_parent_1 = models.CharField("Quantidade parentes de primeiro grau com câncer de mama:",max_length=2, choices=tupleQtdParente)
    
    
    
    
    qtd_parent_2 = models.CharField("Quantidade de parentes de segundo grau ou mais distante com câncer de mama ou ovario < 50 anos:",max_length=2, choices=tupleQtdParente)
    

    parent_seg_grau =  models.CharField(" Parentes de segundo grau ou mais distante com câncer de mama ou ovario < 50 anos:",max_length=2, choices=tupleQtdParente)
    parent_pri_grau =  models.CharField("Parentes de primeiro grau com :",max_length=2,choices=tupleQtdParente)


    asc_judia =  models.CharField("Ascendencia Judia Ashkenazi:",max_length=2, choices=tupleOpcao)

    def __str__(self) -> str:
        return self.nomePaciente



    



    