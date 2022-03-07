from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField(max_length=100, required=True)
    country=forms.CharField(label='Country', max_length=100, required=True)
    state=forms.CharField(label='State', max_length=100, required=True)
    city=forms.CharField(label='City', max_length=100, required=True)
    street=forms.CharField(label='Street', max_length=100, required=True)
    password1=forms.CharField(label='Password', widget=forms.PasswordInput)
    password2=forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User #para relacionarlo con la tabla de usuarios y poder registrarlos
        fields = ['username', 'email', 'country', 'state', 'city', 'street', 'email', 'password1', 'password2']
        help_texts= {k:"" for k in fields }  #reemplazo todos los textos de ayuda por strings vacíos 

    def clean_email(self): 
        email = self.cleaned_data.get('email') 
        username = self.cleaned_data.get('username') 
        if email and User.objects.filter(email=email).exclude(username=username).count(): 
            raise forms.ValidationError(u'Email addresses must be unique.') 
        return email

