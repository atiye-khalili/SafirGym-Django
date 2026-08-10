from django.db import models



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

    class Meta:
        verbose_name = 'ثبت نام'
        verbose_name_plural = 'ثبت نام'


class Trainer(models.Model):        #2
    first_name = models.CharField(max_length=30, verbose_name='نام')
    last_name = models.CharField(max_length=30, verbose_name='نام خانوادگی')
    birthdate = models.DateTimeField(verbose_name='تاریخ تولد')
    phone_number = models.CharField(max_length=11, verbose_name='شماره تلفن')
    specialization = models.CharField(max_length=50, verbose_name='تخصص')
    experience = models.CharField(max_length=50, verbose_name= 'سابقه کاری(سال)')
    biography = models.TextField(verbose_name='بیوگرافی')

    class Meta:
        verbose_name = 'مربی'
        verbose_name_plural = 'مربیان'


class ClassNameChoices(models.TextChoices):
    KICKBOXING = ('kickboxing', 'کیک بوکسینگ')
    MUAYTHAI = ('muaythai', 'موی تای')
    BOXING = ('boxing', 'بوکس')
    FITNESS = ('fitness', 'فیتنس')
    TRX = ('trx', 'تی آر ایکس')
    CROSSFIT = ('crossfit', 'کراسفیت')
    
class GymClass(models.Model):       #3
    class_name = models.CharField(max_length=50, choices=ClassNameChoices.choices)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    capacity = models.PositiveSmallIntegerField(verbose_name='ظرفیت کلاس')
    schedule = models.CharField(max_length=100, verbose_name='برنامه زمانی کلاس')

    class Meta:
        verbose_name = 'کلاس'
        verbose_name_plural = 'کلاس‌ها'


class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    content = models.TextField(verbose_name='محتوا')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='ایجاد شده در تاریخ')

    class Meta:
        verbose_name = 'خبر'
        verbose_name_plural = 'اخبار'