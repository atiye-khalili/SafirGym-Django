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

    def clean(self):
        data = super().clean()
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        if not password == confirm_password:
            raise ValidationError('گذرواژه با تکرار آن مطابقت نداشت')
        return data