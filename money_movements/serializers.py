from rest_framework import serializers, exceptions

from . import models


class MoneyMovementsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.MoneyMovement
        fields = '__all__'
        
    def validate_category(self, value):
        type_id = int(self.initial_data.get('type'))
        if value.type_id != type_id:
            raise exceptions.ValidationError('Is not child of Type instance')
        return value
    
    def validate_subcategory(self, value):
        category_id = int(self.initial_data.get('category'))
        if value.category_id != category_id:
            raise exceptions.ValidationError('Is not child of Category instance')
        return value