from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.validators import validate_email


import json

from .models import Form

# Create your views here.

def forms(request):
    if request.method != 'POST':
        return render(request, 'forms/forms.html')

    nomePaciente =  request.POST.get('nomePaciente')
    sobreNome = request.POST.get('sobrenome')
    nomeClinica = request.POST.get('nomeClinicia')
    idadePaciente =  request.POST.get('idadePaciente')

    mutacaoGenetica = request.POST.get('mutacao')
    opc_bilateral = request.POST.get('opcao_bilateral')
    opc_ovario = request.POST.get('opcao_ovario')

    cancer_mama=  request.POST.get('cancer_mama')
    cancer_diagnostico = request.POST.get('cancer_diagnostico')
    cancer_histoogico =  request.POST.get('cancer_histologico')

    tipo_molecular = request.POST.get('tipo_molecular')
    tam_cancer = request.POST.get('tam_cancer')
    qtd_parent_1 =  request.POST.get('qtd_parent_1')
    qtd_parent_2 =  request.POST.get('qtd_parent_2')

    parent_seg_grau = request.POST.get('parent_2grau')
    parent_pri_grau = request.POST.get('parent_1grau')

    asc_judia = request.POST.get('asc_judia')
    
 
    
    resForms = Form.objects.create(

            nomePaciente = nomePaciente,
            sobrenome= sobreNome,
            nomeclinica= nomeClinica,
            idadepaciente=idadePaciente,
            mutacaoGenetica = mutacaoGenetica,
            opc_bilateral =opc_bilateral,
            opc_ovario = opc_ovario,
            cancer_mama = cancer_mama,
            cancer_diagnostico = cancer_diagnostico,
            cancer_histologico = cancer_histoogico,
            tipo_molecular =tipo_molecular,
            tam_cancer = tam_cancer,
            qtd_parent_1 = qtd_parent_1,
            qtd_parent_2 = qtd_parent_2,
            parent_seg_grau = parent_seg_grau,
            parent_pri_grau = parent_pri_grau,
            asc_judia = asc_judia

        )
    #salvando dados em um arquivo json

    messages.success(request, 'Dados enviados...')       
    return render(request, 'forms/report.html',{
        'resPaciente':resP,
        'resForms':resForms
    })    
    

    
        

    
def report(request, id_report):

    responsePaciente = Paciente.objects.get(Paciente, id = id_report)
    responseForms = Form.objects.get(Form, id =  id_report)


    return render(request, 'forms/report.html', {
        'reportPaciente':responsePaciente,
        'reportForm':responseForms
    })


def results(request):
    return render(request, 'forms/results.html')