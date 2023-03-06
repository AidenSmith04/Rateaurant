from django.urls import path
from project import views

app_name = 'Rateaurant'

urlpatterns = [
    path('', views.home, name='home'),
    path('categories/', views.categories, name='categories'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('addarestaurant/', views.add_a_restaurant, name='addarestaurant'),
    path('logout/', views.user_logout, name='logout'),
    path('category/<slug:category_name>/', views.show_category, name='show_category'),
    path('category/<category_name>/<slug:venue_id>', views.show_venue, name='show_venue'),
]
