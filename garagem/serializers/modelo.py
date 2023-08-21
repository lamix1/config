from rest_framework.serializers import ModelSerializer
from garagem.models import Modelo


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
