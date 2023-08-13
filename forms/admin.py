from django.contrib import admin
# Register your models here.

from .models import Pergunta

class FormPergunta(admin.ModelAdmin):
    list_display = [
            'titulo',
            'peso',
            'mostrar',
        ]
    list_editable = ['mostrar']


class FormResposta(admin.ModelAdmin):
    list_display=[
        'pergunta',
        'resposta',
        'mostrar',
    ]
    list_editable = ['mostrar']

class Form(admin.ModelAdmin):

    list_display = [
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
        'tam_cancer',
        'qtd_parent_1',
        'qtd_parent_2',
        'parent_seg_grau',
        'parent_pri_grau',
        'asc_judia',
    ]

admin.site.register(Pergunta,FormPergunta)


""" 


 """