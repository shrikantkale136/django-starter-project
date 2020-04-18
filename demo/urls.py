from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name = 'demo-home'),
    path('about/', views.about, name = 'demo-about'),
] 