from django.urls import path
from .views import reservation_list, reservation_confirmation, make_reservation, ajax_reservation

urlpatterns = [
    path('', reservation_list, name='reservation_list'),
    path('confirmation/<int:reservation_id>/', reservation_confirmation, name='reservation_confirmation'),
    path('make/<int:daily_menu_id>/', make_reservation, name='make_reservation'),
    path('ajax_reservation/', ajax_reservation, name='ajax_reservation'),
]