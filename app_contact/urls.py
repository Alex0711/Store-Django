from django.urls import path

from . import views

app_name = "app_contact"
urlpatterns = [
    path('', views.contact, name='Contact'),
    path('thanks/', views.contact, name='Thanks'),
]