from django import forms
from .models import Projeto

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['titulo', 'descricao', 'imagem', 'github_url', 'perfil', 'unidade_curricular', 'tecnologias', 'competencias']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4}),
            'tecnologias': forms.CheckboxSelectMultiple(),
            'competencias': forms.CheckboxSelectMultiple(),
        }