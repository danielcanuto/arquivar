from django.db import models
from pessoa.models import Person
from cargo.models import Cargo
# Create your models here.

class Servidor(models.Model):
    nome = models.ForeignKey(Person, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Nome")
    matricula = models.CharField("Matricula SIAPE", max_length=10)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Cargo")
    inicio_vinculo = models.DateField("Inicio Vinculo")

    def __str__(self):
        return f"{self.nome} -  {self.matricula}"

    class Meta:
        verbose_name_plural = "Servidores"
        ordering = ["nome"]