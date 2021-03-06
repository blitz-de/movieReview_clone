from django.contrib import admin
from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.home, name='home'),
    path('details/<int:id>/', views.details, name='detail'),
    path('addmovies/', views.add_movies, name='add_movies'),
    path('editmovies/<int:id>/', views.edit_movies, name='edit_movies')

]
