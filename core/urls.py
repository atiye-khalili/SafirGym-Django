from django.urls import path
from  core.views import *

urlpatterns = [
    path('home/' , home, name='home'),
    path('news/' , news, name='news'),
    path('gymclass/' , gymclass, name='gymclass'),
    path('trainer/' , trainer, name='trainer'),
    path('trainer/detail/<int:trainer_id>/', trainer_detail, name='trainer_detail'),
]