from django.urls import path
from . import views

urlpatterns = [
    path('', views.first, name='first'),
    path('home', views.index, name='home'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    

]
