"""api_rest_finan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'empresas', views.EmpresaViewSet)
router.register(r'clientes', views.ClienteViewSet)
router.register(r'fornecedores', views.FornecedorViewSet)
router.register(r'contas-bancarias', views.ContaBancariaViewSet)
router.register(r'planos-contas', views.PlanoDeContasViewSet)
router.register(r'formas-pagamento', views.FormaDePagamentoViewSet)
router.register(r'lancamentos-a-pagar', views.LancamentoPagarViewSet)
router.register(r'lancamentos-a-receber', views.LancamentoReceberViewSet)
router.register(r'baixas-a-pagar', views.BaixaPagarViewSet)
router.register(r'baixas-a-receber', views.BaixaReceberViewSet)
#router.register(r'tesouraria', views.PlanoDeContasViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]