from django.db import models

class Marca(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nome.upper()}"