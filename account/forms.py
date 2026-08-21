from django.core.exceptions import ValidationError
from django import forms
from account.models import *


class LoginForm(forms.Form):
    username = forms.CharField(max_length=60, label='نام کاربری')
    password = forms.CharField(max_length=50, label='گذرواژه', widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))


class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(
        max_length=60,
        label='تکرار گذرواژه',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'})
    )

    class Meta:
        model = Register
        fields = [
            'username', 'first_name', 'last_name', 'email',
            'password', 'confirm_password',
            'father_name', 'birth_date', 'address', 'phone_number',
            'has_medical_condition', 'describe_condition'
        ]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'father_name': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'has_medical_condition': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'describe_condition': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def clean(self):
        data = super().clean()
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise ValidationError('گذرواژه با تکرار آن مطابقت نداشت')
        return data