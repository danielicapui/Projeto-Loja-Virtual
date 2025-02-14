# loja_virtual/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls), #URLs do administrador
    path('ecommerce/', include('ecommerce.urls')), #URLs do aplicativo
    path('accounts/', include('django.contrib.auth.urls')),  # URLs para autenticação
]
