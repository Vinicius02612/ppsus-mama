from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .calcular_predicao import calcular_predicao


from .models import ModPergunta, ModFormsTo,Formulario
from .forms import Questionario
def create_question(request):
    if request.method != 'POST':
        newpergunta = ModPergunta()
        return render(request, "forms/create_question.html",{'newpergunta':newpergunta})

    newpergunta = ModPergunta(request.POST)
    if not newpergunta.is_valid():
        messages.error(request, "Erro ao enviar pergunta, verifique os campos.")
        newpergunta = ModPergunta(request.POST)
        return render(request, "forms/create_question.html",{'newpergunta':newpergunta})
    newpergunta.save()
    messages.success(request, f'Pergunta salvo com sucesso')
    return render(request, "forms/create_question.html", {'newpergunta':newpergunta})




def forms(request):
    if request.method != 'POST':
        formTo = Questionario()
        return render(request, "forms/forms.html", {'formTo':formTo})
    
    formTo = Questionario(request.POST)
    if not formTo.is_valid():
        messages.error(request, "Erro ao enviar Questions, verifique os campos.")
        formTo =  Questionario(request.POST)
        return render(request, "forms/forms.html", {'formTo':formTo})
    
    resposta = Formulario(
        nomePaciente = formTo.cleaned_data['nomePaciente'],
        sobrenome = formTo.cleaned_data['sobrenome'],
        nomeclinica = formTo.cleaned_data['nomeclinica'],
        sexo = formTo.cleaned_data['sexo'],
        idadepaciente = formTo.cleaned_data['idadepaciente'],
        temcancer = formTo.cleaned_data['temcancer'],
        cancer_mama = formTo.cleaned_data['cancer_mama'],
        idade_diagnostico  = formTo.cleaned_data['idade_diagnostico'],
        mutacaoGenetica = formTo.cleaned_data['mutacaoGenetica'],
        opc_bilateral = formTo.cleaned_data['opc_bilateral'],
        opc_ovario = formTo.cleaned_data['opc_ovario'],
        tipo_molecular = formTo.cleaned_data['tipo_molecular'],
        tam_cancer = formTo.cleaned_data['tam_cancer'],
        historicoFMasculino = formTo.cleaned_data['historicoFMasculino'],
        qtd_parent_2 = formTo.cleaned_data['qtd_parent_2'],
        parent_seg_grau = formTo.cleaned_data['parent_seg_grau'],
        parent_pri_grau = formTo.cleaned_data['parent_pri_grau'],
        asc_judia = formTo.cleaned_data['asc_judia'],
    )
    nome = resposta.nomePaciente
    sobrenome = resposta.sobrenome 
    clinica = resposta.nomeclinica
    sexo = resposta.sexo
    idade = resposta.idadepaciente
    temcancer = resposta.temcancer
    cancer_mama = resposta.cancer_mama
    idade_diagnostico = resposta.idade_diagnostico
    mutacaoGenetica = resposta.mutacaoGenetica
    opc_bilateral = resposta.opc_bilateral
    opc_ovario = resposta.opc_ovario
    tipo_molecular = resposta.tipo_molecular
    tam_cancer = resposta.tam_cancer
    historicoFMasculino = resposta.historicoFMasculino
    qtd_parent_2 = resposta.qtd_parent_2
    parent_seg_grau = resposta.parent_seg_grau
    parent_pri_grau = resposta.parent_pri_grau
    asc_judia = resposta.asc_judia

    pontuacao = calcular_predicao(sexo,idade,temcancer,cancer_mama, idade_diagnostico,mutacaoGenetica,opc_bilateral,opc_ovario,tipo_molecular,tam_cancer,historicoFMasculino,qtd_parent_2,parent_seg_grau,parent_pri_grau,asc_judia)
    if not nome or not sobrenome or not clinica or  not idade:
        nome = "S/N"
        sobrenome = "S/N"
        clinica = "S/N"
        idade = "S/N"
        resposta.nomePaciente = nome
        resposta.sobrenome = sobrenome
        resposta.nomeclinica = clinica
        resposta.idadepaciente = idade
        resposta.save()
        messages.success(request, f'Formulario de {request.POST.get("nomePaciente")} salvo com sucesso')
        return render(request, "forms/results.html", {'formTo':formTo, 'pontos':pontuacao})
    else:
        messages.success(request, f'Formulario de {request.POST.get("nomePaciente")} salvo com sucesso')
        resposta.save()
        return render(request, "forms/results.html", {'formTo':formTo, 'pontos':pontuacao})



def results(request):
    return render(request, 'forms/results.html')

@login_required(redirect_field_name='login')
def viewdata(request):
    formTo = Formulario.objects.all()
    return render(request, 'forms/visualizardados.html',{'formTo':formTo})

