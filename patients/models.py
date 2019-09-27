from django.db import models


class Patient(models.Model):
    id = models.BigIntegerField(primary_key=True, verbose_name='Código Identificador')
    name = models.CharField(max_length=30, verbose_name='Nome do Cliente')
    birth_date = models.DateField(verbose_name='Data de Nascimento')
    collection_date = models.DateField(verbose_name='Data de Coleta')
    delivery_date = models.DateField(verbose_name='Data de Entrega')
    doctor_name = models.CharField(max_length=30, verbose_name='Nome do Médico')
    submission_date = models.DateTimeField(auto_now_add=True, verbose_name='Data da Submissão')
    update_date = models.DateTimeField(auto_now=True, verbose_name='Data da Última Alteração')

    def __str__(self):
        return self.name
