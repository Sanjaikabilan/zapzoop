from django.urls import path, include
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
     path('login/', views.login, name ='login'),
    path('register/', views.register, name='register'),
    path('upload/', views.upload, name='upload'),
    path('vault/', views.vault, name='vault'),
     path('posts/<int:pk>/', views.delete_post, name='delete_post'),
    
]