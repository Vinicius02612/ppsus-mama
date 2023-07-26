from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404,HttpResponseRedirect,HttpResponse


from .models import ModFormsTo,Formulario,AdicionarPerguntas

@login_required(redirect_field_name='login')
def forms(request):
    if request.method != 'POST':
        formTo = ModFormsTo()
        return render(request, "forms/forms.html", {'formTo':formTo})
    
    formTo = ModFormsTo(request.POST)
    if not formTo.is_valid():
        messages.error(request, "Erro ao enviar formulario, verifique os campos.")
        formTo =  ModFormsTo(request.POST)
        return render(request, "forms/forms.html", {'formTo':formTo})
    formTo.save()
    messages.success(request, f'Formulario de {request.POST.get("nomePaciente")} salvo com sucesso')
    return render(request, "forms/results.html", {'formTo':formTo})


@login_required(redirect_field_name='login')
def report(request, id_forms):

    respostas = get_object_or_404(Formulario, id = id_forms)
    return render(request, 'forms/report.html',{'resp': respostas})

    
@login_required(redirect_field_name='login')
def results(request):
    return render(request, 'forms/results.html')
        
""" 
def adicionar_novapergunta(request):
    titulo = request.POST.get('titulo')
    opcoes = request.POST.get('opcoes')
 """

def adicionarPergunta(request):
        if request.method != 'POST':
            newPergunta = AdicionarPerguntas()
            return render(request, 'forms/adicionarPergunta.html',{'pergunta': newPergunta})

        newPergunta = AdicionarPerguntas(request.POST)
        if not newPergunta.is_valid():
            messages.error(request, "Erro ao enviar formulario, verifique os campos.")
            newPergunta =  AdicionarPerguntas(request.POST)
        return render(request, "forms/adicionarPergunta.html")
   

        



 

