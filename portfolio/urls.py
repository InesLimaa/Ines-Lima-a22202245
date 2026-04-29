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
    
    path('projetos/', views.ProjetoListView.as_view(), name='projetos'),
    path('projeto/<int:id>/', views.projeto_detail, name='projeto_detail'),
    path('projetos/create/', views.ProjetoCreateView.as_view(), name='projeto_create'),
    path('projetos/<int:pk>/update/', views.ProjetoUpdateView.as_view(), name='projeto_update'),
    path('projetos/<int:pk>/delete/', views.ProjetoDeleteView.as_view(), name='projeto_delete'),
    
    path('makingof/', views.makingof_view, name='makingof'),
    path('makingof/<int:id>/', views.makingof_detail, name='makingof_detail'),
    
    path('tecnologias/<int:id>/', views.tecnologia_detail, name='tecnologia_detail'),
    path('tecnologias/create/', views.TecnologiaCreateView.as_view(), name='tecnologia_create'),
    path('tecnologias/<int:pk>/delete/', views.TecnologiaDeleteView.as_view(), name='tecnologia_delete'),  
    path('tecnologias/<int:pk>/update/', views.TecnologiaUpdateView.as_view(), name='tecnologia_update'),

    path('competencias/<int:id>/', views.competencia_detail, name='competencia_detail'),
    path('competencias/create/', views.CompetenciaCreateView.as_view(), name='competencia_create'),
    path('competencias/<int:pk>/delete/', views.CompetenciaDeleteView.as_view(), name='competencia_delete'),  
    path('competencias/<int:pk>/update/', views.CompetenciaUpdateView.as_view(), name='competencia_update'),
]