from django import forms
from core.models import *
from django.core.validators import RegexValidator, MinLengthValidator



class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = [
            'first_name', 'last_name', 'birthdate', 'phone_number',
            'specialization', 'experience', 'biography'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'birthdate': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'specialization': forms.Select(attrs={'class': 'form-select'}),
            'experience': forms.NumberInput(attrs={'class': 'form-control'}),
            'biography': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
