from django.shortcuts import render

# Create your views here.

def forms(request):
    return render(request, 'forms/forms.html')