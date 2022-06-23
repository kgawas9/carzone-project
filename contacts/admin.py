from django.contrib import admin

from .models import Contact

# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'first_name', 'last_name', 'email', 'contact_no', 'car_title', 'created_date'
    ]

    list_display_links=[
        'id', 'first_name', 'last_name'
    ]

    search_fields = [
        'first_name', 'car_title', 'email'
    ]

    list_per_page = 25
    