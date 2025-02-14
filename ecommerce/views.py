# ecommerce/views.py
from django.shortcuts import render, redirect
from .models import Produto, CarrinhoProduto, Carrinho

def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'ecommerce/lista_produtos.html', {'produtos': produtos})

def adicionar_ao_carrinho(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    carrinho, created = Carrinho.objects.get_or_create(user=request.user)
    carrinho_produto, created = CarrinhoProduto.objects.get_or_create(carrinho=carrinho, produto=produto)
    carrinho_produto.quantidade += 1
    carrinho_produto.save()
    return redirect('lista_produtos')

# ecommerce/views.py
from .models import Pedido, PedidoProduto
import uuid

def checkout(request):
    carrinho = Carrinho.objects.get(user=request.user)
    pedido = Pedido.objects.create(user=request.user, pagamento_pix=str(uuid.uuid4()))
    for item in carrinho.carrinhoproduto_set.all():
        PedidoProduto.objects.create(pedido=pedido, produto=item.produto, quantidade=item.quantidade)
    carrinho.delete()
    return render(request, 'ecommerce/checkout.html', {'pedido': pedido})

# ecommerce/views.py
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
