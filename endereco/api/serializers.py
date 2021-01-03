from rest_framework.serializers import ModelSerializer
from endereco.models import Endereco

class EnderecoSerializer(ModelSerializer):
    class Meta:
        model = Endereco
        fields = ['id','rua','bairro', 'numero', 'complemento', 
        'cidade', 'estado', 'latitude', 'longitude']