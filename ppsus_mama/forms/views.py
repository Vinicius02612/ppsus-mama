from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.validators import validate_email

from django.http import Http404


from .models import ModFormsTo,Form

# Create your views here.

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


    
def report(request, id_forms):

    respostas = get_object_or_404(Form, id = id_forms)

    return render(request, 'forms/report.html',{'resp': respostas})

    


def results(request):
    return render(request, 'forms/results.html')
    

    
        


   
    

