from django.contrib import admin
from .models import YogaImage


@admin.register(YogaImage)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'image']
