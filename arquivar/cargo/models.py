from django.db import models
# vamos la

# Create your models here.
class Cargo(models.Model):
    CLASSE_CARGO = (
        ("FUNDAMENTAL", "Fundamental - Nível - C"),
        ("MEDIO", "Médio - Nível - D"),
        ("SUPERIOR", "Superior - Nível - E")
    )

    CATEGORIA_FUNCIONAL = (
        ("Téc_Admin", "Tecnico Administrativo"),
        ("Docente", "Docente")
    )

    categoria_funcional = models.CharField("Categoria", max_length=10, choices=CATEGORIA_FUNCIONAL)
    nome = models.CharField("Cargo", max_length= 100)
    classe_cargo = models.CharField("Classe Cargo", max_length=30, choices=CLASSE_CARGO)

    def __str__(self):
        return f"{self.nome} - {self.classe_cargo}"

    class Meta:
        verbose_name_plural = "Cargos"
        ordering = ['classe_cargo', "nome"]