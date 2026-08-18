from django import forms
from core.models import *
from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator
class TrainerForm(forms.Form):
    first_name = forms.CharField(label='نام', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='نام خانوادگی', widget=forms.TextInput(attrs={'class' : 'form-control'}))
    birthdate = forms.DateField(label='تاریخ تولد', widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    phone_number = forms.CharField(validators=[RegexValidator(regex=r'^09\d{9}$',message='شماره تلفن باید با 09 شروع شود و 11 رقم باشد')],label='شماره تلفن', widget=forms.TextInput(attrs={'class': 'form-control'}))
    specialization = forms.ChoiceField(choices=ClassNameChoices.choices, label='تخصص', widget=forms.Select(attrs={'class': 'form-control'}))
    experience = forms.IntegerField(validators=[MinValueValidator(0, 'سابقه کاری نمی‌تواند منفی باشد')], label='سابقه کاری(سال)', widget=forms.TextInput(attrs={'class': 'form-control'}))
    biography = forms.CharField(validators=[MinLengthValidator(50, 'بیوگرافی حداقل باید 50 کاراکتر باشد'), MaxLengthValidator(500, 'بیوگرافی باید حداکثر 500 کاراکتر باشد')], label='بیوگرافی', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4})) 


class RegisterForm(forms.Form):
    first_name = forms.CharField(label='نام', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='نام خانوادگی', widget=forms.TextInput(attrs={'class' : 'form-control'}))
    father_name = forms.CharField(label='نام پدر', widget=forms.TextInput(attrs={'class' : 'form-control'}))
    birth_date = forms.DateField(label='تاریخ تولد', widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    address = forms.CharField(label='نشانی', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))
    phone_number = forms.CharField(validators=[RegexValidator(regex=r'^09\d{9}$',message='شماره تلفن باید با 09 شروع شود و 11 رقم باشد')],label='شماره تلفن', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email_address = forms.EmailField(label='نشانی ایمیل', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    has_medical_condition = forms.BooleanField(required=False, label='دارای شرایط پزشکی')
    describe_condition= forms.CharField(required=False, label='شرح شرایط پزشکی', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))