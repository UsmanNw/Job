from django.forms import ModelForm
from .models import Categories, Products

class CategoriesForm(ModelForm):
    class Meta:
        model = Categories
        fields = '__all__'
        

class ProductsForm(ModelForm):
    class Meta:
        model = Categories
        fields = '__all__'