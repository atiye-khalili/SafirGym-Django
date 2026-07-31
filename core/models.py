from django.db import models



class Register(models.Model):       #1
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    father_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    address = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=11)
    email_address = models.EmailField()
    has_medical_condition = models.BooleanField()
    describe_condition= models.TextField()


class Trainer(models.Model):        #2
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthdate = models.DateTimeField()
    phone_number = models.CharField(max_length=11)
    specialization = models.CharField(max_length=50)
    experience = models.CharField(50)
    biography = models.TextField()


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
    capacity = models.PositiveSmallIntegerField()
    schedule = models.CharField(max_length=100)


class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)