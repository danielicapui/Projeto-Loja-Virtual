# ecommerce/urls.py
from django.urls import path
from .views import lista_produtos, adicionar_ao_carrinho, checkout,signup,perfil,cadastrar_produto
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', lista_produtos, name='lista_produtos'),
    path('adicionar_ao_carrinho/<int:produto_id>/', adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('checkout/', checkout, name='checkout'),
    path('signup/', signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', perfil, name='profile'),
    path('cadastrar_produto/', cadastrar_produto, name='cadastrar_produto'),
]

