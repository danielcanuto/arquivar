from django.db import models
from servidor.models import Servidor
# Create your models here.
class AssentamentoFuncional(models.Model):
    servidor = models.ForeignKey(Servidor, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Nome Servidor")
    Localizacao = models.CharField(max_length=150)
    obs = models.TextField(blank=True, null=True)
