from rest_framework import viewsets
from forms.api import serializers
from forms import models

class FormViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.FormsSerializers
    queryset = models.Pergunta.objects.all()