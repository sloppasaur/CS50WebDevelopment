from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello")

def nate(request):
    return HttpResponse("Hello, Nate!")

def olivia(request):
    return HttpResponse("I love you, Lovely")

def greet(request, name):
    return HttpResponse(f'Hello, {name.capitalize()}!')