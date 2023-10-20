from django.shortcuts import render

from .forms import ContatoForm, ProdutoModelForm
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def contato(request):
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_email()
            messages.success(request, 'Enviado com sucesso!')
            form = ContatoForm()
        else:
            messages.error(request, 'Mensagem não enviada.')

    context = {
        "form": form,
    }

    return render(request, 'contato.html', context=context)

def produto(request):
    if str(request.method) == 'POST':
        form = ProdutoModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto salvo com sucesso.')
            form = ProdutoModelForm()
        else:
            messages.error(request, 'Erro ao salvar o produto.')
    else:
        form = ProdutoModelForm()
    
    context = {
        "form": form,
    }

    return render(request, 'produto.html', context=context)