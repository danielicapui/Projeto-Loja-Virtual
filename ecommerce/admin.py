from django.contrib import admin
from .models import Carrinho,CarrinhoProduto,Categoria,Produto, PedidoProduto,Pedido
# Register your models here.
admin.register(Carrinho)
admin.register(CarrinhoProduto)
admin.register(Categoria)
admin.register(Produto)
admin.register(PedidoProduto)
admin.register(Pedido)