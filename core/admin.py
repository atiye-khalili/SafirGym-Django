from django.contrib import admin
from core.models import Register, Trainer, GymClass, News


admin.site.register(Register)
admin.site.register(Trainer)
admin.site.register(GymClass)
admin.site.register(News)