from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.dashboard, name='login'),
    path('admin/', admin.site.urls),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('empresas/', views.empresas, name='empresas'),
    path('empresas/<int:page_index>', views.empresas_pagination, name='empresas'),
    path('clientes/', views.clientes, name='clientes'),
    path('clientes/<int:page_index>', views.clientes_pagination, name='clientes'),
    path('fornecedores/', views.fornecedores, name='fornecedores'),
    path('fornecedores/<int:page_index>', views.fornecedores_pagination, name='fornecedores'),
    path('contas-bancarias/', views.contas_bancarias, name='contasbancarias'),
    path('contas-bancarias/<int:page_index>', views.contas_bancarias_pagination, name='contasbancarias'),
    path('planos-contas/', views.plano_de_contas, name='planocontas'),
    path('planos-contas/<int:page_index>', views.plano_de_contas_pagination, name='planocontas'),
    path('formas-pagamento/', views.formas_pagamento, name='formaspagamento'),
    path('formas-pagamento/<int:page_index>', views.formas_pagamento_pagination, name='formaspagamento'),
    path('tesouraria/', views.tesouraria, name='tesouraria'),
    path('tesouraria/<int:page_index>', views.tesouraria_pagination, name='tesouraria'),
]