from django.shortcuts import render, redirect
from .forms import CategoriesForm, ProductsForm
from .models import Categories, Products
# Create your views here.


def index(request):
    context = {}
    return render(request, 'index.html', context)



def addCategories(request):
    
    if request.method == 'POST':
        form = CategoriesForm()
        if form.is_valid():
            form.save()
            return redirect('index')
        

def addProducts(request):
    
    if request.method == 'POST':
        form = ProductsForm()
        if form.is_valid():
            form.save()
            return redirect('index')