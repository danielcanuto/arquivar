from pyexpat import model
from django.db import models
# from servidor.models import Servidor
# Create your models here.

from cpf_field.models import CPFField

# Create your models here.


class Pessoa(models.Model):
    nome = models.CharField("Nome", max_length=100)
    aniversario = models.DateField("Aniversário")
    cpf = CPFField('cpf', null=True, blank=True)
    rg = models.CharField('RG', max_length=14, blank=True, null=True)

    def __str__(self):
        return f'{self.nome} - cpf: {self.cpf}'

    class Meta:
        verbose_name_plural = "Pessoas"
        ordering = ["nome"]


# class Servidor(models.Model):
#     CATEGORIA_FUNCIONAL = (
#         ("Téc_Admin", "Tecnico Administrativo"),
#         ("Docente", "Docente")
#     )

#     nome = models.ForeignKey(
#         Pessoa, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Nome")
#     matricula = models.CharField("Matricula SIAPE", max_length=10)
#     categoria_funcional = models.CharField(
#         "Categoria", max_length=10, choices=CATEGORIA_FUNCIONAL)

#     def __str__(self):
#         return f"{self.nome} - siape: {self.matricula}"

#     class Meta:
#         verbose_name_plural = "Servidores"
#         ordering = ["nome"]


class Situacao(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.nome}'

    class Meta:
        verbose_name_plural = "Situações"
        ordering = ["nome"]


class ArmarioAcervo(models.Model):
    codigo = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.codigo}'

    class Meta:
        verbose_name_plural = "Armários"
        ordering = ["codigo"]


class FaceArmario(models.Model):
    armario = models.ForeignKey(
        ArmarioAcervo,
        on_delete=models.CASCADE,
        blank=True, null=True, verbose_name="Armário")
    codigo = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.armario}/{self.codigo}'

    class Meta:
        verbose_name_plural = "Faces Armários"
        ordering = ["codigo"]


class PrateleiraFace(models.Model):
    face = models.ForeignKey(
        FaceArmario,
        on_delete=models.CASCADE,
        blank=True, null=True, verbose_name="Face Armário")
    codigo = models.CharField(max_length=10)
    
    def __str__(self):
        return f'{self.face}/{self.codigo}'

    class Meta:
        verbose_name_plural = "Prateleiras faces"
        ordering = ["codigo"]



class AssentamentoFuncional(models.Model):

    CATEGORIA_FUNCIONAL = (
        ("Téc_Admin", "Tecnico Administrativo"),
        ("Docente", "Docente")
    )

    nome = models.ForeignKey(
        Pessoa, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Nome Servidor")
    
    matricula = models.CharField("Matricula SIAPE", max_length=10)
    
    categoria_funcional = models.CharField(
        "Categoria", max_length=10, choices=CATEGORIA_FUNCIONAL)

    
    situacao = models.ForeignKey(Situacao, on_delete=models.CASCADE,
                                 blank=True, null=True, verbose_name="Situação Servidor")
    localizacao = models.ForeignKey(
        PrateleiraFace, on_delete=models.CASCADE,
        blank=True, null=True, verbose_name="Local Assentamento"

    )
    status_afd = models.BooleanField(
        verbose_name="Incluido no AFD", default=False)
    obs = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.nome} siape: {self.matricula}'

    class Meta:
        verbose_name_plural = "Assentamentos Funcionais"
        ordering = ["nome"]
