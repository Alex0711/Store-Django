from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.

def contact(request):
    if request.method=='POST':
        myform = ContactForm(request.POST)

        if myform.is_valid():
            name=request.POST.get('name')
            email=request.POST.get('email')
            message=request.POST.get('message')
            
            email=EmailMessage(
                "Mensaje desde la app Django - Store",
                f"El usuuario {name}, con la dirección de correo {email}, dice lo siguiente: \n\n {message}",
                "", #No entiendo por qué este queda vacío. Creo que es porque puedo configurar más de un email para enviar correos
                ['alex.senger@hotmail.com'],
                reply_to=[email]
            )

            try:
                email.send()
                return redirect('/app_contact/?enviado')

            except:
                return redirect('/app_contact/?error')

    else:
        myform = ContactForm()
        return render(request, 'app_contact/contact.html', {
            'myform':myform,
        })
