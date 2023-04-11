from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.validators import validate_email

# Create your views here.

def formulario(request):
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
    asc_judia = request.POST.get('asc_judia')

    if not nomePaciente or not sobreNome or not idadePaciente or not nomeClinica or not mutacaoGenetica or not opc_bilateral \
    or not opc_ovario or not cancer_mama or not cancer_diagnostico or not cancer_histoogico or not tipo_molecular or not  tam_cancer \
    or not qtd_parent_1 or not qtd_parent_2 or not parent_seg_grau or not asc_judia:
        messages.error(request, 'Os campos devem ser todos preenchidos!')
        return render(request, 'forms/forms.html')
    else:
        messages.success(request, 'Dados enviados...')
        return redirect('resus')

        






    


def results(request):
    return render(request, 'forms/results.html')