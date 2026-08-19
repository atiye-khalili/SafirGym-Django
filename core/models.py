from django.db import models
from django.contrib.auth.models import AbstractUser



class Register(models.Model):       #1
    first_name = models.CharField(max_length=30, verbose_name='نام')
    last_name = models.CharField(max_length=30, verbose_name='نام خانوادگی')
    father_name = models.CharField(max_length=30, verbose_name='نام پدر')
    birth_date = models.DateField(verbose_name='تاریخ تولد')
    address = models.CharField(max_length=300, verbose_name='نشانی')
    phone_number = models.CharField(max_length=11, verbose_name='شماره تلفن')
    email_address = models.EmailField(verbose_name='نشانی ایمیل')
    has_medical_condition = models.BooleanField(verbose_name='دارای شرایط پزشکی')
    describe_condition= models.TextField(verbose_name='شرح شرایط پزشکی')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'ثبت نام'
        verbose_name_plural = 'ثبت نام'


class ClassNameChoices(models.TextChoices):
    KICKBOXING = ('kickboxing', 'کیک بوکسینگ')
    MUAYTHAI = ('muaythai', 'موی تای')
    BOXING = ('boxing', 'بوکس')
    FITNESS = ('fitness', 'فیتنس')
    TRX = ('trx', 'تی آر ایکس')
    CROSSFIT = ('crossfit', 'کراسفیت')


# class Register(AbstractUser):       #1



#     class Meta():
#         verbose_name = 'ثبت نام'
#         verbose_name_plural = 'ثبت نام'‌

class Trainer(models.Model):        #2
    first_name = models.CharField(max_length=30, verbose_name='نام')
    last_name = models.CharField(max_length=30, verbose_name='نام خانوادگی')
    birthdate = models.DateField(verbose_name='تاریخ تولد')
    phone_number = models.CharField(max_length=11, verbose_name='شماره تلفن')
    specialization = models.CharField(max_length=50,choices=ClassNameChoices.choices ,verbose_name='تخصص')
    experience = models.PositiveSmallIntegerField(verbose_name='سابقه کاری(سال)')
    biography = models.TextField(verbose_name='بیوگرافی', null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} : {self.specialization}"
    class Meta:
        verbose_name = 'مربی'
        verbose_name_plural = 'مربیان'


class GymClass(models.Model):       #3
    class_name = models.CharField(max_length=50, choices=ClassNameChoices.choices)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    capacity = models.PositiveSmallIntegerField(verbose_name='ظرفیت کلاس')
    schedule = models.CharField(max_length=100, verbose_name='برنامه زمانی کلاس')

    def __str__(self):
        return f"{self.class_name} : {self.trainer.first_name} {self.trainer.last_name}"
    class Meta:
        verbose_name = 'کلاس'
        verbose_name_plural = 'کلاس‌ها'


class News(models.Model):   #4
    title = models.CharField(max_length=100, verbose_name='عنوان')
    content = models.TextField(verbose_name='محتوا')
    image = models.ImageField(upload_to='news_images/', verbose_name='تصویر',
        null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='ایجاد شده در تاریخ')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'خبر'
        verbose_name_plural = 'اخبار'