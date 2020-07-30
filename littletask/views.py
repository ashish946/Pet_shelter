from django.shortcuts import render
from .models import littask

# Create your views here.
def home(request):
    t=littask.objects
    return render(request,'littletask/home.html',{'img':t})
