from django.contrib import admin

# Register your models here.
from .models import WeekDay, Meal
admin.site.register(WeekDay)
admin.site.register(Meal)