from django.shortcuts import render

# Create your views here.

def cadastro(request):
    
    return render( request,'account/cadastro.html')


def login(request):
    return render(request,'account/login.html')

def dashboard(request):
    return render(request,'account/dashboard.html')
