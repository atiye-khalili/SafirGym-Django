from django.db import models
from django.contrib.auth.models import AbstractUser


class Register(AbstractUser):
    father_name = models.CharField(max_length=30, verbose_name='نام پدر', blank=True)
    birth_date = models.DateField(verbose_name='تاریخ تولد', null=True, blank=True)
    address = models.CharField(max_length=300, verbose_name='نشانی', blank=True)
    phone_number = models.CharField(max_length=11, verbose_name='شماره تلفن', blank=True)
    has_medical_condition = models.BooleanField(default=False, verbose_name='دارای شرایط پزشکی')
    describe_condition = models.TextField(verbose_name='شرح شرایط پزشکی', blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'.strip()

    class Meta:
        verbose_name = 'عضو'
        verbose_name_plural = 'اعضا'