from django.shortcuts import render, HttpResponse


# Create your views here.
def home(request):
    """panels home page"""
    return HttpResponse("<h1>welcome to crypto funds portfolio</h1>")