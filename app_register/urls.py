from django.urls import path

from . import views

app_name = "app_register"
urlpatterns = [
    path('', views.register, name='Register'),
]
