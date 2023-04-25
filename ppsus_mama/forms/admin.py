from django.contrib import admin

# Register your models here.
from .models import Form

           
class Perguntas(admin.ModelAdmin):
    list_display = [
        'id',
        'nomePaciente',
        'sobrenome',
        'nomeclinica',
        'sexo',
        'idadepaciente',
        'mutacaoGenetica',
        'opc_bilateral',
        'opc_ovario',
        'temcancer',
        'cancer_mama',
        'idade_diagnostico',
        'tipo_molecular',
        'tam_cancer',
        'qtd_parent_1',
        'qtd_parent_2',
        'parent_seg_grau',
        'parent_pri_grau',
        'asc_judia'
    ]

    fields = [
       'nomePaciente',
        'sobrenome',
        'nomeclinica',
        'sexo',
        'idadepaciente',
        'mutacaoGenetica',
        'opc_bilateral',
        'opc_ovario',
        'temcancer',
        'cancer_mama',
        'idade_diagnostico',
        'tipo_molecular',
        'tam_cancer',
        'qtd_parent_1',
        'qtd_parent_2',
        'parent_seg_grau',
        'parent_pri_grau',
        'asc_judia'
    ]



admin.site.register(Form, Perguntas)