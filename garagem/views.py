from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from garagem.models import Marca
from config.serializers import MarcaSerializer

from garagem.models import Categoria
from config.serializers import CategoriaSerializer

class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
