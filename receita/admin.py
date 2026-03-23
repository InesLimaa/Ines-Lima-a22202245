from django.contrib import admin
from .models import Ingrediente, Receita, Utilizador


class IngredienteAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    ordering = ("nome",)
    search_fields = ("nome",)


class ReceitaAdmin(admin.ModelAdmin):
    list_display = ("nome", "tempo_preparo")
    ordering = ("nome",)
    search_fields = ("nome", "descricao")
    filter_horizontal = ("ingredientes",)


class UtilizadorAdmin(admin.ModelAdmin):
    list_display = ("nome", "email")
    ordering = ("nome",)
    search_fields = ("nome", "email")
    filter_horizontal = ("receitas_favoritas",)


# Registar modelos
admin.site.register(Ingrediente, IngredienteAdmin)
admin.site.register(Receita, ReceitaAdmin)
admin.site.register(Utilizador, UtilizadorAdmin)