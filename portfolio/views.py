from django.shortcuts import render, get_object_or_404
from .models import (
    Licenciatura,
    Perfil,
    UnidadeCurricular,
    Tecnologia,
    Competencia,
    Formacao,
    TFC,
    Projeto,
    MakingOf,
)


def portfolio_index(request):
    pages = [
        {'title': 'Licenciaturas', 'url': 'licenciaturas'},
        {'title': 'Perfis', 'url': 'perfis'},
        {'title': 'Unidades Curriculares', 'url': 'unidades_curriculares'},
        {'title': 'Tecnologias', 'url': 'tecnologias'},
        {'title': 'Competências', 'url': 'competencias'},
        {'title': 'Formações', 'url': 'formacoes'},
        {'title': 'TFCs', 'url': 'tfcs'},
        {'title': 'Projetos', 'url': 'projetos'},
        {'title': 'Making Of', 'url': 'makingof'},
    ]
    return render(request, 'portfolio/index.html', {'pages': pages})


def licenciaturas_view(request):
    licenciaturas = Licenciatura.objects.all()
    return render(request, 'portfolio/licenciaturas_list.html', {'licenciaturas': licenciaturas})


def perfis_view(request):
    perfis = Perfil.objects.select_related('licenciatura').all()
    return render(request, 'portfolio/perfis_list.html', {'perfis': perfis})


def unidades_curriculares_view(request):
    unidades = UnidadeCurricular.objects.select_related('licenciatura').all()
    return render(request, 'portfolio/unidades_curriculares_list.html', {'unidades': unidades})


def tecnologias_view(request):
    tecnologias = Tecnologia.objects.all()
    return render(request, 'portfolio/tecnologias_list.html', {'tecnologias': tecnologias})


def competencias_view(request):
    competencias = Competencia.objects.select_related('perfil').prefetch_related('tecnologias').all()
    return render(request, 'portfolio/competencias_list.html', {'competencias': competencias})


def formacoes_view(request):
    formacoes = Formacao.objects.all()
    return render(request, 'portfolio/formacoes_list.html', {'formacoes': formacoes})


def tfcs_view(request):
    tfcs = TFC.objects.prefetch_related('tecnologias').all()
    return render(request, 'portfolio/tfcs_list.html', {'tfcs': tfcs})


def projetos_view(request):
    projetos = Projeto.objects.select_related('perfil', 'unidade_curricular').prefetch_related('tecnologias').all()
    return render(request, 'portfolio/projetos_list.html', {'projetos': projetos})


def makingof_view(request):
    makingofs = MakingOf.objects.all()
    return render(request, 'portfolio/makingof_list.html', {'makingofs': makingofs})


# Detalhes individuais

def licenciatura_detail(request, id):
    obj = get_object_or_404(Licenciatura, id=id)
    fields = [
        {'label': 'Nome', 'value': obj.nome},
        {'label': 'Sigla', 'value': obj.sigla},
        {'label': 'Instituição', 'value': obj.instituicao},
        {'label': 'Duração (anos)', 'value': obj.duracao_anos},
        {'label': 'Ano Início', 'value': obj.ano_inicio},
        {'label': 'Plano de Estudo', 'value': obj.plano_estudo_url},
        {'label': 'Código', 'value': obj.codigo},
        {'label': 'Grau', 'value': obj.grau},
        {'label': 'Unidade Orgânica', 'value': obj.unidade_organica},
    ]
    related = {
        'Unidades Curriculares': obj.ucs.all(),
        'Perfis': [obj.perfil] if hasattr(obj, 'perfil') else [],
    }
    return render(request, 'portfolio/detail.html', {'object': obj, 'fields': fields, 'related': related})


def perfil_detail(request, id):
    obj = get_object_or_404(Perfil, id=id)
    fields = [
        {'label': 'Nome', 'value': obj.nome},
        {'label': 'Email', 'value': obj.email},
        {'label': 'Bio', 'value': obj.bio},
        {'label': 'LinkedIn', 'value': obj.linkedin},
        {'label': 'GitHub', 'value': obj.github},
        {'label': 'Licenciatura', 'value': str(obj.licenciatura)},
    ]
    related = {
        'Competências': obj.competencias.all(),
        'Projetos': obj.projetos.all(),
    }
    return render(request, 'portfolio/detail.html', {'object': obj, 'fields': fields, 'related': related})


def unidade_curricular_detail(request, id):
    obj = get_object_or_404(UnidadeCurricular, id=id)
    fields = [
        {'label': 'Nome', 'value': obj.nome},
        {'label': 'Ano Curricular', 'value': obj.ano_curricular},
        {'label': 'Semestre', 'value': obj.semestre},
        {'label': 'ECTS', 'value': obj.ects},
        {'label': 'Apresentação', 'value': obj.apresentacao},
        {'label': 'Objetivos', 'value': obj.objetivos},
        {'label': 'Programa', 'value': obj.programa},
        {'label': 'Bibliografia', 'value': obj.bibliografia},
        {'label': 'Licenciatura', 'value': str(obj.licenciatura)},
    ]
    related = {
        'Projetos': obj.projetos.all(),
    }
    return render(request, 'portfolio/detail.html', {'object': obj, 'fields': fields, 'related': related})


def tecnologia_detail(request, id):
    obj = get_object_or_404(Tecnologia, id=id)
    fields = [
        {'label': 'Nome', 'value': obj.nome},
        {'label': 'Tipo', 'value': obj.tipo},
        {'label': 'Interesse', 'value': obj.interesse},
        {'label': 'Link', 'value': obj.link},
    ]
    related = {
        'Competências': obj.competencias.all(),
        'Formações': obj.formacoes.all(),
        'TFCs': obj.tfcs.all(),
        'Projetos': obj.projetos.all(),
    }
    return render(request, 'portfolio/detail.html', {'object': obj, 'fields': fields, 'related': related})


def competencia_detail(request, id):
    obj = get_object_or_404(Competencia, id=id)
    fields = [
        {'label': 'Nome', 'value': obj.nome},
        {'label': 'Descrição', 'value': obj.descricao},
        {'label': 'Nível', 'value': obj.nivel},
        {'label': 'Evidência', 'value': obj.evidencia},
        {'label': 'Perfil', 'value': str(obj.perfil)},
    ]
    related = {
        'Tecnologias': obj.tecnologias.all(),
        'Formações': obj.formacoes.all(),
        'Projetos': obj.projetos.all(),
    }
    return render(request, 'portfolio/detail.html', {'object': obj, 'fields': fields, 'related': related})


def formacao_detail(request, id):
    obj = get_object_or_404(Formacao, id=id)
    fields = [
        {'label': 'Título', 'value': obj.titulo},
        {'label': 'Entidade', 'value': obj.entidade},
        {'label': 'Tipo', 'value': obj.tipo},
        {'label': 'Data Início', 'value': obj.data_inicio},
        {'label': 'Data Fim', 'value': obj.data_fim},
        {'label': 'Descrição', 'value': obj.descricao},
        {'label': 'Concluída', 'value': 'Sim' if obj.concluida else 'Não'},
    ]
    related = {
        'Competências': obj.competencias.all(),
        'Tecnologias': obj.tecnologias.all(),
    }
    return render(request, 'portfolio/detail.html', {'object': obj, 'fields': fields, 'related': related})


def tfc_detail(request, id):
    obj = get_object_or_404(TFC, id=id)
    fields = [
        {'label': 'Título', 'value': obj.titulo},
        {'label': 'Autor', 'value': obj.autor},
        {'label': 'Ano', 'value': obj.ano},
        {'label': 'Resumo', 'value': obj.resumo},
        {'label': 'Interesse', 'value': obj.interesse},
    ]
    related = {
        'Tecnologias': obj.tecnologias.all(),
    }
    return render(request, 'portfolio/detail.html', {'object': obj, 'fields': fields, 'related': related})


def projeto_detail(request, id):
    obj = get_object_or_404(Projeto, id=id)
    fields = [
        {'label': 'Título', 'value': obj.titulo},
        {'label': 'Descrição', 'value': obj.descricao},
        {'label': 'GitHub URL', 'value': obj.github_url},
        {'label': 'Perfil', 'value': str(obj.perfil)},
        {'label': 'Unidade Curricular', 'value': str(obj.unidade_curricular)},
    ]
    related = {
        'Tecnologias': obj.tecnologias.all(),
        'Competências': obj.competencias.all(),
    }
    return render(request, 'portfolio/detail.html', {'object': obj, 'fields': fields, 'related': related})


def makingof_detail(request, id):
    obj = get_object_or_404(MakingOf, id=id)
    fields = [
        {'label': 'Título', 'value': obj.titulo},
        {'label': 'Descrição', 'value': obj.descricao},
        {'label': 'Modificações', 'value': obj.modificacoes},
    ]
    related = {}
    return render(request, 'portfolio/detail.html', {'object': obj, 'fields': fields, 'related': related})
