from . import views
from django.urls import path

urlpatterns = [
    path("products/index3",views.index3,name='index3'),
    path("products/index4",views.index4,name='index4'),
    
]