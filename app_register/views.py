from django.shortcuts import render, redirect
from django.contrib import messages

from .models import *
from .forms import *

# Create your views here.
def register(request): 
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() #acá guardo el usuario

            #Envío el mensaje de que se creó el usuario
            username=form.cleaned_data['username']
            messages.success(request, f'User {username} created')

            #Agrego los campos de la dirección
            email=form.cleaned_data['email']
            country=form.cleaned_data['country']
            city=form.cleaned_data['city']
            street=form.cleaned_data['street']

            user=Profile.objects.get(email=email)
            user.country=country
            user.city=city
            user.street=street
            user.save()

            return redirect('app_store:Home')
    
    else:
        form=(UserRegisterForm)
    
    context = {'form':form}
    return render(request, 'app_register/register.html', context)