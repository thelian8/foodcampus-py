from django.urls import path
from . import views

app_name = 'menus'

urlpatterns = [
    
    path('student/', views.student_menu_view, name='student_menu'),
    path('teacher/', views.teacher_menu_view, name='teacher_menu'),
]