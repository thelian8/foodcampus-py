# menus/admin.py
from django.contrib import admin
from .models import DailyMenu 
from django.utils.html import format_html
from django.templatetags.static import static

@admin.register(DailyMenu)
class DailyMenuAdmin(admin.ModelAdmin): 
    list_display = ('name', 'type', 'price', 'date', 'available', 'image_preview')
    list_filter = ('type', 'date', 'available') # You can now filter by 'type'
    search_fields = ('name', 'description')
    # Optional: Add date_hierarchy for convenient date navigation
    date_hierarchy = 'date'
    readonly_fields = ('image_preview',)
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="100" style="object-fit: cover;" />'.format(obj.image.url))
        return "No Image"
    image_preview.short_description = 'Preview'