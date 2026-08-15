from django.shortcuts import render , get_object_or_404 , redirect
from django.contrib import messages
from django.http import HttpResponse
from core.models import *


def home(request):
    name = Register.objects.first()
    return render(request, 'core/home.html', context={
        'firstname' : name.first_name
    })

def news(request):
    news = News.objects.last()
    # context= {
    #     'news_title': news.title
    # }
    return render(request, 'core/news.html', context={
        'news_title': news.title
    })

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
    detail= Trainer.objects.get(id=trainer_id)
    return render(request, 'core/trainer_detail.html', context={'detail': detail})