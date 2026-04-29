from django import forms
from .models import Competencia, Projeto, Tecnologia

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['titulo', 'descricao', 'imagem', 'github_url', 'perfil', 'unidade_curricular', 'tecnologias', 'competencias']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4}),
            'tecnologias': forms.CheckboxSelectMultiple(),
            'competencias': forms.CheckboxSelectMultiple(),
        }

class TecnologiaForm(forms.ModelForm):
    class Meta:
        model = Tecnologia
        fields = ['nome', 'logo', 'link', 'interesse', 'tipo']
        widgets = {
            'interesse': forms.NumberInput(attrs={'min': 1, 'max': 5}),
        }

class CompetenciaForm(forms.ModelForm):
    class Meta:
        model = Competencia
        fields = ['nome', 'descricao', 'nivel', 'evidencia', 'perfil', 'tecnologias']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4}),
            'nivel': forms.Select(choices=[(1, 'Básico'), (2, 'Intermediário'), (3, 'Avançado')]),
            'tecnologias': forms.CheckboxSelectMultiple(),
        }