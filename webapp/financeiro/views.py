from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.paginator import Paginator, InvalidPage, EmptyPage
import requests, json
from django.http import HttpResponse

# pagination
items_for_page = 5

# server rest
url = "http://127.0.0.1:8001"

# server app
server = "http://127.0.0.1:8000"

def login(request):
    headers = {
        "Accept": "application/json"
    }

    response = requests.get(url + "/empresas", headers=headers)
    list_empresa = json.loads(response.content)
    return render(request, 'financeiro/login.html', {})

def users(request):
    return users_pagination(request, 1)


def user_view(request, id):
    return view("users", id)

def user_add(request):
    return add(request, "users")


def user_edit(request, id):
    return edit(request, id, "users")


def user_delete(request, id):
    return delete(id, "users")


def users_pagination(request, page_index):
    headers = {
        "Accept": "application/json"
    }

    response = requests.get(url + "/users", headers=headers)
    list_user = json.loads(response.content)
    paginator = Paginator(list_user, items_for_page)  # Mostra n empresas por página

    try:
        users = paginator.page(page_index)
    except (EmptyPage, InvalidPage):
        users = paginator.page(paginator.num_pages)

    page = {
        "href": "/users",
        "title": "Usuários",
        "server": server
    }

    context = {
        "description": "Usuários",
        "page": page,
        "num_pages": paginator.num_pages,
        "total_itens": len(list_user),
        "user": get_info_user_auth(),
        "items": users,
        "cards": get_info_cards_top(),
    }

    return render(request, 'financeiro/users.html', context)

def empresas(request):
    return empresas_pagination(request, 1)


def empresa_view(request, id):
    return view("empresas", id)


def empresa_add(request):
    return add(request, "empresas")


def empresa_edit(request, id):
    return edit(request, id, "empresas")


def empresa_delete(request, id):
    return delete(id, "empresas")


def empresas_pagination(request, page_index):
    headers = {
        "Accept": "application/json"
    }

    response = requests.get(url + "/empresas", headers=headers)
    list_empresa = json.loads(response.content)
    paginator = Paginator(list_empresa, items_for_page)  # Mostra n empresas por página

    try:
        empresas = paginator.page(page_index)
    except (EmptyPage, InvalidPage):
        empresas = paginator.page(paginator.num_pages)

    page = {
        "href": "/empresas",
        "title": "Empresas",
        "server": server
    }

    context = {
        "description": "Empresas",
        "page": page,
        "num_pages": paginator.num_pages,
        "total_itens": len(list_empresa),
        "user": get_info_user_auth(),
        "items": empresas,
        "cards": get_info_cards_top(),
    }

    return render(request, 'financeiro/empresas.html', context)


def clientes(request):
    return clientes_pagination(request, 1)


def cliente_view(request, id):
    return view("clientes", id)


def cliente_add(request):
    return add(request, "clientes")


def cliente_edit(request, id):
    return edit(request, id, "clientes")


def cliente_delete(request, id):
    return delete(id, "clientes")


def clientes_pagination(request, page_index):
    headers = {
        "Accept": "application/json"
    }

    response = requests.get(url + "/clientes", headers=headers)
    list_clientes = json.loads(response.content)
    paginator = Paginator(list_clientes, items_for_page)  # Mostra n empresas por página

    try:
        clientes = paginator.page(page_index)
    except (EmptyPage, InvalidPage):
        clientes = paginator.page(paginator.num_pages)

    page = {
        "href": "/clientes",
        "title": "Clientes",
        "server": server
    }

    context = {
        "description": "Clientes",
        "page": page,
        "num_pages": paginator.num_pages,
        "total_items": len(list_clientes),
        "user": get_info_user_auth(),
        "items": clientes,
        "cards": get_info_cards_top(),
    }

    return render(request, 'financeiro/clientes.html', context)


def fornecedores(request):
    return fornecedores_pagination(request, 1)


def fornecedor_view(request, id):
    return view("fornecedores", id)


def fornecedor_add(request):
    return add(request, "fornecedores")


def fornecedor_edit(request, id):
    return edit(request, id, "fornecedores")


def fornecedor_delete(request, id):
    return delete(id, "fornecedores")


def fornecedores_pagination(request, page_index):
    headers = {
        "Accept": "application/json"
    }

    response = requests.get(url + "/fornecedores", headers=headers)
    list_fornecedor = json.loads(response.content)
    paginator = Paginator(list_fornecedor, items_for_page)  # Mostra n fornecedores por página

    try:
        fornecedores = paginator.page(page_index)
    except (EmptyPage, InvalidPage):
        fornecedores = paginator.page(paginator.num_pages)

    page = {
        "href": "/fornecedores",
        "title": "Fornecedores",
        "server": server
    }

    context = {
        "description": "Fornecedores",
        "page": page,
        "num_pages": paginator.num_pages,
        "total_items": len(list_fornecedor),
        "user": get_info_user_auth(),
        "items": fornecedores,
        "cards": get_info_cards_top(),
    }

    return render(request, 'financeiro/fornecedores.html', context)


def contas_bancarias(request):
    return contas_bancarias_pagination(request, 1)


def contas_bancarias_view(request, id):
    return view("contas-bancarias", id)


def contas_bancarias_add(request):
    return add(request, "contas-bancarias")


def contas_bancarias_edit(request, id):
    return edit(request, id, "contas-bancarias")


def contas_bancarias_delete(request, id):
    return delete(id, "contas-bancarias")


def contas_bancarias_pagination(request, page_index):
    headers = {
        "Accept": "application/json"
    }

    response = requests.get(url + "/contas-bancarias", headers=headers)
    list_contas_bancarias = json.loads(response.content)
    paginator = Paginator(list_contas_bancarias, items_for_page)  # Mostra n fornecedores por página

    try:
        contasbancarias = paginator.page(page_index)
    except (EmptyPage, InvalidPage):
        contasbancarias = paginator.page(paginator.num_pages)

    page = {
        "href": "/contas-bancarias",
        "title": "Contas Bancárias",
        "server": server
    }

    context = {
        "description": "Contas Bancárias",
        "page": page,
        "num_pages": paginator.num_pages,
        "total_items": len(list_contas_bancarias),
        "user": get_info_user_auth(),
        "items": contasbancarias,
        "cards": get_info_cards_top(),
    }
    return render(request, 'financeiro/contasbancarias.html', context)


def plano_de_contas(request):
    return plano_de_contas_pagination(request, 1)


def plano_de_contas_view(request, id):
    return view("planos-contas", id)


def plano_de_contas_add(request):
    return add(request, "planos-contas")


def plano_de_contas_edit(request, id):
    return edit(request, id, "planos-contass")


def plano_de_contas_delete(request, id):
    return delete(id, "planos-contas")


def plano_de_contas_pagination(request, page_index):
    headers = {
        "Accept": "application/json"
    }

    response = requests.get(url + "/planos-contas", headers=headers)
    list_plano_contas = json.loads(response.content)
    paginator = Paginator(list_plano_contas, items_for_page)  # Mostra n fornecedores por página

    try:
        planocontas = paginator.page(page_index)
    except (EmptyPage, InvalidPage):
        planocontas = paginator.page(paginator.num_pages)

    page = {
        "href": "/planos-contas",
        "title": "PlanoContas",
        "server": server
    }

    context = {
        "descripton": "PlanoContas",
        "page": page,
        "num_pages": paginator.num_pages,
        "total_items": len(list_plano_contas),
        "user": get_info_user_auth(),
        "items": planocontas,
        "cards": get_info_cards_top(),
    }
    return render(request, 'financeiro/planocontas.html', context)

def formas_pagamento(request):
    return formas_pagamento_pagination(request, 1)


def formas_pagamento_view(request, id):
    return view("formas-pagamento", id)


def formas_pagamento_add(request):
    return add(request, "formas-pagamento")


def formas_pagamento_edit(request, id):
    return edit(request, id, "formas-pagamento")


def formas_pagamento_delete(request, id):
    return delete(id, "formas-pagamento")


def formas_pagamento_pagination(request, page_index):
    headers = {
        "Accept": "application/json"
    }

    response = requests.get(url + "/formas-pagamento", headers=headers)
    list_formas_pagamento = json.loads(response.content)
    paginator = Paginator(list_formas_pagamento, items_for_page)  # Mostra n fornecedores por página

    try:
        formaspagamento = paginator.page(page_index)
    except (EmptyPage, InvalidPage):
        formaspagamento = paginator.page(paginator.num_pages)

    page = {
        "href": "/formas-pagamento",
        "title": "Formas de Pagamento",
        "server": server
    }

    context = {
        "description": "Formas de Pagamento",
        "page": page,
        "num_pages": paginator.num_pages,
        "total_items": len(list_formas_pagamento),
        "user": get_info_user_auth(),
        "items": formaspagamento,
        "cards": get_info_cards_top(),
    }
    return render(request, 'financeiro/formaspagamento.html', context)


def tesouraria(request):
    return tesouraria_pagination(request, 1)


def tesouraria_view(request, id):
    return view("tesouraria", id)


def tesouraria_add(request):
    return add(request, "tesouraria")


def tesouraria_edit(request, id):
    return edit(request, id, "tesouraria")


def tesouraria_delete(request, id):
    return delete(id, "tesouraria")


def tesouraria_pagination(request, page_index):
    headers = {
        "Accept": "application/json"
    }

    response = requests.get(url + "/tesouraria", headers=headers)
    list_tesouraria = json.loads(response.content)
    paginator = Paginator(list_tesouraria, items_for_page)  # Mostra n fornecedores por página

    try:
        tesouraria = paginator.page(page_index)
    except (EmptyPage, InvalidPage):
        tesouraria = paginator.page(paginator.num_pages)

    # Carregando combobox para o modals
    combobox_empresas = json.loads(view("empresas", "").content)
    combobox_fornecedores = json.loads(view("fornecedores", "").content)
    combobox_formas_de_pagamento = json.loads(view("formas-pagamento", "").content)
    combobox_planos_conta = json.loads(view("planos-contas", "").content)

    page = {
        "href": "/tesouraria",
        "title": "Tesouraria",
        "server": server
    }

    context = {
        "description": "Tesouraria",
        "page": page,
        "num_pages": paginator.num_pages,
        "total_items": len(list_tesouraria),
        "user": get_info_user_auth(),
        "items": tesouraria,
        "cards": get_info_cards_top(),
        "combobox_empresas": combobox_empresas,
        "combobox_fornecedores": combobox_fornecedores,
        "combobox_formas_pagamento": combobox_formas_de_pagamento,
        "combobox_planos_conta": combobox_planos_conta,
    }
    return render(request, 'financeiro/tesouraria.html', context)


def lancamentos_a_receber(request):
    return lancamentos_a_receber_pagination(request, 1)


def lancamentos_a_receber_view(request, id):
    return view("lancamentos-a-receber", id)


def lancamentos_a_receber_add(request):
    return add(request, "lancamentos-a-receber")


def lancamentos_a_receber_edit(request, id):
    return edit(request, id, "lancamentos-a-receber")


def lancamentos_a_receber_delete(request, id):
    return delete(id, "lancamentos-a-receber")


def lancamentos_a_receber_pagination(request, page_index):
    headers = {
        "Accept": "application/json"
    }

    response = requests.get(url + "/lancamentos-a-receber", headers=headers)
    list_lancamento_a_receber = json.loads(response.content)
    paginator = Paginator(list_lancamento_a_receber, items_for_page)  # Mostra n fornecedores por página

    try:
        lancamentos = paginator.page(page_index)
    except (EmptyPage, InvalidPage):
        lancamentos = paginator.page(paginator.num_pages)

    # Carregando combobox para o modals
    combobox_empresas = json.loads(view("empresas", "").content)
    combobox_fornecedores = json.loads(view("fornecedores", "").content)
    combobox_formas_de_pagamento = json.loads(view("formas-pagamento", "").content)

    page = {
        "href": "/lancamentos-a-receber",
        "title": "Lançamentos a Receber",
        "server": server
    }

    context = {
        "description": "Lançamentos a Receber",
        "page": page,
        "num_pages": paginator.num_pages,
        "total_items": len(list_lancamento_a_receber),
        "user": get_info_user_auth(),
        "items": lancamentos,
        "cards": get_info_cards_top(),
        "combobox_empresas": combobox_empresas,
        "combobox_fornecedores": combobox_fornecedores,
        "combobox_formas_pagamento": combobox_formas_de_pagamento,
    }

    return render(request, 'financeiro/lancamentos-a-receber.html', context)


def lancamentos_a_pagar(request):
    return lancamentos_a_pagar_pagination(request, 1)


def lancamentos_a_pagar_view(request, id):
    return view("lancamentos-a-pagar", id)


def lancamentos_a_pagar_add(request):
    return add(request, "lancamentos-a-pagar")


def lancamentos_a_pagar_edit(request, id):
    return edit(request, id, "lancamentos-a-pagar")


def lancamentos_a_pagar_delete(request, id):
    return delete(id, "lancamentos-a-pagar")


def lancamentos_a_pagar_pagination(request, page_index):
    headers = {
        "Accept": "application/json"
    }

    response = requests.get(url + "/lancamentos-a-pagar", headers=headers)
    list_lancamento_a_pagar = json.loads(response.content)
    paginator = Paginator(list_lancamento_a_pagar, items_for_page)  # Mostra n fornecedores por página

    try:
        lancamentos = paginator.page(page_index)
    except (EmptyPage, InvalidPage):
        lancamentos = paginator.page(paginator.num_pages)

    # Carregando combobox para o modals
    combobox_empresas = json.loads(view("empresas", "").content)
    combobox_fornecedores = json.loads(view("fornecedores", "").content)
    combobox_formas_de_pagamento = json.loads(view("formas-pagamento", "").content)

    page = {
        "href": "/lancamentos-a-pagar",
        "title": "Lançamentos a Pagar",
        "server": server
    }

    context = {
        "description": "Lançamentos a Pagar",
        "page": page,
        "num_pages": paginator.num_pages,
        "total_items": len(list_lancamento_a_pagar),
        "user": get_info_user_auth(),
        "items": lancamentos,
        "cards": get_info_cards_top(),
        "combobox_empresas": combobox_empresas,
        "combobox_fornecedores": combobox_fornecedores,
        "combobox_formas_pagamento": combobox_formas_de_pagamento,
    }

    return render(request, 'financeiro/lancamentos-a-pagar.html', context)


def baixas_a_receber(request):
    return baixas_a_receber_pagination(request, 1)


def baixas_a_receber_view(request, id):
    return view("baixas-a-receber", id)


def baixas_a_receber_add(request):
    return add(request, "baixas-a-receber")


def baixas_a_receber_edit(request, id):
    return edit(request, id, "baixas-a-receber")


def baixas_a_receber_delete(request, id):
    return delete(id, "baixas-a-receber")


def baixas_a_receber_pagination(request, page_index):
    headers = {
        "Accept": "application/json"
    }

    response = requests.get(url + "/baixas-a-receber", headers=headers)
    list_baixa_a_receber = json.loads(response.content)
    paginator = Paginator(list_baixa_a_receber, items_for_page)  # Mostra n fornecedores por página

    try:
        baixas = paginator.page(page_index)
    except (EmptyPage, InvalidPage):
        baixas = paginator.page(paginator.num_pages)

    page = {
        "href": "/baixas-a-receber",
        "title": "Baixas a Receber",
        "server": server
    }

    # Carregando combobox para o modals
    combobox_empresas = json.loads(view("empresas", "").content)
    combobox_fornecedores = json.loads(view("fornecedores", "").content)
    combobox_formas_de_pagamento = json.loads(view("formas-pagamento", "").content)

    context = {
        "description": "Baixas a Receber",
        "page": page,
        "num_pages": paginator.num_pages,
        "total_items": len(list_baixa_a_receber),
        "user": get_info_user_auth(),
        "items": baixas,
        "cards": get_info_cards_top(),
        "combobox_empresas": combobox_empresas,
        "combobox_fornecedores": combobox_fornecedores,
        "combobox_formas_pagamento": combobox_formas_de_pagamento,
    }

    return render(request, 'financeiro/baixas-a-receber.html', context)


def baixas_a_pagar(request):
    return baixas_a_pagar_pagination(request, 1)


def baixas_a_pagar_view(request, id):
    return view("baixas-a-pagar", id)


def baixas_a_pagar_add(request):
    return add(request, "baixas-a-pagar")


def baixas_a_pagar_edit(request, id):
    return edit(request, id, "baixas-a-pagar")


def baixas_a_pagar_delete(request, id):
    return delete(id, "baixas-a-pagar")


def baixas_a_pagar_pagination(request, page_index):
    headers = {
        "Accept": "application/json"
    }

    response = requests.get(url + "/baixas-a-pagar", headers=headers)
    list_baixa_a_pagar = json.loads(response.content)
    paginator = Paginator(list_baixa_a_pagar, items_for_page)  # Mostra n fornecedores por página

    try:
        baixas = paginator.page(page_index)
    except (EmptyPage, InvalidPage):
        baixas = paginator.page(paginator.num_pages)

    page = {
        "href": "/baixas-a-pagar",
        "title": "Baixas a Pagar",
        "server": server
    }

    # Carregando combobox para o modals
    combobox_empresas = json.loads(view("empresas", "").content)
    combobox_fornecedores = json.loads(view("fornecedores", "").content)
    combobox_formas_de_pagamento = json.loads(view("formas-pagamento", "").content)

    context = {
        "description": "Baixas a Pagar",
        "page": page,
        "num_pages": paginator.num_pages,
        "total_items": len(list_baixa_a_pagar),
        "user": get_info_user_auth(),
        "items": baixas,
        "cards": get_info_cards_top(),
        "combobox_empresas": combobox_empresas,
        "combobox_fornecedores": combobox_fornecedores,
        "combobox_formas_pagamento": combobox_formas_de_pagamento,
    }

    return render(request, 'financeiro/baixas-a-pagar.html', context)


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


def view(model, id):
    headers = {
        "Accept": "application/json"
    }

    response = requests.get(url + "/" + model + "/%s" % id, headers=headers)

    return HttpResponse(response)


def add(request, model):
    headers = {
        "Accept": "application/json"
    }
    if request.method == "POST":
        data = json.loads(request.POST.get("form"))
        response = requests.post(url + "/" + model + "/", data, headers=headers)

    return HttpResponse(response)


def edit(request, id, model):
    headers = {
        "Accept": "application/json"
    }
    if request.method == "POST":
        data = json.loads(request.POST.get("form"))
        response = requests.put(url + "/" + model + "/%s/" % id, data, headers=headers)

    return HttpResponse(response)


def delete(id, model):
    headers = {
        "Accept": "application/json"
    }

    response = requests.delete(url + "/" + model + "/%s/" % id, headers=headers)

    return HttpResponse(response)
