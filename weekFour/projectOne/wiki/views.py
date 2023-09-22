from django.http import HttpResponseRedirect
from django import forms
from django.shortcuts import render
from django.urls import reverse


entries = []

# Create your views here.
def index(request):
    return render(request, "wiki/index.html")

def entry(request):
    return render(request, "wiki/entry.html")

