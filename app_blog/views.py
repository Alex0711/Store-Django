from django.shortcuts import render, get_object_or_404
from .models import Category, Blog
# Create your views here.

def blog(request):
    posts= Blog.objects.all()
    categories=Category.objects.all()
    return render(request, "app_blog/blog.html", {
        'posts':posts,
        'categories':categories
    })

def category(request, category_id):
    categories=Category.objects.all()

    category= get_object_or_404(Category, pk=category_id)
    #posts= category.blog_set.all() Cualquiera de los dos funciona
    posts= Blog.objects.filter(categories=category)
    return render(request, "app_blog/category.html", {
        'posts':posts,
        'categories':categories
    })