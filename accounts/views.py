# foodcampuspro/accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm # <--- IMPORT THIS
from .forms import CustomUserCreationForm
from .models import CustomUser

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Registration successful! Please log in.")
            return redirect('accounts:login')
        else:
            messages.error(request, "Registration failed. Please correct the errors below.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'auth/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST) # <--- Instantiate form with POST data
        if form.is_valid(): # <--- Validate the form
            username = form.cleaned_data.get('username') # <--- Get cleaned data
            password = form.cleaned_data.get('password') # <--- Get cleaned data
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.category == 'student':
                    messages.success(request, f"Welcome, {user.username}! Redirecting to student menu.")
                    return redirect('menus:student_menu')
                elif user.category == 'teacher':
                    messages.success(request, f"Welcome, {user.username}! Redirecting to teacher menu.")
                    return redirect('menus:teacher_menu')
                else:
                    messages.success(request, f"Welcome, {user.username}! Redirecting to homepage.")
                    return redirect('homepage')
            # The authenticate call above would return None if credentials are bad,
            # but form.is_valid() should catch basic errors.
            # If form.is_valid() is True but authenticate returns None, it implies a deeper issue
            # or custom authentication backend that's not being hit.
        else:
            # Form is not valid (e.g., fields missing, invalid username/password)
            messages.error(request, "Invalid username or password.") # Or form.errors for more detail
            # If you want to show form errors:
            # for field, errors in form.errors.items():
            #     for error in errors:
            #         messages.error(request, f"{field}: {error}")
    else:
        form = AuthenticationForm() # <--- Instantiate an empty form for GET request
    return render(request, 'registration/login.html', {'form': form}) # <--- Pass form to template

def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('homepage')

# REMOVE THESE DUPLICATE VIEWS FROM accounts/views.py (as per previous instructions)
# @login_required
# def student_menu_view(request):
#     return render(request, 'menu/student_menu.html')

# @login_required
# def teacher_menu_view(request):
#     return render(request, 'menu/teacher_menu.html')