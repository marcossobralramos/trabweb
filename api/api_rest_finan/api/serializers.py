from django.contrib.auth.models import User, Group
from .models import Empresa, Cliente, Fornecedor, ContaBancaria, PlanoDeContas, FormaDePagamento, LancamentoPagar, LancamentoReceber, Tesouraria
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class EmpresaSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Empresa
		fields = (
			'id_empresa', 'razao_social', 'identificacao', 'tipo_pessoa',
			'cnpj_cpf', 'inscricao_estadual', 'inscricao_municipal',
			'endereco', 'bairro', 'municipio', 'cep', 'uf', 'telefone',
			'email', 'nome_titular', 'cpf', 'funcao'
		)

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Cliente
		fields = (
			'id_cliente', 'razao_social', 'identificacao', 'tipo_pessoa',
			'cnpj_cpf', 'inscricao_estadual', 'inscricao_municipal',
			'endereco', 'bairro', 'municipio', 'cep', 'uf', 'telefone',
			'email', 'nome_titular', 'cpf', 'funcao'
		)

class FornecedorSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Fornecedor
		fields = (
			'id_fornecedor', 'razao_social', 'identificacao', 'tipo_pessoa',
			'cnpj_cpf', 'inscricao_estadual', 'inscricao_municipal',
			'endereco', 'bairro', 'municipio', 'cep', 'uf', 'telefone',
			'email', 'nome_titular', 'cpf', 'funcao'
		)

class ContaBancariaSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = ContaBancaria
		fields = (
			'id_conta_bancaria', 'classificacao', 'descricao', 'numero_conta',
			'numero_agencia', 'data_saldo_inicial', 'saldo_inicial',
			'caixa', 'banco'
		)

class PlanoDeContasSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
         model = PlanoDeContas
         fields = (
			'id_plano_de_contas', 'id_conta_bancaria', 'classificacao', 'tipo_conta',
			'descricao', 'caixa', 'banco','cliente', 'fornecedor', 'entrada_recurso',
			'saida_recurso'
         )

class FormaDePagamentoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
         model = FormaDePagamento
         fields = (
			'id_forma_pagamento', 'descricao'
		 )

class LancamentoPagarSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = LancamentoPagar
		fields = (
			'id_lancamento_pagar', 'id_fornecedor', 'id_empresa', 'data_emissao',
			'data_vencimento', 'valor_titulo', 'numero_documento', 'data_baixa', 'valor_pago',
			'id_forma_pagamento'
		)

class LancamentoReceberSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = LancamentoReceber
		fields = (
			'id_lancamento_receber', 'id_cliente', 'id_empresa', 'data_emissao',
			'data_vencimento', 'valor_titulo', 'numero_documento', 'data_baixa', 'valor_pago',
			'id_forma_pagamento'
		)



class TesourariaSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
         model = Tesouraria
         fields = (
			'id_tesouraria', 'id_Empresa', 'id_clientes', 'id_plano_de_contas',
			'id_formas_pagamento', 'id_fornecedor', 'valor',
			'numero', 'data_emissao','data_vencimento', 'data_disponibilidade'
		 )