from django.contrib import admin
from .models import Profile
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
    fields=['user', 'email', 'country', 'state', 'city', 'street', 'created', 'updated']
    list_display=('user', 'email', 'country', 'state', 'city', 'street', 'created', 'updated')


admin.site.register(Profile, ProfileAdmin)
