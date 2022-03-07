from django.urls import path

from . import views
from app_products import urls

app_name = "shopping_cart"
urlpatterns = [
    path('add/<int:product_id>/', views.add_product, name='add'),
    path('deletes/<int:product_id>/', views.deletes, name='deletes'),
    path('delete/<int:product_id>/', views.delete, name='delete'),
    path('clean/', views.clean, name='clean'),
]
