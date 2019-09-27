from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from patients.models import Patient
from .serializers import PatientSerializer


class PatientViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = PatientSerializer
    filter_backends = [SearchFilter]
    search_fields = ['id']

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        queryset = Patient.objects.all()
        if id:
            queryset = Patient.objects.filter(pk=id)
        return queryset

    # def list(self, request, *args, **kwargs):
    #     return Response({"title": 123})

    # def create(self, request, *args, **kwargs):
    #     return Response({'Hello': request.data['name']})

    # def destroy(self, request, *args, **kwargs):
    #     pass

    # def retrieve(self, request, *args, **kwargs):
    #     pass

    # def update(self, request, *args, **kwargs):
    #     pass

    # def partial_update(self, request, *args, **kwargs):
    #     pass

    # @action(methods=['get'], detail=True)
    # def alert(self, request, pk=None):
    #     pass
