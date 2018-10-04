from django.contrib.auth.models import User, Group
from .models import Empresa, Cliente, Fornecedor, ContaBancaria, 
	PlanoDeContas, FormaDePagamento, LancamentoPagar, LancamentoReceber, 
	BaixaPagar, BaixaReceber, Tesouraria
from rest_framework import viewsets
from trabweb.api_rest.serializers import UserSerializer, GroupSerializer,
	EmpresaSerializer, ClienteSerializer, FornecedorSerializer, ContaBancariaSerializer, 
	PlanoDeContasSerializer, FormaDePagamentoSerializer, LancamentoPagarSerializer, 
	LancamentoReceberSerializer, BaixaPagarSerializer, BaixaReceberSerializer, TesourariaSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class EmpresaViewSet(viewsets.ModelViewSet):
	queryset = Empresa.objects.all()
	serializer_class = EmpresaSerializer

class ClienteViewSet(viewsets.ModelViewSet):
	queryset = Cliente.objects.all()
	serializer_class = ClienteSerializer

class FornecedorViewSet(viewsets.ModelViewSet):
	queryset = Fornecedor.objects.all()
	serializer_class = FornecedorSerializer

class ContaBancariaViewSet(viewsets.ModelViewSet):
	queryset = ContaBancaria.objects.all()
	serializer_class = ContaBancariaSerializer

class PlanoDeContasViewSet(viewsets.ModelViewSet):
	queryset = PlanoDeContas.objects.all()
	serializer_class = PlanoDeContasSerializer

class FormaDePagamentoViewSet(viewsets.ModelViewSet):
	queryset = FormaDePagamento.objects.all()
	serializer_class = FormaDePagamentoSerializer

class LancamentoReceberViewSet(viewsets.ModelViewSet):
	queryset = LancamentoReceber.objects.all()
	serializer_class = LancamentoReceberSerializer

class LancamentoPagarViewSet(viewsets.ModelViewSet):
	queryset = LancamentoPagar.objects.all()
	serializer_class = LancamentoPagarSerializer

class BaixaReceberViewSet(viewsets.ModelViewSet):
	queryset = BaixaReceber.objects.all()
	serializer_class = BaixaReceberSerializer

class BaixaReceberViewSet(viewsets.ModelViewSet):
	queryset = Tesouraria.objects.all()
	serializer_class = TesourariaSerializer