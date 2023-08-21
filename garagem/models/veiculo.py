from django.db import models

from uploader.models import Image

from garagem.models import Marca, Modelo, Categoria, Cor, Acessorio

class Veiculo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="veiculos")
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, related_name="veiculos")        
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="veiculos")
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="veiculos")
    ano = models.IntegerField(default=0,  null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True, blank=True)
    acessorios = models.ManyToManyField(Acessorio, related_name="veiculos")
    capa = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )
    
    def __str__(self):
        return f"marca:{self.marca}, categoria:{self.categoria}, ano:{self.ano} cor:{self.cor}"
    
    class Meta:
        verbose_name_plural = "Veículos"
