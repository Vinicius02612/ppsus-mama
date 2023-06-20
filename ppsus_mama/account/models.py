from django.db import models
from forms.models import Formulario,AdicionarPerguntas
from django import forms
# Create your models here.


class ModForms(forms.ModelForm):
    class Meta:
        model = Formulario
        exclude = ()

