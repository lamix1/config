from django.db import models

from uploader.models import Image

from garagem.models import Marca, Modelo, Categoria, Cor, Acessorio

class Veiculo(models.Model):
    id = models.BigAutoField(primary_key=True)
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, related_name="veiculos")
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="veiculos")
    ano = models.IntegerField(default=0,  null=True)
    descricao = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True, blank=True)
    acessorios = models.ManyToManyField(Acessorio, related_name="veiculos")
    capa = models.ManyToManyField(Image, related_name="+", null=True, blank=True, default=None,)
    
    def __str__(self):
        return f"{self.modelo}- {self.ano}"
    
    class Meta:
        verbose_name = "Veículo"
        verbose_name_plural = "Veículos"
