from django.db import models

# Create your models here.

class Turma(models.Model):
    nome = models.CharField(max_length = 100)
    ano_letivo = models.CharField(max_length=9)

    def __str__(self):
        return f"{self.nome} - {self.ano_letivo}"

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    especialidade = models.CharField(max_length=100, blank=True, null=True)
    turma = models.OneToOneField(Turma, on_delete = models.CASCADE, related_name = 'professor')

    def __str__(self):
        return self.nome

class Aluno(models.Model): 
    nome = models.CharField(max_length=100)
    numero = models.PositiveIntegerField(unique=True)
    data_nascimento = models.DateField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    turma = models.ForeignKey(Turma, on_delete = models.CASCADE, related_name = 'alunos')

    def __str__(self):
        return self.nome