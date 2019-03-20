from django.shortcuts import render
from app.models import Vagas
from app.forms import BuscarVagas


def todas_vagas(request):
    vagas = Vagas.objects.all()

    contexto = {
        'vagas': vagas
    }
    
    return render(request, 'vagas.html', contexto)

