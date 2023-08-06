from django.contrib import admin
# Register your models here.
from .models import Formulario


           
class Perguntas(admin.ModelAdmin):
    list_display = [
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


admin.site.register(Formulario, Perguntas)
