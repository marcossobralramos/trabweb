from django.db import models

# Create your models here.
class Usuarios(models.Model):
    
        idUsuario = models.IntegerField(primary_key = True)
        usuario = models.CharField(max_length=50)
        nome = models.CharField(max_length=50)
        senha = models.CharField(max_length=22)
        confirmaSenha = models.CharField( max_length=22)
        
        def __str__(self):
            """String for representing the Model object."""
            return self.usuario
   
class Empresas(models.Model):
    
        idEmpresas = models.IntegerField(primary_key = True)
        razaoSocial = models.CharField(max_length=50)
        identificacao = models.CharField(max_length=50)
        tipoPessoa = models.CharField(max_length=10)
        cnpj = models.CharField(max_length=15)
        inscricaoEstadual = models.CharField(max_length=20)
        inscricaoMunicipal = models.CharField(max_length=20)
        endereco = models.CharField(max_length=50)
        bairro = models.CharField(max_length=50)
        municipio = models.CharField(max_length=50)
        cep = models.CharField(max_length=10)
        uf = models.CharField(max_length=2)
        telefone = models.CharField(max_length=20)
        email = models.CharField(max_length=50)
        nomeTitular = models.CharField(max_length=50)
        cpf = models.CharField(max_length=15)
        funcao = models.CharField(max_length=50)
        
        def __str__(self):
            """String for representing the Model object."""
            return self.identificacao

class Clientes(models.Model):
    
        idClientes = models.IntegerField(primary_key = True)
        razaoSocial = models.CharField(max_length=50)
        identificacao = models.CharField(max_length=50)
        tipoPessoa = models.CharField(max_length=10)
        cnpjCpf = models.CharField(max_length=15)
        inscricaoEstadual = models.CharField(max_length=20)
        inscricaoMunicipal = models.CharField(max_length=20)
        endereco = models.CharField(max_length=50)
        bairro = models.CharField(max_length=50)
        municipio = models.CharField(max_length=50)
        cep = models.CharField(max_length=10)
        uf = models.CharField(max_length=2)
        telefone = models.CharField(max_length=20)
        email = models.CharField(max_length=50)
        nomeTitular = models.CharField(max_length=50)
        cpf = models.CharField(max_length=15)
        funcao = models.CharField(max_length=50)
        
        def __str__(self):
            """String for representing the Model object."""
            return self.identificacao

class Fornecedores(models.Model):
    
        idFornecedores = models.IntegerField(primary_key = True)
        razaoSocial = models.CharField(max_length=50)
        identificacao = models.CharField(max_length=50)
        tipoPessoa = models.CharField(max_length=10)
        cnpjCpf = models.CharField(max_length=15)
        inscricaoEstadual = models.CharField(max_length=20)
        inscricaoMunicipal = models.CharField(max_length=20)
        endereco = models.CharField(max_length=50)
        bairro = models.CharField(max_length=50)
        municipio = models.CharField(max_length=50)
        cep = models.CharField(max_length=10)
        uf = models.CharField(max_length=2)
        telefone = models.CharField(max_length=20)
        email = models.CharField(max_length=50)
        nomeTitular = models.CharField(max_length=50)
        cpf = models.CharField(max_length=15)
        funcao = models.CharField(max_length=50)
        
        def __str__(self):
            """String for representing the Model object."""
            return self.identificacao

class ContasBancarias(models.Model):
    
        idContasBancarias = models.IntegerField(primary_key = True)
        classificacao = models.CharField(max_length=18)
        descricao = models.CharField(max_length=50)
        numeroConta = models.CharField(max_length=20)
        numeroAgencia = models.CharField(max_length=20)
        dataSaldoInicial = models.CharField(max_length=12)
        saldoInicial = models.CharField(max_length=14)
        caixa = models.CharField( max_length=1)
        banco = models.CharField( max_length=1)
        
        def __str__(self):
            """String for representing the Model object."""
            return self.idContasBancarias

class PlanodeContas(models.Model):
    
        idPlanodeContas = models.IntegerField(primary_key = True)
        idContasBancarias =  models.ForeignKey(ContasBancarias, on_delete=models.SET_NULL, null=True)
        classificacao = models.CharField(max_length=18)
        tipoConta = models.CharField(max_length=15)
        descricao = models.CharField(max_length=50)
        caixa = models.CharField( max_length=1)
        banco = models.CharField( max_length=1)
        cliente = models.CharField(max_length=1)
        fornecedor = models.CharField(max_length=1)
        entradaRecurso = models.CharField(max_length=1)
        saidaRecurso = models.CharField(max_length=1)
        
        
        def __str__(self):
            """String for representing the Model object."""
            return self.idPlanodeContas

class FormasPagamento(models.Model):
        idFormasPagamento = models.CharField(max_length=11)
        descricao = models.CharField(max_length=50)

        def __str__(self):
            return self.classificacao

class Tesouraria(models.Model):
    
        idTesouraria = models.IntegerField(primary_key = True)
        idEmpresas =  models.ForeignKey(Empresas, on_delete=models.CASCADE, null=True)
        idClientes =  models.ForeignKey(Clientes, on_delete=models.SET_NULL, null=True)
        idPlanodeContas = models.ForeignKey(PlanodeContas, on_delete = models.CASCADE, null=True)
        idFormasPagamento = models.ForeignKey(FormasPagamento, on_delete = models.CASCADE, null=True)
        idFornecedores = models.ForeignKey(Fornecedores, on_delete = models.CASCADE, null=True)
        valor = models.CharField( max_length=14)
        numero = models.CharField( max_length=15)
        dataEmissao = models.CharField(max_length=12)
        dataVencimento = models.CharField(max_length=12)
        dataDisponibilidade = models.CharField(max_length=12)
      
        
        def __str__(self):
            """String for representing the Model object."""
            return self.idTesouraria

class LancamentoReceber(models.Model):
    
        idLancamentosReceber = models.IntegerField(primary_key = True)
        idClientes =  models.ForeignKey(Clientes, on_delete=models.CASCADE, null=True)
        idEmpresas=  models.ForeignKey(Empresas, on_delete=models.SET_NULL, null=True)
        dataEmissao = models.CharField(max_length=12)
        dataVencimento = models.CharField(max_length=12)
        valorTitulo = models.CharField(max_length=14)
        numeroDocumento = models.CharField(max_length=20)
      
        
        def __str__(self):
            """String for representing the Model object."""
            return self.idLancamentosReceber

class LancamentoPagar(models.Model):
    
        idLancamentosPagar = models.IntegerField(primary_key = True)
        idFornecedores =  models.ForeignKey(Fornecedores, on_delete=models.CASCADE, null=True)
        idEmpresas=  models.ForeignKey(Empresas, on_delete=models.SET_NULL, null=True)
        dataEmissao = models.CharField(max_length=12)
        dataVencimento = models.CharField(max_length=12)
        valorTitulo = models.CharField(max_length=14)
        numeroDocumento = models.CharField(max_length=20)
      
        
        def __str__(self):
            """String for representing the Model object."""
            return self.idLancamentosPagar
    
class BaixaPagar(models.Model):
    
        idBaixasPagar = models.IntegerField(primary_key = True)
        idFormasPagamento =  models.ForeignKey(FormasPagamento, on_delete=models.CASCADE, null=True)
        banco = models.CharField(max_length=50)
        disponibilidade = models.CharField(max_length=12)
        dataBaixa = models.CharField(max_length=12)
        valorPago = models.CharField(max_length=14)
        residual = models.CharField(max_length=14)
      
        
        def __str__(self):
            """String for representing the Model object."""
            return self.idBaixasPagar

class BaixaReceber(models.Model):
    
        idBaixasReceber = models.IntegerField(primary_key = True)
        idFormasPagamento =  models.ForeignKey(FormasPagamento, on_delete=models.CASCADE, null=True)
        idLancamentosReceber =  models.ForeignKey(LancamentoReceber, on_delete=models.CASCADE, null=True)
        banco = models.CharField(max_length=50)
        disponibilidade = models.CharField(max_length=12)
        dataBaixa = models.CharField(max_length=12)
        valorPago = models.CharField(max_length=14)
        residual = models.CharField(max_length=14)
      
        
        def __str__(self):
            """String for representing the Model object."""
            return self.idBaixasReceber
    
    
