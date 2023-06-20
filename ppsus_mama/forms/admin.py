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


    def adicionar_pergunta(self, request, queryset):
        if request.method == 'POST':
            form = AdicionarPerguntas(request.POST)
            
            if form.is_valid():
                pergunta = form.cleaned_data['pergunta']

                novo_formulario =  Formulario.objects.create(pergunta = pergunta)
                novo_formulario.save()
                self.message_user(request, 'Pergunta adicionada com sucesso!')
                return HttpResponseRedirect(request.get_full_path())
            else:
                form = AdicionarPerguntas()
            
            context = {
                'form':form,
                'title':'Adicionar Pergunta'
            }

            return render(request, 'dashboard.html', context)





admin.site.register(Formulario, Perguntas)
