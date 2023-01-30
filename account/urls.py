from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginCustom, name='log-in'),
    path('logout/', views.logoutCutom, name='log-out'),
    path('regis/', views.register, name='regis'),
]