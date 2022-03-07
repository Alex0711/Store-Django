from django.contrib import admin
from .models import *

# Register your models here.

class ServiceAdmin(admin.ModelAdmin):
    fields = ["title", "content", "image", "created", "updated"]
    readonly_fields=('created', 'updated',)
    list_display = ("title", "content", "created", "updated")
    search_fields = ["title"]
    list_filter=("created", "updated")
    date_hierarchy="created"

admin.site.register(Service, ServiceAdmin)