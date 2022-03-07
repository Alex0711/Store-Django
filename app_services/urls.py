from django.urls import path
from . import views

app_name = "app_services"
urlpatterns = [
    path('', views.services, name='Services'),
]
