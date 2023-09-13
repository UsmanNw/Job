from django.urls import path
from . import views


urlpatterns= [
    path('', views.index, name='index'),
    path('categories/', views.categories, name='categories'),
    path('categories/add', views.addProducts, name='categories-add'),
    path('products/', views.products, name='products'),
    path('products/add', views.addCategories, name='products-add'),

]