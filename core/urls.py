
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('onlineshop/', include('onlineshop.urls')),
    path("api/", include("api.urls")),
]
