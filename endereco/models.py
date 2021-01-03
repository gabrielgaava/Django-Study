from django.db import models

# Create your models here.
class Endereco(models.Model):
    rua = models.CharField(max_length=255)
    bairro = models.CharField(max_length=60)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=100, null=True, blank=True)
    cidade = models.CharField(max_length=60)
    estado = models.CharField(max_length=60)
    latitude = models.IntegerField(null=True, blank=True)
    longitude = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.rua 