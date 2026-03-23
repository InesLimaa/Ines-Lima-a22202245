from django.contrib import admin

# Register your models here.

from .models import Turma
from .models import Professor
from .models import Aluno

class TurmaAdmin(admin.ModelAdmin):
    list_display = ("nome", "ano_letivo")
    ordering = ("nome", "ano_letivo")
    search_fields = ("nome", "ano_letivo")


class ProfessorAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "telefone", "especialidade", "turma")
    ordering = ("nome",)
    search_fields = ("nome", "email", "especialidade")


class AlunoAdmin(admin.ModelAdmin):
    list_display = ("nome", "numero", "email", "turma")
    ordering = ("nome", "numero")
    search_fields = ("nome", "numero", "email")


# Registar no admin
admin.site.register(Turma, TurmaAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Aluno, AlunoAdmin)