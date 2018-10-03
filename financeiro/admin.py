from django.contrib import admin
from .models import Usuarios
from .models import Empresas
from .models import Clientes
from .models import Fornecedores
from .models import ContasBancarias
from .models import PlanodeContas
from .models import FormasPagamento
from .models import LancamentoReceber
from .models import LancamentoPagar
from .models import BaixaPagar
from .models import BaixaReceber


#Categoria, BOok, Alunos, Emprestimo
admin.site.register(Usuarios)
admin.site.register(Empresas)
admin.site.register(Clientes)
admin.site.register(Fornecedores)
admin.site.register(ContasBancarias)
admin.site.register(PlanodeContas)
admin.site.register(FormasPagamento)
admin.site.register(LancamentoReceber)
admin.site.register(LancamentoPagar)
admin.site.register(BaixaPagar)
admin.site.register(BaixaReceber)

# Register your models here.
