from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from django.http import HttpResponse
from django.http import JsonResponse
from django.views import View

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all() #take all product from the database
    serializer_class = ProductSerializer #which serializer to convert in json and vice versa
def home(request):
    return HttpResponse("Welcome to the Product API! type this to go to api page:http://127.0.0.1:8000/api/products/")
class ProductListView(View):
    def get(self, request):
        products = list(Product.objects.values('name', 'price', 'description'))  # Mod
        return JsonResponse(products, safe=False)
