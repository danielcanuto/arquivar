from django.contrib import admin

from assentamento_fucional.models import AssentamentoFuncional
# Register your models here.


@admin.register(AssentamentoFuncional)
class CargoAdmin(admin.ModelAdmin):
    pass
