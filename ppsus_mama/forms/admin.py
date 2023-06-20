from django.contrib import admin
from django.http import Http404,HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

# Register your models here.
from .models import Formulario,ModFormsTo,AdicionarPerguntas

           
class Perguntas(admin.ModelAdmin):
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
        'idade_diagnostico',
        'opc_ovario',
        'tipo_molecular',
        'tam_cancer',
        'qtd_parent_1',
        'qtd_parent_2',
        'parent_seg_grau',
        'parent_pri_grau',
        'asc_judia'
    ]

    fields = [
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

    search_fields = ('pergunta',)





admin.site.register(Formulario, Perguntas)
