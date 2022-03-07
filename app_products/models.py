from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class ProductCategory(models.Model):
    name=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=300)
    image=models.ImageField(upload_to='products', null=True, blank=True)
    price=models.FloatField()
    availability=models.BooleanField(default=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    category=models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='Product'
        verbose_name_plural='Products'

    def __str__(self):
        return self.title