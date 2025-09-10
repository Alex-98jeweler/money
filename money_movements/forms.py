from django import forms
from django.core.exceptions import ValidationError

from . import models
from money_info import models as info_models


class MoneyMovementForm(forms.ModelForm):
    
    class Meta:
        model = models.MoneyMovement
        fields = '__all__'
        
        
    def clean_category(self):
        type_id = self.data.get('type')
        category_id = self.data.get('category')
        try:
            category = info_models.Category.objects.get(pk=category_id, type_id=type_id)
        except info_models.Category.DoesNotExist:
            raise ValidationError('Category is not child passed Type')
        return category
    
    def clean_subcategory(self):
        category_id = self.data.get('category')
        subcategory_id = self.data.get('subcategory')
        try:
            category = info_models.SubCategory.objects.get(pk=subcategory_id, category_id=category_id)
        except info_models.SubCategory.DoesNotExist:
            raise ValidationError('Subcategory is not child passed Category')
        return category
