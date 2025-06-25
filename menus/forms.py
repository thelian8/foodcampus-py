from django import forms
from .models import DailyMenu

class DailyMenuForm(forms.ModelForm):
    class Meta:
        model = DailyMenu
        fields = ['type', 'name', 'description', 'price', 'date', 'available', 'image']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'description': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-select'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'available': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'image': forms.FileInput(attrs={'class': 'form-control'})
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make the image field not required for updates
        if self.instance and self.instance.pk:
            self.fields['image'].required = False
