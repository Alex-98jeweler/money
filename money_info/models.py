from django.db import models


class Status(models.Model):
    
    name = models.CharField(max_length=32, unique=True)
    
    class Meta:
        verbose_name_plural = 'Statuses'
    
    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=32, unique=True)
    
    def __str__(self):
        return self.name


class Category(models.Model):
    
    name = models.CharField(max_length=32, unique=True)
    type = models.ForeignKey(Type, on_delete=models.PROTECT)
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name
    


class SubCategory(models.Model):
    
    name = models.CharField(max_length=64, unique=True)
    category = models.ForeignKey(Category, models.PROTECT)
    
    class Meta:
        verbose_name_plural = 'Subcategories'
    
    def __str__(self):
        return self.name
