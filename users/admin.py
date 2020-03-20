from django.contrib import admin

# Register your models here.
from .models import UserDetails

@admin.register(UserDetails)
class UserDetailsAdmin(admin.ModelAdmin):
    list_display= ('adhar_number','name', 'address','phone_number',)
    ordering=('name',)
    search_fields=('name', 'adhar_number', 'phone_number',)