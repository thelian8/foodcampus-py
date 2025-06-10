# foodcampuspro/accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # Import AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('category',) # Ensure category is included in registration

# You can use Django's built-in AuthenticationForm directly in views,
# or define a custom one if you need extra fields or validation specific to login.
# For now, let's just assume we'll use Django's default for simplicity.
# If you DID want to customize it, it might look like this:
# class LoginForm(AuthenticationForm):
#     # You could add custom fields here if needed
#     passS