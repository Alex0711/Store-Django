from django import forms

class ContactForm(forms.Form):

    name=forms.CharField(label= 'Name', max_length=20)
    email=forms.EmailField(label= 'Your Email', max_length=50)
    message=forms.CharField(label= 'Messaje', max_length=500, widget=forms.Textarea)