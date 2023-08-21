from rest_framework.viewsets import ModelViewSet
from garagem.models import Veiculo, Acessorio, Categoria, Cor, Marca, Modelo
from garagem.serializers import VeiculoSerializer, VeiculoListSerializer, VeiculoDetailSerializer, ModeloSerializer, MarcaSerializer, CategoriaSerializer, CorSerializer, AcessorioSerializer 


class VeiculoViewSet(ModelViewSet):
    queryset = Veiculo.objects.all()
    def get_serializer_class(self):
        if self.action == "list":
            return VeiculoListSerializer
        elif self.action == "retrieve":
            return VeiculoDetailSerializer
        return VeiculoSerializer