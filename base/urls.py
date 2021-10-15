from django.contrib import admin
from django.urls import path
from . import views
from django.http import HttpResponse

urlpatterns = [
    path('', views.home, name='home'),
    path('room/<str:pk>/', views.room, name='room'),
    path('create-room/', views.create_Room, name='create-room'),
    path('update-room/<str:pk>/', views.update_Room, name='update-room'),
    path('delete-room/<str:pk>/', views.delete_Room, name='delete-room'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('delete-message/<str:pk>/', views.delete_message, name='delete-message'),
    path('user_profile/<str:pk>/', views.user_profile, name='user-profile'),
]