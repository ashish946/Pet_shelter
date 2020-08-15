from django.shortcuts import render
from .models import Animal
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404

def home(request):
    animals=Animal.objects.all()
    cats=Animal.objects.filter(animal='Cat')
    paginator1=Paginator(cats,1)
    page=request.GET.get('catpage')
    cats=paginator1.get_page(page)

    dogs=Animal.objects.filter(animal='Dog')
    paginator2 = Paginator(dogs, 1)
    page2 = request.GET.get('dogpage')
    dogs = paginator2.get_page(page2)

    return render(request,'home.html',{'animals':animals,'cats':cats,'dogs':dogs})

def search(request):
    return render(request,'search.html',{})

def detail(request,animal_id):
    animal=get_object_or_404(Animal,pk=animal_id)
    animals=Animal.objects.all()
    return render(request,'detail.html',{'animal':animal,'animals':animals})

