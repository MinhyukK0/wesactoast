import json
from django.http import JsonResponse
from django.views import View
from django.shortcuts import render
from products.models import Menu, Product, Image, Ingredient

# Create your views here.
class ProductView(View):
    def get(self, request):
        products = Product.objects.all()
        results = []
        for product in products:
            results.append(
                {
                    'Menu' : product.menu.name ,
                    'Name' : product.kr_name ,
                    'Information' : product.information,
                    'Image' : list(map(lambda x: x.url, product.image_set.all()))[0] ,
                    'Ingredient' : list(map(lambda x: x.name, product.ingredient.all())),
                }
                )
        return JsonResponse({"results": results}, status = 200)