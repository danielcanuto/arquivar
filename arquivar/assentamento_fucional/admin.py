from django.contrib import admin

from assentamento_fucional.models import AssentamentoFuncional, Pessoa, Situacao, ArmarioAcervo,FaceArmario, PrateleiraFace
# Register your models here.


@admin.register(AssentamentoFuncional, Pessoa,  Situacao, ArmarioAcervo, FaceArmario, PrateleiraFace)
class AssentamentoAdmin(admin.ModelAdmin):
    pass
