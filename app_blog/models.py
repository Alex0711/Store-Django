from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
    name=models.CharField(max_length=50)
    created=models.DateTimeField(default=timezone.now)
    updated=models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categories'

    def __str__(self):
        return self.name


class Blog(models.Model):
    title=models.CharField(max_length=50)
    content=models.CharField(max_length=50)
    image=models.ImageField(upload_to='blog', null=True, blank=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    categories=models.ManyToManyField(Category)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='Post'
        verbose_name_plural='Posts'

    def __str__(self):
        return self.title