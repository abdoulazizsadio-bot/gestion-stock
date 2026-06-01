from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('articles/', views.articles, name='articles'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
