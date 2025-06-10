from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_list, name='category_list'),  # Placeholder for listing categories
    path('<str:category>/', views.category_detail, name='category_detail'),  # Placeholder for category details
]