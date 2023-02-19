from django.urls import path
from . import views

urlpatterns = [
    path('slideshow/', views.slideshow, name='slideshow'),
    path('yoga_image/', views.image_view, name='yoga_image'),
    ]
