from django.shortcuts import render, HttpResponse


# Create your views here.
def home(request):
    """panels home page"""
    return render(request, 'panel/dashboard.html')