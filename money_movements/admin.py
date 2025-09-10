from django.contrib import admin

from . import models, forms


class MoneyMovementAdmin(admin.ModelAdmin):
    
    form = forms.MoneyMovementForm
    list_filter = ('status', 'type', 'category', 'subcategory')
    
admin.site.register(models.MoneyMovement, MoneyMovementAdmin)
    
