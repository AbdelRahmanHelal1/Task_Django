from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index1(request):
    return HttpResponse('Custmer_index_number_1')

def index2(request):
    return HttpResponse('Custmer_index_number_2')
