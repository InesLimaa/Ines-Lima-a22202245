from django.db import models


class PersonalTrainer(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True, blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    especialidade = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return self.nome


class Membro(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nome


class SessaoTreino(models.Model):
    pt = models.ForeignKey(
        PersonalTrainer,
        on_delete=models.CASCADE,
        related_name='sessoes'
    )
    membro = models.ForeignKey(
        Membro,
        on_delete=models.CASCADE,
        related_name='sessoes'
    )
    data = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f"{self.membro.nome} marcou sessão para o dia {self.data}, às {self.hora} com o PT: {self.pt.nome}"