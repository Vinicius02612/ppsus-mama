from rest_framework import serializers
from forms import models

class FormsSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Pergunta
        fields = ['titulo','peso', 'tipo']