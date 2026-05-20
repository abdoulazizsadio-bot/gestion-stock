from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('articles/', views.articles, name='articles'),
    path('templates_base/', views.templates_base, name='templates_base'),
]
