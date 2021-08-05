from django.urls import path
from calculator import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('<str:dish_name>/', views.dish_view, name='dish-view')
]
