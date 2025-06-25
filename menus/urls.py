from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

app_name = 'menus'

urlpatterns = [
    
    path('student/', views.student_menu_view, name='student_menu'),
    path('teacher/', views.teacher_menu_view, name='teacher_menu'),
    path('admin/upload/', views.admin_menu_upload, name='admin_menu_upload'),
    path('admin/delete/<int:item_id>/', views.delete_menu_item, name='delete_menu_item'),
    path('submit-ticket-order/', csrf_exempt(views.submit_ticket_order), name='submit_ticket_order'),
]