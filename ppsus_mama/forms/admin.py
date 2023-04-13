from django.contrib import admin

# Register your models here.
from .models import Form,Paciente


                    
class Perguntas(admin.ModelAdmin):
    list_display = [
        'dado_paciente',
        'mutacaoGenetica',
        'opc_bilateral',
        'opc_ovario',
        'cancer_mama',
        'cancer_diagnostico',
        'cancer_histologico',
        'tipo_molecular',
        'tam_cancer',
        'qtd_parent_1',
        'qtd_parent_2',
        'parent_seg_grau',
        'parent_pri_grau',
        'asc_judia'
    ]


admin.site.register(Paciente)

admin.site.register(Form, Perguntas)