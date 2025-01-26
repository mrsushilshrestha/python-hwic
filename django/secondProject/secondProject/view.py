from django.http import HttpResponse
from django.shortcuts import render


def product(request):
    return render(request,"product.html")


def login(request):
    return render(request,"login.html")

def index(request):
    return render(request,"index.html")

def signup(request):
    return render(request,"signup.html")

