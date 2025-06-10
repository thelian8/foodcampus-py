# foodcampuspro/menus/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import DailyMenu # Ensure this is imported

@login_required
def student_menu_view(request):
    # Filter for menus specifically marked as 'student' type
    menu_items = DailyMenu.objects.filter(type='student', available=True).order_by('date', 'name')
    context = {'menu_items': menu_items}
    return render(request, 'menu/student_menu.html', context)

@login_required
def teacher_menu_view(request):
    # Filter for menus specifically marked as 'teacher' type
    menu_items = DailyMenu.objects.filter(type='teacher', available=True).order_by('date', 'name')
    context = {'menu_items': menu_items}
    return render(request, 'menu/teacher_menu.html', context)