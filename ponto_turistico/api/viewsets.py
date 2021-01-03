from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from ponto_turistico.models import PontoTuristico
from .serializers import PontoTuristicoSerializer

class PontoTuristicoViewSet(ModelViewSet):

    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        return PontoTuristico.objects.all()
    
    # Altera a Listagem padrão do Rest Framework (GET Geral)
    # def list(self, request, *args, **kwargs):

    # Altera o comportamento de criação (POST)
    # def create(self, request, *args, **kwargs):
    #    print(request.data['nome'])
    #    return Response({'message': "Ponto turistico criado"})

    # Altera o comportamento de destruição (DELETE)    
    def destroy(self, request, *args, **kwargs):
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