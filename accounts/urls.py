# foodcampuspro/accounts/urls.py

from django.urls import path
from . import views

# Optional: Add app_name for clarity, though not strictly required for this file if no other app redirects to its internal URLs
app_name = 'accounts'

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),      # <--- Use your custom login view
    path('logout/', views.logout_view, name='logout'),    # <--- Use your custom logout view
    # IMPORTANT: REMOVE THESE LINES, as student/teacher menus are in the 'menus' app
    # path('student-menu/', views.student_menu_view, name='student_menu'),
    # path('teacher-menu/', views.teacher_menu_view, name='teacher_menu'),
]