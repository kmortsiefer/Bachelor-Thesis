from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='main-home'),
    path('api/', views.api, name='main-api')
]
