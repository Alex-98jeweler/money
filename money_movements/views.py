from rest_framework import generics
from drf_yasg.utils import swagger_auto_schema

from money_movements import serializers, models, method_params
from money_movements.services import sql_conditions


class MoneyMovementsCreateListView(generics.ListCreateAPIView):
    
    serializer_class = serializers.MoneyMovementsSerializer
    
    @swagger_auto_schema(manual_parameters=method_params.LIST_PARAMS)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    def get_queryset(self):
        q = sql_conditions.prepare_money_movements_conditions(self.request.GET)
        if q:
            queryset = models.MoneyMovement.objects.filter(q)
        else:
            queryset = models.MoneyMovement.objects.all()
        return queryset
    

class MoneyMoveRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    
    serializer_class = serializers.MoneyMovementsSerializer
    http_method_names = ['get', 'put', 'delete']
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return models.MoneyMovement.objects.filter(pk=pk)

