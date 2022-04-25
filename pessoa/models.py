from django.db import models

# Create your models here.
from django.db import models

from cpf_field.models import CPFField

# Create your models here.
class Person(models.Model):
    SEXO_CHOICES = [
        ["F", "Feminino"],
        ["M", "Masculino"],
        ["N", "Nenhuma das opções"]
    ]

    name = models.CharField("Nome", max_length=100)
    birthday = models.DateField("Aniversário")
    bio = models.TextField('Sobre', null=True, blank=True)
    photo = models.ImageField(
        'Foto', upload_to='clients_photos', null=True, blank=True)
    cpf = CPFField('cpf', null=True, blank=True)
    rg = models.CharField('RG', max_length=14, blank=True, null=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)

    def __str__(self):
        return f'{self.name} - cpf: {self.cpf}'

# class AgenteTrabalhador(models.Model):
#     nome = models.ForeignKey(Person, on_delete=models.CASCADE, blank=True, null=True)
#     digitalizador = models.BooleanField(default=False)


#     def __str__(self):
#             return f'{self.nome}'

