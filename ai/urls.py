from django.urls import path

from . import views

urlpatterns = [
    # path('question/', views.show_question, name='show_question'),
    path('', views.home_page, name='home'),
    path('yoga/', views.ask_question, name='ask_question'),
    path('create_ai_form/', views.create_ai_form, name='aiform'),
]