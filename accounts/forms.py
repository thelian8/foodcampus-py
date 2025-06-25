# foodcampuspro/accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
import re

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label="Email Address", required=False)
    phone_number = forms.CharField(label="Phone Number", max_length=20)
    category = forms.ChoiceField(label="Category", choices=CustomUser.CATEGORY_CHOICES)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email', 'phone_number', 'category',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Apply the styling to all relevant fields
        self.fields['username'].widget.attrs.update({'placeholder': 'Enter your username', 'style': 'width: 100%; padding: 12px; border: 1px solid #ccc; border-radius: 8px; font-size: 16px;'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Enter your email', 'style': 'width: 100%; padding: 12px; border: 1px solid #ccc; border-radius: 8px; font-size: 16px;'})
        self.fields['phone_number'].widget.attrs.update({'placeholder': 'Enter your phone number', 'style': 'width: 100%; padding: 12px; border: 1px solid #ccc; border-radius: 8px; font-size: 16px;'})
        self.fields['category'].widget.attrs.update({'style': 'width: 100%; padding: 12px; border: 1px solid #ccc; border-radius: 8px; font-size: 16px;'})

        # CORRECTED: Use 'password' and 'password2' for styling
        if 'password' in self.fields: # Safely check if the field exists
            self.fields['password'].widget.attrs.update({'placeholder': 'Enter your password', 'style': 'width: 100%; padding: 12px; border: 1px solid #ccc; border-radius: 8px; font-size: 16px;'})
        if 'password2' in self.fields: # Safely check for password2
            self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm your password', 'style': 'width: 100%; padding: 12px; border: 1px solid #ccc; border-radius: 8px; font-size: 16px;'})
        # Note: 'password_confirmation' is not a field provided by UserCreationForm.

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            return None
        return email

    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        if not re.fullmatch(r'6\d{8}', phone):
            raise forms.ValidationError('Phone number must be in the format 6XXXXXXXX (must start with 6 and have 8 more digits, no country code).')
        return phone