from django.shortcuts import render, redirect
from .models import Despesa, Inquilinos, Unidades
from django.contrib import messages
from django.core.paginator import Paginator
from .filters import DespesaFilter



################### INQUILINOS #########################

def inquilinos(request):
    inquilinos = Inquilinos.objects.all()
    paginator = Paginator(inquilinos, 5)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    context = {
        'inquilinos' : inquilinos,
        'page_obj' : page_obj
    }

    return render(request, 'inquilinos/inquilinos.html')


def add_inquilino(request):
    inquilinos = Inquilinos.objects.all()
    context = {
        'values' : request.POST,
        'inquilinos' : inquilinos,
    }
    if request.method == 'GET':
        return render(request, 'inquilinos/add_inquilino.html')

    if request.method == 'POST':
        nome = request.POST['nome'] 
        idade = request.POST['idade']
        sexo = request.POST['sexo'] 
        telefone = request.POST['telefone'] 
        email = request.POST['email']

        if not nome:
            messages.error(request, 'Precisa de um nome!')
            return render(request, 'inquilinos/add_inquilino.html')
        
        if not idade:
            messages.error(request, 'Precisa de uma idade!')
            return render(request, 'inquilinos/add_inquilino.html')
        
        
        if not sexo:
            messages.error(request, 'Precisa de um Sexo')
            return render(request, 'inquilinos/add_inquilino.html')
        
        
        if not telefone:
            messages.error(request, 'Precisa de um Telefone')
            return render(request, 'inquilinos/add_inquilino.html')

        
        if not email:
            messages.error(request, 'Precisa de um email!')

        Inquilinos.objects.create(nome=nome, idadade=idade, sexo=sexo, telefone=telefone, email=email)
        messages.success(request, 'Inquilino salvo com Sucesso!')

        return redirect('inquilinos')
        





################### UNIDADES #########################



def unidades(request):
    unidades = Unidades.objects.all()
    paginator = Paginator(unidades, 5)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    context = {
        'unidades' : unidades,
        'page_obj' : page_obj
    }

    return render(request, 'unidades/unidades.html', context)

def add_unidade(request):
    unidades = Unidades.objects.all()
    context = {
        'values' : request.POST,
        'unidades' : unidades,
    }
    if request.method == 'GET':
        return render(request, 'unidades/add_unidade.html')

    if request.method == 'POST':
        identicacao = request.POST['identicacao'] 
        proprietario = request.POST['proprietario']
        condominio = request.POST['condominio'] 
        endereco = request.POST['endereco'] 

        if not identicacao:
            messages.error(request, 'Precisa de uma identicação!')
            return render(request, 'unidades/add_unidade.html')
        
        if not proprietario:
            messages.error(request, 'Precisa de um Proprietario!')
            return render(request, 'unidades/add_unidade.html')
        
        
        if not condominio:
            messages.error(request, 'Precisa de um condominio')
            return render(request, 'unidades/add_unidade.html')
        
        
        if not endereco:
            messages.error(request, 'Precisa de um Endereço')
            return render(request, 'unidades/add_unidade.html')

        Unidades.objects.create(identicacao=identicacao, proprietario=proprietario, condominio=condominio, endereco=endereco )
        messages.success(request, 'Unidade salva com Sucesso!')

        return redirect('unidades')
        
def deletar_unidade(request, id):
    unidades = Unidades.objects.get(pk=id)
    unidades.delete()
    messages.success(request, 'Unidade Excluída')
    return redirect('unidades')       


#DESPESAS


def despesas(request):
    despesas = Despesa.objects.all()
    paginator = Paginator(despesas, 5)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    myFilter = DespesaFilter(request.GET, queryset=despesas)
    despesas = myFilter.qs
    context = {
        'despesas': despesas,
        'page_obj': page_obj,
        'myFilter': myFilter,
    }
    return render(request, 'despesas/despesas.html', context)



def add_despesa(request):
    despesa = Despesa.objects.all()
    unidades = Unidades.objects.all()
    context = {
        'unidades': unidades,
        'values': request.POST,
        'despesa': despesa,
    }
    if request.method == 'GET':
        return render(request, 'despesas/add_despesa.html', context)

    if request.method == 'POST':
        valor = request.POST['valor']

        if not valor:
            messages.error(request, 'Valor é necessário!')
            return render(request, 'despesas/add_despesa', context)
        descricao = request.POST['descricao']
        tipo_despesa = request.POST['tipo_despesa']
        status_pagamento = request.POST['status_pagamento']
        vencimento_fatura = request.POST['vencimento_fatura']
        unidade = request.POST['unidade']

        if not descricao:
            messages.error(request, 'Descrição é necessario')
            return render(request, 'despesas/add_despesa', context)
        
        if not tipo_despesa:
            messages.error(request, 'Precisa de uma Categoria!')
            return render(request, 'despesas/add-despesa', context)

        Despesa.objects.create(valor=valor, descricao=descricao, status_pagamento=status_pagamento, vencimento_fatura=vencimento_fatura,
                               tipo_despesa=tipo_despesa, unidade=unidade )
        messages.success(request, 'Expense saved successfully')

        return redirect('despesas')

def editar_despesa(request, id):
    despesa = Despesa.objects.get(pk=id)
    unidades = Unidades.objects.all()
    context = {
        'despesa': despesa,
        'values': despesa,
        'unidades': unidades,

    }
    if request.method == 'GET':
        return render(request, 'despesas/edita_despesa.html', context)
    if request.method == 'POST':
        valor = request.POST['valor']

        if not valor:
            messages.error(request, 'Amount is required')
            return render(request, 'despesas/edita_despesa.html', context)

        descricao = request.POST['descricao']
        tipo_despesa = request.POST['tipo_despesa']
        status_pagamento = request.POST['status_pagamento']
        vencimento_fatura = request.POST['vencimento_fatura']


        if not descricao:
            messages.error(request, 'description is required')
            return render(request, 'despesas/edita_despesa.html', context)

        despesa.valor = valor
        despesa.vencimento_fatura = vencimento_fatura
        despesa.status_pagamento = status_pagamento
        despesa.tipo_despesa = tipo_despesa
        despesa.descricao = descricao

        despesa.save()
        messages.success(request, 'Despesa enviada com Sucesso!')

        return redirect('despesas')


        
def deleta_despesa(request, id):
    despesas = Despesa.objects.get(pk=id)
    despesas.delete()
    messages.success(request, 'Despesa Excluída')
    return redirect('despesas')     