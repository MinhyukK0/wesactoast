from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length= 30)

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'menu'

class Products(models.Model):
    kr_name = models.CharField(max_length=30)
    en_name = models.CharField(max_length=30)
    information = models.TextField(default = '')
    ingredients = models.ManyToManyField('Ingredients', related_name='product_ingredient')
    menu = models.ForeignKey(Menu, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.kr_name
    class Meta:
        db_table = 'products'

class Images(models.Model):
    url = models.TextField(default='')
    product = models.ForeignKey(Products, on_delete = models.CASCADE)
    
    class Meta:
        db_table = 'images'

class Ingredients(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'ingredients'
