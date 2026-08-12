from django.shortcuts import render
from django.http import HttpResponse
from core.models import *

# def gym(request):
#     return render(request, 'core/index.html')

def home(request):
    name = Register.objects.first()
    context={
        'firstname' : name
    }
    return render(request, 'core/index.html', context=context)