from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from .models import Empresas
from .models import Clientes
from .models import Fornecedores
from .models import ContasBancarias
from .models import PlanodeContas
from .models import FormasPagamento
from .models import Tesouraria
# pagination
items_for_page = 10

# Create your views here.
def dashboard(request):

    page = {
        "href" : "/dashboard",
        "title" : "Dashboard",
    }

    user = get_info_user_auth()

    context = {
        "descripton" : "Dashboard",
        "page" : page,
        "user" : user,
        "cards" : get_info_cards_top(),
    }
    return render(request, 'financeiro/dashboard.html', context)

def login(request):
    return render(request, 'financeiro/login.html', context)

def empresas(request):
    return empresas_pagination(request, 1)

def empresas_pagination(request, page_index):

    list_empresa = Empresas.objects.all()
    paginator = Paginator(list_empresa, items_for_page)  # Mostra n empresas por página

    try:
        empresas = paginator.page(page_index)
    except (EmptyPage, InvalidPage):
        empresas = paginator.page(paginator.num_pages)

    page = {
        "href": "/empresas",
        "title": "Empresas",
    }

    context = {
        "descripton": "Empresas",
        "page" : page,
        "num_pages": paginator.num_pages,
        "total_itens": len(list_empresa),
        "user": get_info_user_auth(),
        "items": empresas,
        "cards": get_info_cards_top(),
    }

    return render(request, 'financeiro/empresas.html', context)

def clientes(request):
    return clientes_pagination(request, 1)

def clientes_pagination(request, page_index):

    list_clientes = Clientes.objects.all()
    paginator = Paginator(list_clientes, items_for_page)  # Mostra n empresas por página

    try:
        clientes = paginator.page(page_index)
    except (EmptyPage, InvalidPage):
        clientes = paginator.page(paginator.num_pages)

    page = {
        "href": "/clientes",
        "title": "Clientes",
    }

    context = {
        "descripton": "Clientes",
        "page" : page,
        "num_pages": paginator.num_pages,
        "total_items": len(list_clientes),
        "user": get_info_user_auth(),
        "items": clientes,
        "cards": get_info_cards_top(),
    }

    return render(request, 'financeiro/clientes.html', context)

def fornecedores(request):
    return fornecedores_pagination(request, 1)

def fornecedores_pagination(request, page_index):

    list_fornecedor = Fornecedores.objects.all()
    paginator = Paginator(list_fornecedor, items_for_page)  # Mostra n fornecedores por página

    try:
        fornecedores = paginator.page(page_index)
    except (EmptyPage, InvalidPage):
        fornecedores = paginator.page(paginator.num_pages)

    page = {
        "href": "/fornecedores",
        "title": "Fornecedores",
    }

    context = {
        "descripton": "Fornecedores",
        "page" : page,
        "num_pages": paginator.num_pages,
        "total_items": len(list_fornecedor),
        "user": get_info_user_auth(),
        "items": fornecedores,
        "cards": get_info_cards_top(),
    }

    return render(request, 'financeiro/fornecedores.html', context)

def contas_bancarias(request):
    return contas_bancarias_pagination(request, 1)

def contas_bancarias_pagination(request, page_index):

    list_contas_bancarias = ContasBancarias.objects.all()
    paginator = Paginator(list_contas_bancarias, items_for_page)  # Mostra n fornecedores por página

    try:
        contasbancarias = paginator.page(page_index)
    except (EmptyPage, InvalidPage):
        contasbancarias = paginator.page(paginator.num_pages)

    page = {
        "href": "/contas-bancarias",
        "title": "ContasBancarias",
    }

    context = {
        "descripton": "ContasBancarias",
        "page" : page,
        "num_pages": paginator.num_pages,
        "total_items": len(list_contas_bancarias),
        "user": get_info_user_auth(),
        "items": contasbancarias,
        "cards": get_info_cards_top(),
    }
    return render(request, 'financeiro/contasbancarias.html', context)
    
def plano_de_contas(request):
    return plano_de_contas_pagination(request, 1)

def plano_de_contas_pagination(request, page_index):

    list_plano_contas = PlanodeContas.objects.all()
    paginator = Paginator(list_plano_contas, items_for_page)  # Mostra n fornecedores por página

    try:
        planocontas = paginator.page(page_index)
    except (EmptyPage, InvalidPage):
        planocontas = paginator.page(paginator.num_pages)

    page = {
        "href": "/planos-contas",
        "title": "PlanoContas",
    }

    context = {
        "descripton": "PlanoContas",
        "page" : page,
        "num_pages": paginator.num_pages,
        "total_items": len(list_plano_contas),
        "user": get_info_user_auth(),
        "items": planocontas,
        "cards": get_info_cards_top(),
    }
    return render(request, 'financeiro/planocontas.html', context)


def formas_pagamento(request):
    return formas_pagamento_pagination(request, 1)

def formas_pagamento_pagination(request, page_index):

    list_formas_pagamento = FormasPagamento.objects.all()
    paginator = Paginator(list_formas_pagamento, items_for_page)  # Mostra n fornecedores por página

    try:
        formaspagamento = paginator.page(page_index)
    except (EmptyPage, InvalidPage):
        formaspagamento = paginator.page(paginator.num_pages)

    page = {
        "href": "/formas-pagamento",
        "title": "FormasPagamento",
    }

    context = {
        "descripton": "FormasPagamento",
        "page" : page,
        "num_pages": paginator.num_pages,
        "total_items": len(list_formas_pagamento),
        "user": get_info_user_auth(),
        "items": formaspagamento,
        "cards": get_info_cards_top(),
    }

    return render(request, 'financeiro/formaspagamento.html', context)

def tesouraria(request):
    return tesouraria_pagination(request, 1)

def tesouraria_pagination(request, page_index):

    list_tesouraria = Tesouraria.objects.all()
    paginator = Paginator(list_tesouraria, items_for_page)  # Mostra n fornecedores por página

    try:
        tesouraria = paginator.page(page_index)
    except (EmptyPage, InvalidPage):
        tesouraria = paginator.page(paginator.num_pages)

    page = {
        "href": "/tesouraria",
        "title": "Tesouraria",
    }

    context = {
        "descripton": "Tesouraria",
        "page" : page,
        "num_pages": paginator.num_pages,
        "total_items": len(list_tesouraria),
        "user": get_info_user_auth(),
        "items": tesouraria,
        "cards": get_info_cards_top(),
    }

    return render(request, 'financeiro/tesouraria.html', context)

def get_info_user_auth():
    return {
        "img_url": "https://lh4.googleusercontent.com/-iQ04MxZ1EpY/AAAAAAAAAAI/AAAAAAAABLQ/hsldODaCorY/s96-c/photo.jpg",
        "name": "Marcos Sobral",
    }

def get_info_cards_top():
    return {
        "clientes": {
            "total": 200,
            "percent": 7.98,
            "percent_info": "Desde a semana passada",
            "percent_status": "up",
        }
    }