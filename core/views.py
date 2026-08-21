from django.shortcuts import render , get_object_or_404 , redirect
from django.contrib import messages
from django.http import HttpResponse
from core.models import *
from core.forms import *
from account.models import Register

def home(request):
    name = Register.objects.first()
    return render(request, 'core/home.html', context={
        'firstname' : name.first_name
    })

def news(request):
    news = News.objects.order_by('-created_at')
    return render(request, 'core/news.html', context={
        'news': news
    })

def news_detail(request, news_id):
    news = News.objects.get_object_or_404(News, pk=news_id)
    return render(request, 'core/news_detail.html', context={'news': news})

def gymclass(request):
    classes = GymClass.objects.all()
    return render(request, 'core/gymclass.html', context={
        'classes' : classes
    })



def trainer(request):
    trainer = Trainer.objects.all()
    return render(request, 'core/trainer.html', context={
        'trainer' : trainer
    })

def trainer_detail(request, trainer_id):
    detail= Trainer.objects.get_object_or_404(Trainer, pk=trainer_id)
    return render(request, 'core/trainer_detail.html', context={'detail': detail})

def trainer_form(request):
    form = TrainerForm()
    if request.method == 'POST':
        form = TrainerForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            birthdate = form.cleaned_data.get('birthdate')
            phone_number = form.cleaned_data.get('phone_number')
            specialization = form.cleaned_data.get('specialization')
            experience = form.cleaned_data.get('experience')
            biography = form.cleaned_data.get('biography')
            new = Trainer.objects.create(first_name = first_name, last_name = last_name, 
                birthdate = birthdate, phone_number = phone_number, specialization = specialization, 
                experience = experience, biography = biography)
            messages.success(request, 'مربی با موفقیت ثبت شد.')
            return redirect('trainer')
        else:
            print(form.errors)
    context = {'form': form}
    return render(request, 'core/trainer_form.html', context=context)

def trainer_edit(request, trainer_id):
    t = Trainer.objects.filter(pk=trainer_id)
    trainer = t.first()

    form = TrainerForm(initial={
        'first_name': trainer.first_name,
        'last_name': trainer.last_name,
        'birthdate': trainer.birthdate,
        'phone_number': trainer.phone_number,
        'specialization': trainer.specialization,
        'experience': trainer.experience,
        'biography': trainer.biography,
    })
    if request.method == 'POST':
        form = TrainerForm(instance=trainer, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'مربی با موفقیت ویرایش شد')
            return redirect('trainer_detail', trainer_id=trainer.id)
    return render(request, 'core/trainer_edit.html', context={'form': form, 't': trainer})

def trainer_delete(request, trainer_id):
    trainer = get_object_or_404(Trainer, pk=trainer_id)
    trainer.delete()
    messages.success(request, 'مربی با موفقیت حذف شد')
    return redirect('trainer')



# def register_form(request):
#     form = RegisterForm()
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data.get('first_name')
#             last_name = form.cleaned_data.get('last_name')
#             father_name = form.cleaned_data.get('father_name')
#             birth_date = form.cleaned_data.get('birth_date')
#             address = form.cleaned_data.get('address')
#             phone_number = form.cleaned_data.get('phone_number')
#             email_address = form.cleaned_data.get('email_address')
#             has_medical_condition = form.cleaned_data.get('has_medical_condition')
#             describe_condition = form.cleaned_data.get('describe_condition')
#             new = Register.objects.create(first_name=first_name, last_name=last_name, 
#             father_name=father_name, birth_date=birth_date, address=address, 
#             phone_number=phone_number, email_address=email_address, 
#             has_medical_condition=has_medical_condition, describe_condition=describe_condition)
#             messages.success(request, 'ثبت نام با موفقیت انجام شد.')
#             return redirect('home')
#         else:
#             print(form.errors)
#     return render(request, 'core/register_form.html', context={'form' : form})