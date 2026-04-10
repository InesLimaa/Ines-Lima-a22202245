from django.db import models


class Licenciatura(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=20)
    instituicao = models.CharField(max_length=100)
    duracao_anos = models.IntegerField()
    ano_inicio = models.IntegerField()
    plano_estudo_url = models.URLField(blank=True, null=True)

    # NOVOS CAMPOS (API)
    codigo = models.IntegerField(blank=True, null=True)
    grau = models.CharField(max_length=50, blank=True, null=True)
    unidade_organica = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nome


# Perfil
class Perfil(models.Model):
    nome = models.CharField(max_length=100)
    fotografia = models.ImageField(upload_to='perfil/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    email = models.EmailField()
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    cv_pdf = models.FileField(upload_to='cv/', blank=True, null=True)

    licenciatura = models.OneToOneField(
        Licenciatura,
        on_delete=models.CASCADE,
        related_name='perfil'
    )

    def __str__(self):
        return self.nome


class UnidadeCurricular(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=50, blank=True, null=True)
    ano_curricular = models.IntegerField()
    semestre = models.IntegerField()
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='ucs/', blank=True, null=True)
    ects = models.IntegerField()

    # NOVOS CAMPOS (API)
    apresentacao = models.TextField(blank=True, null=True)
    objetivos = models.TextField(blank=True, null=True)
    programa = models.TextField(blank=True, null=True)
    bibliografia = models.TextField(blank=True, null=True)

    licenciatura = models.ForeignKey(
        Licenciatura,
        on_delete=models.CASCADE,
        related_name='ucs'
    )

    def __str__(self):
        return self.nome


# Tecnologia
class Tecnologia(models.Model):
    nome = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='tecnologias/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    interesse = models.IntegerField()
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


# Competência
class Competencia(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    nivel = models.CharField(max_length=50)
    evidencia = models.TextField(blank=True, null=True)

    perfil = models.ForeignKey(
        Perfil,
        on_delete=models.CASCADE,
        related_name='competencias'
    )

    tecnologias = models.ManyToManyField(
        Tecnologia,
        related_name='competencias',
        blank=True
    )

    def __str__(self):
        return self.nome


# Formação
class Formacao(models.Model):
    titulo = models.CharField(max_length=100)
    entidade = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    data_inicio = models.DateField()
    data_fim = models.DateField(blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    concluida = models.BooleanField(default=False)

    competencias = models.ManyToManyField(
        Competencia,
        related_name='formacoes',
        blank=True
    )

    tecnologias = models.ManyToManyField(
        Tecnologia,
        related_name='formacoes',
        blank=True
    )

    def __str__(self):
        return self.titulo


# TFC
class TFC(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    ano = models.IntegerField()
    resumo = models.TextField(blank=True, null=True)
    interesse = models.IntegerField()

    tecnologias = models.ManyToManyField(
        Tecnologia,
        related_name='tfcs',
        blank=True
    )

    def __str__(self):
        return self.titulo


# Projeto
class Projeto(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='projetos/', blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)

    perfil = models.ForeignKey(
        Perfil,
        on_delete=models.CASCADE,
        related_name='projetos'
    )

    unidade_curricular = models.ForeignKey(
        UnidadeCurricular,
        on_delete=models.CASCADE,
        related_name='projetos'
    )

    tecnologias = models.ManyToManyField(
        Tecnologia,
        related_name='projetos',
        blank=True
    )

    competencias = models.ManyToManyField(
        Competencia,
        related_name='projetos',
        blank=True
    )

    def __str__(self):
        return self.titulo


# Making Of
class MakingOf(models.Model):
    titulo = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='makingof/', blank=True, null=True)
    descricao = models.TextField()
    modificacoes = models.TextField()


    def __str__(self):
        return self.titulo