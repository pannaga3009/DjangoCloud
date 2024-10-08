from django.urls import path
from . import views

urlpatterns = [
    path('recipes/', views.recipe_list, name='recipe-list'),
    path('recipes/<int:pk>/', views.recipe_detail, name='recipe-detail'),
]