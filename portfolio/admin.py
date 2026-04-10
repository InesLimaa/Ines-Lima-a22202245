from django.contrib import admin
from .models import (
    Licenciatura,
    Perfil,
    UnidadeCurricular,
    Tecnologia,
    Competencia,
    Formacao,
    TFC,
    Projeto,
    MakingOf,
)


class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ("nome", "sigla", "instituicao", "duracao_anos", "ano_inicio")
    ordering = ("nome",)
    search_fields = ("nome", "sigla", "instituicao")


class PerfilAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "licenciatura")
    ordering = ("nome",)
    search_fields = ("nome", "email")


class UnidadeCurricularAdmin(admin.ModelAdmin):
    list_display = ("nome", "ano_curricular", "semestre", "ects", "licenciatura")
    ordering = ("nome",)
    search_fields = ("nome", "descricao")
    list_filter = ("ano_curricular", "semestre", "licenciatura")


class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ("nome", "tipo", "interesse")
    ordering = ("nome",)
    search_fields = ("nome", "tipo")
    list_filter = ("tipo",)


class CompetenciaAdmin(admin.ModelAdmin):
    list_display = ("nome", "nivel", "perfil")
    ordering = ("nome",)
    search_fields = ("nome", "descricao", "nivel")
    list_filter = ("nivel",)


class FormacaoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "entidade", "tipo", "data_inicio", "data_fim", "concluida")
    ordering = ("-data_inicio",)
    search_fields = ("titulo", "entidade", "tipo")
    list_filter = ("tipo", "concluida")


class TFCAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "ano", "interesse")
    ordering = ("-ano", "titulo")
    search_fields = ("titulo", "autor", "resumo")
    list_filter = ("ano",)


class ProjetoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "perfil", "unidade_curricular",)
    ordering = ("titulo",)
    search_fields = ("titulo", "descricao")
    list_filter = ("unidade_curricular",)


class MakingOfAdmin(admin.ModelAdmin):
    ordering = ("titulo",)
    search_fields = ("titulo", "descricao", "modificacoes")


admin.site.register(Licenciatura, LicenciaturaAdmin)
admin.site.register(Perfil, PerfilAdmin)
admin.site.register(UnidadeCurricular, UnidadeCurricularAdmin)
admin.site.register(Tecnologia, TecnologiaAdmin)
admin.site.register(Competencia, CompetenciaAdmin)
admin.site.register(Formacao, FormacaoAdmin)
admin.site.register(TFC, TFCAdmin)
admin.site.register(Projeto, ProjetoAdmin)
admin.site.register(MakingOf, MakingOfAdmin)