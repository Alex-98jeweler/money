from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from . import models, serializers



class TypeAPIViewSet(viewsets.ModelViewSet):
    
    model = models.Type
    serializer_class = serializers.TypeSerializer
    queryset = models.Type.objects.all()
    
    
class StatusAPIViewSet(viewsets.ModelViewSet):
    
    model = models.Status
    serializer_class = serializers.StatusSerializer
    queryset = models.Status.objects.all()


class CategoryAPIViewSet(viewsets.ModelViewSet):
    
    model = models.Category
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['type']
    http_method_names = ['get', 'post', 'put', 'delete']
    
    
class SubCategoryAPIViewSet(viewsets.ModelViewSet):
    
    model = models.SubCategory
    serializer_class = serializers.SubCategorySerializer
    queryset = models.SubCategory.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']
    http_method_names = ['get', 'post', 'put', 'delete']
