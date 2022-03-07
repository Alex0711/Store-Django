from django.shortcuts import render
from .models import Service

# Create your views here.

def services(request):
    services=Service.objects.all()
    return render(request, "app_services/services.html", {
        'services':services,
    })