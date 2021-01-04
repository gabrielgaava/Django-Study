from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from ponto_turistico.models import PontoTuristico
from .serializers import PontoTuristicoSerializer

class PontoTuristicoViewSet(ModelViewSet):

    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):

        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        queryset = PontoTuristico.objects.all()

        # Modifica a URL seletora, por exemplo:
        # ../api/ponto-turistico/nome/
        # lookup_field = 'nome'

        if id:
            queryset = PontoTuristico.objects.filter(pk = id)

        if nome: 
            queryset = queryset.filter(nome__iexact = nome)

        return queryset
    
    # Altera a Listagem padrão do Rest Framework (GET Geral)
    # def list(self, request, *args, **kwargs):

    # Altera o comportamento de criação (POST)
    # def create(self, request, *args, **kwargs):
    #    print(request.data['nome'])
    #    return Response({'message': "Ponto turistico criado"})

    # Altera o comportamento de destruição (DELETE)    
    # def destroy(self, request, *args, **kwargs):
        super(PontoTuristicoViewSet, self).destroy(self, request, *args, **kwargs)
        return Response(
            {
                'ponto-deletado': kwargs['pk'],
                'message': 'Testando'
            }
        )

    # Altera o comportamento de exibição (GET Unico)
    # def retrieve(self, request, *args, **kwargs):

    # Altera o comportamento de atualização (UPDATE)
    # def update(self, request, *args, **kwargs):

    # Altera o comportamento do (PATCH)
    # def partial_update(self, request, *args, **kwargs):

    # Actions Personalizadas
    # Detail retorna a Primary Key (ponto-turistico/id/denunciar)
    @action(methods=['get'], detail=True)
    def denunciar(self, request, pk=None):
        return Response({'message': 'Denuncia feita'})

    # (ponto-turistico/aprovados)
    @action(methods=['get'], detail=False)
    def aprovados(self, request):
        return super(PontoTuristicoViewSet, self).list(self, request)