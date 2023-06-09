from rest_framework.serializers import ModelSerializer

from garagem.models import Marca, Categoria, Cor, Acessorio, Modelo, Veiculo

class MarcaSerializer(ModelSerializer):
    class Meta:
        model = Marca
        fields = "__all__"

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"

class CorSerializer(ModelSerializer):
    class Meta:
        model = Cor
        fields = "__all__"

class AcessorioSerializer(ModelSerializer):
    class Meta:
        model = Acessorio
        fields = "__all__"

class ModeloSerializer(ModelSerializer):
    class Meta:
        model = Modelo
        fields = "__all__"

class ModeloListSerializer(ModelSerializer):
    class Meta:
        model = Modelo
        fields = ["id", "nome"]

class ModeloDetailSerializer(ModelSerializer):
    class Meta:
        model = Modelo
        fields = "__all__"
        depth = 1

class VeiculoSerializer(ModelSerializer):
    class Meta:
        model = Veiculo
        fields = "__all__"

class VeiculoDetailSerializer(ModelSerializer):
    class Meta:
        model = Veiculo
        fields = "__all__"
        depth = 2

class VeiculoListSerializer(ModelSerializer):
    class Meta:
        model = Veiculo
        fields = ["id", "modelo", "ano"]