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
]