from django.shortcuts import render
from django.http import HttpResponse
from core.models import *


def home(request):
    name = Register.objects.first()
    context={
        'firstname' : name.first_name
    }
    return render(request, 'core/home.html', context=context)

def news(request):
    news = News.objects.last()
    context= {
        'news_title': news.title
    }
    return render(request, 'core/news.html', context=context)

def gymclass(request):
    classes = GymClass.objects.all()
    context={
        'classes' : classes.classes.class_name
    }
    return render(request, 'core/gymclass.html', context=context)
