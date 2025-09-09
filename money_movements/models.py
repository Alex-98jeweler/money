from django.db import models


class MoneyMovement(models.Model):
    
    date_time = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    status = models.ForeignKey('money_info.Status', models.SET_NULL, null=True)
    type = models.ForeignKey('money_info.Type', models.CASCADE)
    category = models.ForeignKey('money_info.Category', models.CASCADE)
    subcategory = models.ForeignKey('money_info.SubCategory', models.CASCADE)
    comment = models.TextField(max_length=1024)
