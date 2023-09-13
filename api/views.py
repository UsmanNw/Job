from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CategoriesSerializer, ProductsSerializer
from onlineshop.models import Categories, Products

@api_view(['GET'])
def getRoutes(request):

    routes = [
        {'GET': '/api/products/'},
        {'GET': '/api/products/id'},
        {'POST': '/api/products/add'},
        {'PUT': '/api/products/id'},
        {'POST': '/api/products/delete/id'},
        {'POST': '/api/products/product-image/id'},
        
        
    ]
    
    return Response(routes)


@api_view(['GET'])
def getCategories(request):
    categories = Categories.objects.all()
    serializer = CategoriesSerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProducts(request):
    products = Products.objects.all()
    serializer = ProductsSerializer(products, many=True)
    return Response(serializer.data)