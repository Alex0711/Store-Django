from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email= models.EmailField(verbose_name='Email', unique=True)
    country= models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    street=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username 
