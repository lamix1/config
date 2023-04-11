from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from garagem.models import Marca
from config.serializers import MarcaSerializer

class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
