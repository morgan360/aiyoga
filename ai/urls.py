from django.urls import path

from . import views

urlpatterns = [
    # path('question/', views.show_question, name='show_question'),
    path('', views.home_page, name='home'),
    path('yoga/', views.ask_question, name='ask_question'),
    path('image/', views.generate_image, name='generate_image'),
    path('tai_yoga/', views.tai_yoga, name='tai_yoga'),
    path('create_ai_form/', views.create_ai_form, name='aiform'),
]