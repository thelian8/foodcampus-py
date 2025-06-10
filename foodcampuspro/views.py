from django.shortcuts import render
from django.contrib import messages
from menus.models import DailyMenu
from accounts.models import CustomUser

def homepage_view(request):
    show_menu = request.GET.get('show_menu', False)
    menu_items = None
    if show_menu:
        menu_items = DailyMenu.objects.filter(available=True)
        if not menu_items.exists():
            messages.info(request, "No meals available yet. Check back later!")
    if request.user.is_authenticated and menu_items and menu_items.exists():
        messages.success(request, "Great news! Today's meals are ready early. Place your reservation now!")
    return render(request, 'homepage.html', {'menu_items': menu_items, 'show_menu': show_menu})