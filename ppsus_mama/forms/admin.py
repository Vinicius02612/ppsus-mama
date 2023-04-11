from django.contrib import admin

# Register your models here.
from .models import Pergunta, Cliente


class PerguntasAdmin(admin.ModelAdmin):



    list_display = ('id', 'titulo', 'peso','cliente')


admin.site.register(Cliente)
admin.site.register(Pergunta, PerguntasAdmin)