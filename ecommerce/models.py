# ecommerce/models.py
from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True) #opcional
    def __str__(self):
        return self.nome
class Carrinho(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    produtos = models.ManyToManyField(Produto, through='CarrinhoProduto')

    def __str__(self):
        return f'Carrinho de {self.user.username}'
class CarrinhoProduto(models.Model):
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.quantidade}x {self.produto.nome}'
class Pedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    produtos = models.ManyToManyField(Produto, through='PedidoProduto')
    data_pedido = models.DateTimeField(auto_now_add=True)
    pagamento_pix = models.CharField(max_length=100)  # Código PIX

    def __str__(self):
        return f'Pedido {self.id} de {self.user.username}'
class PedidoProduto(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.quantidade}x {self.produto.nome}'
