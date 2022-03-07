from django.contrib import admin
from .models import Blog, Category

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated',)

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)