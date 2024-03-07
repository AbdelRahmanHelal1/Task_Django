from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index3(request):

    return HttpResponse("Products_index_3")

def index4(request):

    return HttpResponse("Products_index_4")
