from django.urls import path

from . import views

app_name = "app_blog"
urlpatterns = [
    path('', views.blog, name='Blog'),
    path('category/<int:category_id>', views.category, name='Category')
]