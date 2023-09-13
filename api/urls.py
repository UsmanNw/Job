from django.urls import path
from . import views
urlpatterns = [
    
    path('', views.getRoutes),
    
    path('categories/', views.getCategories),
    path('products/', views.getProducts)
    
]