from django.contrib import admin
from .models import DailyMenu

@admin.register(DailyMenu)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'student_price', 'teacher_price', 'available')
    list_filter = ('available',)
    search_fields = ('name',)