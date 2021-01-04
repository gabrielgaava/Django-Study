from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from ponto_turistico.models import PontoTuristico
from atracoes.api.serializers import AtracaoSerializer
from endereco.api.serializers import EnderecoSerializer

class PontoTuristicoSerializer(ModelSerializer):

    # Adicionar objeto completo no retorno de outras entidades
    atracoes = AtracaoSerializer(many=True)
    endereco = EnderecoSerializer()

    # Adicionando atributo "adicional" no retorno
    custom_prop = SerializerMethodField()
    
    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'custom_prop', 'descricao2', 'atracoes', 'endereco', 'aprovado', 'foto')
        
    # Função de retorno do campo costumizado
    def get_custom_prop(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)