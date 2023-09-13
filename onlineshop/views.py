from django.shortcuts import render, redirect
from .forms import CategoriesForm, ProductsForm
from .models import Categories, Products
# Create your views here.


def index(request):
    context = {}
    return render(request, 'index.html', context)



def categories(request):
    
  categories = Categories.objects.all()
  
  context = {
      'categories' : categories
  }  

  return render(request, 'categories.html', context)  



def products(request):
    
  Products = Products.objects.all()
  
  context = {
      'products' : Products
  }  

  return render(request, 'products.html', context)  



def addCategories(request):
    
    if request.method == 'POST':
        form = CategoriesForm()
        if form.is_valid():
            form.save()
            return redirect('categories')
        

def addProducts(request):
    
    if request.method == 'POST':
        form = ProductsForm()
        if form.is_valid():
            form.save()
            return redirect('products')