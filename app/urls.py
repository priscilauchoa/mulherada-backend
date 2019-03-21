from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobrenos', views.sobrenos, name='sobrenos'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('login', views.login, name='login'),
    path('avaliacao', views.avaliacao, name='avaliacao'),
    path('curriculo', views.curriculo, name='curriculo'),
    path('lista-vagas', views.lista_vagas, name='lista-vagas'),
    path('descricao-vaga/<id>', views.descricao_vaga, name='descricao-vaga'),
]
