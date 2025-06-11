# menus/admin.py
from django.contrib import admin
from .models import DailyMenu # Ensure DailyMenu is imported

@admin.register(DailyMenu)
class DailyMenuAdmin(admin.ModelAdmin): # Consider renaming your class to DailyMenuAdmin
    list_display = ('name', 'type', 'price', 'date', 'available')
    list_filter = ('type', 'date', 'available') # You can now filter by 'type'
    search_fields = ('name', 'description')
    # Optional: Add date_hierarchy for convenient date navigation
    date_hierarchy = 'date'