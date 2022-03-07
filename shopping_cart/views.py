from nturl2path import url2pathname
from django.shortcuts import render, redirect

from .cart import Cart
from app_products.models import Product

# Create your views here.

def add_product(request, product_id):
    cart=Cart(request)
    product=Product.objects.get(id=product_id)
    cart.add_to_cart(product=product)
    return redirect('app_products:Store')

def deletes(request, product_id):
    cart=Cart(request)
    product=Product.objects.get(id=product_id)
    cart.delete_products(product=product)
    return redirect('app_products:Store')

def delete(request, product_id):
    cart=Cart(request)
    product=Product.objects.get(id=product_id)
    cart.delete_a_product(product=product)
    return redirect('app_products:Store') 

def clean(request):
    cart=Cart(request)
    cart.clean_cart()
    return redirect('app_products:Store')