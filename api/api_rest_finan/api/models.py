from django.db import models

class Empresa(models.Model):

    id_empresa = models.AutoField(primary_key = True)
    razao_social = models.CharField(max_length=50)
    identificacao = models.CharField(max_length=50)
    tipo_pessoa = models.CharField(max_length=10)
    cnpj_cpf = models.CharField(max_length=15)
    inscricao_estadual = models.CharField(max_length=20)
    inscricao_municipal = models.CharField(max_length=20)
    endereco = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    municipio = models.CharField(max_length=50)
    cep = models.CharField(max_length=10)
    uf = models.CharField(max_length=2)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    nome_titular = models.CharField(max_length=50)
    cpf = models.CharField(max_length=15)
    funcao = models.CharField(max_length=50)
    
    def __str__(self):
        """String for representing the Model object."""
        return self.identificacao

class Cliente(models.Model):
    
    id_cliente = models.AutoField(primary_key = True)
    razao_social = models.CharField(max_length=50)
    identificacao = models.CharField(max_length=50)
    tipo_pessoa = models.CharField(max_length=10)
    cnpj_cpf = models.CharField(max_length=15)
    inscricao_estadual = models.CharField(max_length=20)
    inscricao_municipal = models.CharField(max_length=20)
    endereco = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    municipio = models.CharField(max_length=50)
    cep = models.CharField(max_length=10)
    uf = models.CharField(max_length=2)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    nome_titular = models.CharField(max_length=50)
    cpf = models.CharField(max_length=15)
    funcao = models.CharField(max_length=50)
    
    def __str__(self):
        """String for representing the Model object."""
        return self.identificacao

class Fornecedor(models.Model):
    
    id_fornecedor = models.AutoField(primary_key = True)
    razao_social = models.CharField(max_length=50)
    identificacao = models.CharField(max_length=50)
    tipo_pessoa = models.CharField(max_length=10)
    cnpj_cpf = models.CharField(max_length=15)
    inscricao_estadual = models.CharField(max_length=20)
    inscricao_municipal = models.CharField(max_length=20)
    endereco = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    municipio = models.CharField(max_length=50)
    cep = models.CharField(max_length=10)
    uf = models.CharField(max_length=2)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    nome_titular = models.CharField(max_length=50)
    cpf = models.CharField(max_length=15)
    funcao = models.CharField(max_length=50)
    
    def __str__(self):
        """String for representing the Model object."""
        return self.identificacao

class ContaBancaria(models.Model):
    
    id_conta_bancaria = models.AutoField(primary_key = True)
    classificacao = models.CharField(max_length=18)
    descricao = models.CharField(max_length=50)
    numero_conta = models.CharField(max_length=20)
    numero_agencia = models.CharField(max_length=20)
    data_saldo_inicial = models.CharField(max_length=12)
    saldo_inicial = models.CharField(max_length=14)
    caixa = models.CharField(max_length=1)
    banco = models.CharField(max_length=1)
    
    def __str__(self):
        """String for representing the Model object."""
        return self.id_conta_bancaria

class PlanoDeContas(models.Model):
    
    id_plano_de_contas = models.AutoField(primary_key = True)
    id_conta_bancaria =  models.ForeignKey(ContaBancaria, on_delete=models.SET_NULL, null=True)
    classificacao = models.CharField(max_length=18)
    tipo_conta = models.CharField(max_length=15)
    descricao = models.CharField(max_length=50)
    caixa = models.CharField( max_length=1)
    banco = models.CharField( max_length=1)
    cliente = models.CharField(max_length=1)
    fornecedor = models.CharField(max_length=1)
    entrada_recurso = models.CharField(max_length=1)
    saida_recurso = models.CharField(max_length=1)
    
    def __str__(self):
        """String for representing the Model object."""
        return self.descricao

class FormaDePagamento(models.Model):

    id_forma_pagamento = models.AutoField(primary_key=True, max_length=11)
    descricao = models.CharField(max_length=50)

    def __str__(self):
        return self.descricao

class Tesouraria(models.Model):
    
    id_tesouraria = models.AutoField(primary_key = True)
    id_Empresa =  models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True)
    id_clientes =  models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    id_plano_de_contas = models.ForeignKey(PlanoDeContas, on_delete = models.CASCADE, null=True)
    id_formas_pagamento = models.ForeignKey(FormaDePagamento, on_delete = models.CASCADE, null=True)
    id_fornecedor = models.ForeignKey(Fornecedor, on_delete = models.CASCADE, null=True)
    valor = models.CharField( max_length=14)
    numero = models.CharField( max_length=15)
    data_emissao = models.CharField(max_length=12)
    data_vencimento = models.CharField(max_length=12)
    data_disponibilidade = models.CharField(max_length=12)
        
    def __str__(self):
        """String for representing the Model object."""
        return self.id_tesouraria

class LancamentoReceber(models.Model):
    
    id_lancamento_receber = models.AutoField(primary_key = True)
    id_cliente =  models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True)
    id_empresa =  models.ForeignKey(Empresa, on_delete=models.SET_NULL, null=True)
    data_emissao = models.CharField(max_length=12)
    data_vencimento = models.CharField(max_length=12)
    valor_titulo = models.CharField(max_length=14)
    numero_documento = models.CharField(max_length=20)
    data_baixa = models.CharField(max_length=12, null=True)
    valor_pago = models.CharField(max_length=14, null=True)
    id_forma_pagamento = models.ForeignKey(FormaDePagamento, on_delete=models.CASCADE, null=True)
  
    def __str__(self):
        """String for representing the Model object."""
        return self.id_lancamento_receber

class LancamentoPagar(models.Model):
    
    id_lancamento_pagar = models.AutoField(primary_key = True)
    id_fornecedor =  models.ForeignKey(Fornecedor, on_delete=models.CASCADE, null=True)
    id_empresa=  models.ForeignKey(Empresa, on_delete=models.SET_NULL, null=True)
    data_emissao = models.CharField(max_length=12)
    data_vencimento = models.CharField(max_length=12)
    valor_titulo = models.CharField(max_length=14)
    numero_documento = models.CharField(max_length=20)
    data_baixa = models.CharField(max_length=12, null=True)
    valor_pago = models.CharField(max_length=14, null=True)
    id_forma_pagamento = models.ForeignKey(FormaDePagamento, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        """String for representing the Model object."""
        return self.id_lancamento_pagar

'''
class BaixaPagar(models.Model):
  
  id_baixa_pagar = models.AutoField(primary_key = True)
  id_forma_pagamento =  models.ForeignKey(FormaDePagamento, on_delete=models.CASCADE, null=True)
  banco = models.CharField(max_length=50)
  disponibilidade = models.CharField(max_length=12)
  data_baixa = models.CharField(max_length=12)
  valor_pago = models.CharField(max_length=14)
  residual = models.CharField(max_length=14)

  def __str__(self):
      """String for representing the Model object."""
      return self.id_baixa_pagar
'''
'''
class BaixaReceber(models.Model):
    
    id_baixa_receber = models.AutoField(primary_key = True)
    id_forma_pagamento =  models.ForeignKey(FormaDePagamento, on_delete=models.CASCADE, null=True)
    id_lancamento_receber =  models.ForeignKey(LancamentoReceber, on_delete=models.CASCADE, null=True)
    banco = models.CharField(max_length=50)
    disponibilidade = models.CharField(max_length=12)
    data_baixa = models.CharField(max_length=12)
    valor_pago = models.CharField(max_length=14)
    residual = models.CharField(max_length=14)
  
    def __str__(self):
        """String for representing the Model object."""
        return self.id_baixa_receber
'''