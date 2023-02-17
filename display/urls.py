from django.urls import path
from . import views

urlpatterns = [
    path('slideshow/', views.slideshow, name='slideshow'),
    ]
