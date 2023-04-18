from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.validators import validate_email




from .models import ModFormsTo

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
    return redirect('results')

    
def report(request):
    ...

def results(request):
    return render(request, 'forms/results.html')
    
        


   
    

