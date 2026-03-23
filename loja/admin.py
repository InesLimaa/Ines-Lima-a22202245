from django.contrib import admin
from .models import Categoria, Produto, Morada, Cliente, Pedido, ItemPedido


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    ordering = ("nome",)
    search_fields = ("nome",)


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome", "preco", "categoria")
    ordering = ("nome",)
    search_fields = ("nome",)
    list_filter = ("categoria",)


class MoradaAdmin(admin.ModelAdmin):
    list_display = ("rua", "cidade")
    ordering = ("cidade", "rua")
    search_fields = ("rua", "cidade")


class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "morada")
    ordering = ("nome",)
    search_fields = ("nome", "email")


class PedidoAdmin(admin.ModelAdmin):
    list_display = ("id", "cliente", "data")
    ordering = ("data",)
    search_fields = ("cliente__nome",)
    list_filter = ("data",)


class ItemPedidoAdmin(admin.ModelAdmin):
    list_display = ("pedido", "produto", "quantidade")
    ordering = ("pedido",)
    search_fields = ("produto__nome", "pedido__cliente__nome")


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Morada, MoradaAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(ItemPedido, ItemPedidoAdmin)