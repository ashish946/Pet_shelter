from django.shortcuts import render
from .models import Animal

def home(request):
    animals=Animal.objects.all()
    return render(request,'home.html',{'animals':animals})

def search(request):
    return render(request,'search.html',{})