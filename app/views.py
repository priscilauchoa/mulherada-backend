from django.shortcuts import render
from django.http import JsonResponse
from app.models import Vagas

def index(request):
    return render(request, 'index.html')

def sobrenos(request):
    return render(request, 'sobrenos.html')

def cadastro(request):
    return render(request, 'cadastro-usuario.html')

def login(request):
    return render(request, 'login.html')

def avaliacao(request):
    return render(request, 'avaliacao.html')

def curriculo(request):
    return render(request, 'curriculo.html')


def lista_vagas(request):

    cargo = request.POST.get("cargo", "")
    localidade = request.POST.get("localidade", "")
    vagas = Vagas.objects.filter(titulo__contains=cargo, cidade__contains=localidade)

    contexto = {
        'localidade': localidade,
        'vagas': vagas
    }

    return render(request, 'lista-vagas.html', contexto)

def descricao_vaga(request, id):

    vaga = Vagas.objects.filter(id=id).first()

    contexto = {
        'vaga': vaga
    }

    print(contexto)
    return render(request, 'descricao-vaga.html', contexto)

    
