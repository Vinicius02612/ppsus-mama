from django.db import models
from django import forms



class Pergunta(models.Model):
    titulo = models.CharField(max_length=100, primary_key=True)
    peso = models.IntegerField()
    tipo = models.CharField(max_length=100)
    mostrar = models.BooleanField(default=True)
    def __str__(self) -> str:
        return self.titulo
    
class ModPergunta(forms.ModelForm):
    class Meta:
        model = Pergunta
        fields = ("titulo","peso","tipo")
""" 
class Pergunta(models.Model):
    titulo = models.CharField(max_length=100, primary_key=True)
    peso = models.IntegerField()
    mostrar = models.BooleanField(default=True)


    def __str__(self) -> str:
        return self.titulo
    
class ModPergunta(forms.ModelForm):
    class Meta:
        model = Pergunta
        fields = ("titulo","peso")


class Resposta(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    resposta = models.CharField(max_length=100)
    mostrar = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.resposta

class ModResposta(forms.ModelForm):
    
    class Meta:
        model = Resposta
        fields = ("pergunta","resposta")



class Formulario(models.Model):

    
    nomePaciente = models.CharField("Nome do paciente:",max_length=255, blank=True)
    sobrenome = models.CharField("Sobrenome:",max_length=255, blank=True)
    nomeclinica =  models.CharField("Nome da clinica:",max_length=255, blank=True)

    tuplesexo = (
        ("F", "Feminino"),
        ("M", "Masculino"),
    )
    sexo = models.CharField("Sexo",  max_length=2,choices=tuplesexo , blank=False)
    idadepaciente =  models.CharField("Idade do paciente:",max_length=3, blank=False)

    tupleOpcao = (
        ("SIM", "SIM"),
        ("NAO", "NAO"),
    )
    temcancer = models.CharField("Tem câncer de mama?",max_length=3, choices=tupleOpcao)

    tupleCancer = (
        ("Carcinoma ductal insitu", "Carcinoma ductal insitu"),
        ("Carcinoma não epecial", "Carcinoma não epecial"),
        ("Lobural", "Lobural"),
        ("Medular", "Medular"),
        ("Metaplatico", "Metaplatico"),
        ("Mucinoso", "Mucinoso"),
        ("Não tem cancer de mama", "Não tem cancer de mama"),
    )

    cancer_mama = models.CharField("Se tem câncer de mama, qual tipo histologico?",max_length=25, choices=tupleCancer)

    tupleIdadeCancer = (
        ("Maior que 60 anos","Maior que 60 anos"),
        ("Entre 55 e 60 anos", "Entre 55 e 60 anos"),
        ("Entre 45 e 55 anos", "Entre 45 e 55 anos"),
        ("Entre 35 e 45 anos", "Entre 35 e 45 anos"),
        ("Entre 30 e 35 anos", "Entre 30 e 35 anos"),
        ("Menor que 30 anos", "Menor que 30 anos"),
        ("Menor que 30 anos", "Menor que 30 anos"),
        ("Sem diagnostico", "Sem diagnostico"),  
    )
    idade_diagnostico =  models.CharField("Faixa de idade do diagnostico de câncer de mama:",max_length=25, choices=tupleIdadeCancer)

    tupleMutacao = (
        ("BRCA1", "BRCA1"),
        ("BRCA2", "BRCA2"),
        ("TP53", "TP53"),
        ("CDH1", "CDH1"),
        ("STK11", "STK11"), 
        ("PTEN", "PTEN"),
        ("PALB2","PALB2"),
        ("VUS", "VUS"),
        ("NÃO APRESENTA MUTAÇÃO", "NÃO APRESENTA MUTAÇÃO"),
    )
    mutacaoGenetica =  models.CharField("Teste genético apresenta mutação do tipo:",max_length=22, choices=tupleMutacao)
    opc_bilateral = models.CharField("Historico Pessoal de cancer de mama bilateral:",max_length=3, choices=tupleOpcao)
    opc_ovario = models.CharField("Tem historico Pessoal de cançer de ovario?",max_length=3, choices=tupleOpcao)

    tupleTipoMolecular = (
        ("Luminal", "Luminal"),
        ("Luminal HEr2", "Luminal HEr2"),
        ("HEr2", "HEr2"),
        ("Triplo Negativo", "Triplo Negativo"),
        ("Não tem cancer de mama", "Não tem cancer de mama"),
    )

    tipo_molecular = models.CharField("Tipo molecular de câncer de mama:",max_length=23, choices=tupleTipoMolecular)

    tupleTamanhoDoCancer = (
        ("Insitu", "Insitu"),
        ("T1", "T1"),
        ("T2", "T2"),
        ("T3", "T3"),
        ("T4", "T4"),
        ("Não tem cancer de mama", "Não tem cancer de mama"),
    )
    tam_cancer = models.CharField("Se tem câncer, qual o tamanho do tumor:",max_length=23,choices=tupleTamanhoDoCancer)
    
    tupleQtdParente = (
        ("Um", "Um"),
        ("Dois", "Dois"),
        ("Três ou Mais", "Três ou Mais"),
        ("Desconhece", "Desconhece"),
    )
    qtd_parent_1 = models.CharField("Quantidade parentes de primeiro grau com câncer de mama:",max_length=12, choices=tupleQtdParente)
    qtd_parent_2 = models.CharField(" Quantidade de parentes de primeiro grau ou mais distante com câncer de mama ou ovario com idade  < 50 anos",max_length=12, choices=tupleQtdParente)
    parent_seg_grau =  models.CharField("Quantidade parentes de segundo grau ou mais distante com câncer de mama ou ovario < 50 anos:",max_length=12, choices=tupleQtdParente)


    tupleParentePrimeiroGrau= (
        ("Cancer de ovario", "Cancer de ovario"),
        ("Cancer de mama masculino", "Cancer de mama masculino"),
        ("Cancer de prostata", "Cancer de prostata"),
        ("Cancer bilateral de mama", "Cancer bilateral de mama"),
        ("Cancer de pancreas", "Cancer de pancreas"),
        ("Dois ou mais itens", "Dois ou mais itens"),
        ("Nenhum", "Nenhum"),
        ("Desconhce","Desconhece")
    )
    parent_pri_grau =  models.CharField("Parentes de primeiro grau com :",max_length=25,choices=tupleParentePrimeiroGrau)
    asc_judia =  models.CharField("Ascendencia Judia Ashkenazi:",max_length=12, choices=tupleOpcao)
    nova_pergunta = models.CharField(max_length=100,blank=True)

    def __str__(self) -> str:
        return self.nomePaciente



class ModFormsTo(forms.ModelForm):
    class Meta:
        model = Formulario
        exclude =('nova_pergunta',)
        
 """