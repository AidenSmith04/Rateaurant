from django.urls import path
from project import views

app_name = 'Rateaurant'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.NA, name='register'),
    path('login/', views.NA, name='login'),
    path('categories/', views.NA, name='categories'),
]