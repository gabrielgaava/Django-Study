from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from atracoes.models import Atracao
from .serializers import AtracaoSerializer

class AtracoesViewSet(ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
    

    # Permissões
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )

    # Adiciona possibilidade de filtrar itens na página da Response
    # filter_backends = (DjangoFilterBackend, )
    # filter_fields = ('nome', 'descricao')

    # Adicionando busca no endpoint
    filter_backends = (SearchFilter, )
    search_fields = ('nome', 'descricao', '=idade_minima')
