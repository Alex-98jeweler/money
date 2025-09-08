from rest_framework import viewsets, pagination

from . import models, serializers



class TypeAPIViewSet(viewsets.ModelViewSet):
    
    model = models.Type
    serializer_class = serializers.TypeSerializer
    pagination_class = pagination.PageNumberPagination
    queryset = models.Type.objects.all()
    
    
class StatusAPIViewSet(viewsets.ModelViewSet):
    
    model = models.Status
    serializer_class = serializers.StatusSerializer
    pagination_class = pagination.PageNumberPagination
    queryset = models.Status.objects.all()


class CategoryAPIViewSet(viewsets.ModelViewSet):
    
    model = models.Category
    serializer_class = serializers.CategorySerializer
    pagination_class = pagination.PageNumberPagination
    queryset = models.Category.objects.all()
    
    
class SubCategoryAPIViewSet(viewsets.ModelViewSet):
    
    model = models.SubCategory
    serializer_class = serializers.SubCategorySerializer
    pagination_class = pagination.PageNumberPagination
    queryset = models.SubCategory.objects.all()
