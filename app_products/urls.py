from django.urls import path

from . import views

app_name = "app_products"
urlpatterns = [
    path('', views.store, name='Store'),
]