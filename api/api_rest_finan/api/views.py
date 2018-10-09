from django.contrib.auth.models import User, Group
from .models import Empresa, Cliente, Fornecedor, ContaBancaria, PlanoDeContas, FormaDePagamento, LancamentoPagar, LancamentoReceber, Tesouraria
from rest_framework import viewsets
from api.serializers import UserSerializer, GroupSerializer, EmpresaSerializer, ClienteSerializer, FornecedorSerializer, ContaBancariaSerializer, PlanoDeContasSerializer, FormaDePagamentoSerializer, LancamentoPagarSerializer, LancamentoReceberSerializer, TesourariaSerializer

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
	queryset = LancamentoReceber.objects.exclude(data_baixa__isnull=False).exclude(valor_pago__isnull=False)
	serializer_class = LancamentoReceberSerializer

class LancamentoPagarViewSet(viewsets.ModelViewSet):
	queryset = LancamentoPagar.objects.exclude(data_baixa__isnull=False).exclude(valor_pago__isnull=False)
	serializer_class = LancamentoPagarSerializer

class BaixaReceberViewSet(viewsets.ModelViewSet):
	queryset = LancamentoReceber.objects.all().exclude(valor_pago__isnull=True)
	serializer_class = LancamentoReceberSerializer

class BaixaPagarViewSet(viewsets.ModelViewSet):
	queryset = LancamentoPagar.objects.all().exclude(valor_pago__isnull=True)
	serializer_class = LancamentoPagarSerializer

class TesourariaViewSet(viewsets.ModelViewSet):
	queryset = Tesouraria.objects.all()
	serializer_class = TesourariaSerializer