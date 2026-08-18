from django.urls import path
from  core.views import *

urlpatterns = [
    path('home/' , home, name='home'),
    path('news/' , news, name='news'),
    path('gymclass/' , gymclass, name='gymclass'),
    path('trainer/' , trainer, name='trainer'),
    path('trainer/detail/<int:trainer_id>/', trainer_detail, name='trainer_detail'),
    path('news/detail/<int:news_id>/', news_detail, name='news_detail'),
    path('trainer/form/', trainer_form , name='trainer_form'),
    path('register/form/', register_form, name='register_form')
]