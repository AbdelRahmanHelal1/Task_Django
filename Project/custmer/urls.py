from . import views
from django.urls import path

urlpatterns = [
    path("custmer/index1",views.index1,name='index1'),
    path("custmer/index2",views.index2,name='index2'),
    
]