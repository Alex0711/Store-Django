from django.shortcuts import render
from .models import Product, ProductCategory

# Create your views here.

def store(request):
    products=Product.objects.all()
    return render(request, "app_products/store.html", {
        'products':products,
    })