from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio_index, name='portfolio_index'),
    path('licenciaturas/', views.licenciaturas_view, name='licenciaturas'),
    path('licenciatura/<int:id>/', views.licenciatura_detail, name='licenciatura_detail'),
    path('perfis/', views.perfis_view, name='perfis'),
    path('perfil/<int:id>/', views.perfil_detail, name='perfil_detail'),
    path('unidades-curriculares/', views.unidades_curriculares_view, name='unidades_curriculares'),
    path('unidade-curricular/<int:id>/', views.unidade_curricular_detail, name='unidade_curricular_detail'),
    path('tecnologias/', views.tecnologias_view, name='tecnologias'),
    path('tecnologia/<int:id>/', views.tecnologia_detail, name='tecnologia_detail'),
    path('competencias/', views.competencias_view, name='competencias'),
    path('competencia/<int:id>/', views.competencia_detail, name='competencia_detail'),
    path('formacoes/', views.formacoes_view, name='formacoes'),
    path('formacao/<int:id>/', views.formacao_detail, name='formacao_detail'),
    path('tfcs/', views.tfcs_view, name='tfcs'),
    path('tfc/<int:id>/', views.tfc_detail, name='tfc_detail'),
    path('projetos/', views.projetos_view, name='projetos'),
    path('projeto/<int:id>/', views.projeto_detail, name='projeto_detail'),
    path('makingof/', views.makingof_view, name='makingof'),
    path('makingof/<int:id>/', views.makingof_detail, name='makingof_detail'),
]