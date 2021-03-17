from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hello_message(request):
    return HttpResponse("Hello from my soul, World!!!")
