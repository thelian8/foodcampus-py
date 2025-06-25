from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Reservation
from menus.models import DailyMenu
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import datetime

@login_required
def make_reservation(request, daily_menu_id):
    daily_menu = get_object_or_404(DailyMenu, id=daily_menu_id)
    if request.method == 'POST':
        tickets_or_plates = int(request.POST.get('tickets_or_plates', 1))
        payment_method = request.POST.get('payment_method')
        reservation = Reservation.objects.create(
            user=request.user,
            daily_menu=daily_menu,
            tickets_or_plates=tickets_or_plates,
            payment_method=payment_method,
            payment_status='pending'
        )
        messages.success(request, "Reservation created! Please complete your payment to confirm.")
        return redirect('reservation_list')
    return render(request, 'reservations/make_reservation.html', {'daily_menu': daily_menu})

@login_required
def reservation_list(request):
    reservations = Reservation.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'reservations/reservation_list.html', {'reservations': reservations})

@login_required
def reservation_confirmation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id, user=request.user)
    return render(request, 'reservations/reservation_confirmation.html', {'reservation': reservation})

@csrf_exempt
def ajax_reservation(request):
    if request.method == 'POST':
        import json
        data = json.loads(request.body.decode('utf-8'))
        name = data.get('full_name')
        phone = data.get('phone_number')
        tickets = int(data.get('num_tickets', 1))
        menu_id = data.get('meal_id')
        # Use the logged-in user's category if authenticated
        if request.user.is_authenticated:
            category = getattr(request.user, 'category', None)
        else:
            category = data.get('category', 'student')
        from menus.models import DailyMenu
        try:
            menu = DailyMenu.objects.get(id=menu_id)
        except DailyMenu.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Menu item not found.'}, status=400)
        Reservation.objects.create(
            user=request.user if request.user.is_authenticated else None,
            menu=menu,
            category=category,
            tickets_or_plates=tickets,
            payment_method='Mobile Money',
            payment_status='pending',
        )
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'error': 'Invalid request.'}, status=400)

@login_required
def user_reservations(request):
    reservations = Reservation.objects.filter(user=request.user).order_by('-created_at')
    data = [
        {
            'menu': r.menu.name,
            'tickets_or_plates': r.tickets_or_plates,
            'created_at': r.created_at.strftime('%Y-%m-%d %H:%M'),
            'category': r.category,
            'day_of_week': r.created_at.strftime('%A'),
        }
        for r in reservations
    ]
    return JsonResponse({'reservations': data})