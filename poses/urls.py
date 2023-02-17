from django.urls import path
from . import views

urlpatterns = [
    path('poses/', views.pose_list, name='pose_list'),
    path('poses/new/', views.pose_new, name='pose_new'),
    path('poses/<int:pk>/edit/', views.pose_edit, name='pose_edit'),
]
