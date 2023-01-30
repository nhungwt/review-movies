from django.urls import path
from . import views

urlpatterns = [
    path('', views.listMovie, name='listMovie'),
    path('<int:pk>/', views.movieDetail, name='movie_detail'),
]