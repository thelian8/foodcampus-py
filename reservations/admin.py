# C:\Users\Nicolas\Documents\foodcampuspro\reservations\admin.py

from django.contrib import admin
from .models import Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'menu',  # Changed from 'daily_menu' to 'menu'
        'category',  # Added category here
        'tickets_or_plates',
        'payment_method',
        'payment_status',
        'created_at'
    )
    list_filter = ('category', 'payment_status', 'payment_method')  # Added category here
    search_fields = (
        'user__username',
        'menu__name'  # Changed from 'daily_menu__menu_item__name' to 'menu__name'
                      # because DailyMenu itself has a 'name' field, not 'menu_item'.
    )