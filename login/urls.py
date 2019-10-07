from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login_request/', views.login, name='login_request')
]