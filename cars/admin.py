from django.contrib import admin

from .models import Car

from django.utils.html import format_html

# Register your models here.

class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px" />'.format(object.car_image.url))

    thumbnail.short_description = 'car image'
    list_display = ['id', 'car_title', 'thumbnail', 'model', 'city', 'color', 'body_style', 'fuel_type','is_featured']

    list_display_links = ('id', 'car_title', 'thumbnail')

    # add checkbox in admin
    list_editable = ('is_featured',)

    search_fields = ('id', 'car_title', 'city', 'model', 'body_style', 'fuel_type')

    list_filter = ('city', 'model', 'body_style', 'fuel_type')

admin.site.register(Car, CarAdmin)


