from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Reservation
from menus.models import DailyMenu

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