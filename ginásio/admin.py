from django.contrib import admin
from .models import PersonalTrainer, Membro, SessaoTreino


class PersonalTrainerAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "telefone", "especialidade")
    ordering = ("nome",)
    search_fields = ("nome", "email", "especialidade")


class MembroAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "telefone", "data_nascimento")
    ordering = ("nome",)
    search_fields = ("nome", "email")


class SessaoTreinoAdmin(admin.ModelAdmin):
    list_display = ("membro", "pt", "data", "hora")
    ordering = ("data", "hora")
    search_fields = ("membro__nome", "pt__nome")
    list_filter = ("data", "pt")


# Registos
admin.site.register(PersonalTrainer, PersonalTrainerAdmin)
admin.site.register(Membro, MembroAdmin)
admin.site.register(SessaoTreino, SessaoTreinoAdmin)