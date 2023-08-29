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

class Formulario(models.Model):
    nomePaciente = models.CharField(max_length=255, blank=True)
    sobrenome = models.CharField(max_length=255, blank=True)
    nomeclinica =  models.CharField(max_length=255, blank=True)
    sexo = models.CharField( max_length=2, blank=False)
    idadepaciente =  models.CharField(max_length=3, blank=False)
    temcancer = models.CharField(max_length=100)
    cancer_mama = models.CharField(max_length=100 )
    idade_diagnostico =  models.CharField(max_length=100)
    mutacaoGenetica =  models.CharField(max_length=100)
    opc_bilateral = models.CharField(max_length=100)
    opc_ovario = models.CharField(max_length=100)
    tipo_molecular = models.CharField(max_length=100)
    historicoFMasculino =  models.CharField(max_length=100)
    qtd_parent_2 = models.CharField(max_length=100)
    parent_seg_grau =  models.CharField(max_length=100)
    parent_pri_grau =  models.CharField(max_length=255)
    asc_judia =  models.CharField(max_length=12)

    def __str__(self) -> str:
        return self.nomePaciente



class ModFormsTo(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = (
        'id',
        'nomePaciente',
        'sobrenome',
        'nomeclinica',
        'sexo',
        'idadepaciente',
        'temcancer',
        'cancer_mama',
        'idade_diagnostico',
        'mutacaoGenetica',
        'opc_bilateral',
        'opc_ovario',
        'tipo_molecular',
        'historicoFMasculino',
        'qtd_parent_2',
        'parent_seg_grau',
        'asc_judia',
        )
