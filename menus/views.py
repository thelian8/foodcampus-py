# foodcampuspro/menus/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils import timezone
from django.contrib import messages
from django.http import JsonResponse
from .models import DailyMenu, TicketOrder
from django.views.decorators.http import require_http_methods
from .forms import DailyMenuForm

def is_admin(user):
    return user.is_authenticated and user.is_staff

#@login_required
def student_menu_view(request):
    # Get today's date
    today = timezone.now().date()
    
    # Get available menu items for students for today
    menu_items = DailyMenu.objects.filter(
        type='student',
        available=True,
        date=today  # Only show today's menu
    ).order_by('name')
    
    # Get the first menu item with an image, if any
    menu_image = None
    if menu_items and hasattr(menu_items[0], 'image') and menu_items[0].image:
        menu_image = menu_items[0].image
    
    context = {
        'menu_items': menu_items,
        'menu_image': menu_image,
        'today': today
    }
    return render(request, 'menu/student_menu.html', context)


@require_http_methods(["POST"])
def submit_ticket_order(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            ticket_quantity = int(request.POST.get('ticketQuantity', 1))
            payment_method = request.POST.get('paymentMethod')
            
            # Validate ticket quantity
            if ticket_quantity < 1 or ticket_quantity > 15:
                return JsonResponse({
                    'success': False,
                    'message': 'Ticket quantity must be between 1 and 15.'
                }, status=400)
            
            # Validate payment method
            valid_payment_methods = dict(TicketOrder.PAYMENT_METHODS).keys()
            if payment_method not in valid_payment_methods:
                return JsonResponse({
                    'success': False,
                    'message': 'Invalid payment method.'
                }, status=400)
            
            # Create the order
            order = TicketOrder.objects.create(
                name=name,
                ticket_quantity=ticket_quantity,
                payment_method=payment_method,
                is_confirmed=True
            )
            
            return JsonResponse({
                'success': True,
                'message': 'Your ticket order has been placed successfully!',
                'order_id': order.id
            })
            
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': f'An error occurred: {str(e)}'
            }, status=500)
    
    return JsonResponse({
        'success': False,
        'message': 'Invalid request method.'
    }, status=405)

#@login_required
def teacher_menu_view(request):
    # Get today's date
    today = timezone.now().date()
    
    # Get available menu items for teachers for today
    menu_items = DailyMenu.objects.filter(
        type='teacher',
        available=True,
        date=today  # Only show today's menu
    ).order_by('name')
    
    context = {
        'menu_items': menu_items,
        'today': today
    }
    return render(request, 'menu/teacher_menu_new.html', context)

@login_required
@user_passes_test(is_admin)
def admin_menu_upload(request):
    if request.method == 'POST':
        form = DailyMenuForm(request.POST, request.FILES)
        if form.is_valid():
            menu = form.save(commit=False)
            menu.save()
            messages.success(request, 'Menu item added successfully!')
            return redirect('admin_menu_upload')
    else:
        form = DailyMenuForm()
    
    # Get all menu items for the admin to view
    menu_items = DailyMenu.objects.all().order_by('-date', 'type')
    return render(request, 'menu/admin_menu_upload.html', {
        'form': form,
        'menu_items': menu_items
    })

@login_required
@user_passes_test(is_admin)
def delete_menu_item(request, item_id):
    menu_item = get_object_or_404(DailyMenu, id=item_id)
    if request.method == 'POST':
        menu_item.delete()
        messages.success(request, 'Menu item deleted successfully!')
    return redirect('admin_menu_upload')