# foodcampuspro/accounts/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
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
    
    # Password reset URLs (new functionality)
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='auth/password_reset.html',
        email_template_name='auth/password_reset_email.html',
        subject_template_name='auth/password_reset_subject.txt'
    ), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='auth/password_reset_done.html'
    ), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='auth/password_reset_confirm.html'
    ), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='auth/password_reset_complete.html'
    ), name='password_reset_complete'),
]