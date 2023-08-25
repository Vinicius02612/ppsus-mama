from django.contrib import admin
# Register your models here.

from .models import Pergunta, Formulario


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
        'historicoFMasculino',
        'qtd_parent_2',
        'parent_seg_grau',
        'parent_pri_grau',
        'asc_judia',
    ]


admin.site.register(Formulario,Form)


""" 


 """