from django.urls import path

from . import views
from .views import Login_View, Logout_View

app_name = "app_store"
urlpatterns = [
    path('', Login_View.as_view(), name='Home'),
    path('logout/', Logout_View.as_view(), name='Logout'),
]