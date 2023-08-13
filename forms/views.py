from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required



from .models import ModFormsTo,Formulario

""" def create_question(request):
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
    return render(request, "forms/create_question.html", {'newpergunta':newpergunta}) """



@login_required(redirect_field_name='login')
def forms(request):
    if request.method != 'POST':
        formTo = ModFormsTo()
        return render(request, "forms/forms.html", {'formTo':formTo})
    
    formTo = ModFormsTo(request.POST)
    if not formTo.is_valid():
        messages.error(request, "Erro ao enviar Questions, verifique os campos.")
        formTo =  ModFormsTo(request.POST)
        return render(request, "forms/forms.html", {'formTo':formTo})
    formTo.save()
    messages.success(request, f'Formulario de {request.POST.get("nomePaciente")} salvo com sucesso')
    return render(request, "forms/results.html", {'formTo':formTo})


@login_required(redirect_field_name='login')
def results(request):
    return render(request, 'forms/results.html')

@login_required(redirect_field_name='login')
def viewdata(request):
    form = Formulario.objects.all()

    return render(request, 'forms/visualizardados.html',{'formTo':form})

