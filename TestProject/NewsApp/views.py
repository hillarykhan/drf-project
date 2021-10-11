from django.shortcuts import render
from .models import News

# Create your views here.

def Home(request):
    context = {
        "name":"Parwiz Forogh",
        "number":8537812
        
    }

    return render(request, 'home.html', context)

def NewsP(request):
    obj = News.objects.get(id=1)

    context = {
        "data":obj
    }

    return render(request, 'news.html', context)

def NewsDate(request):

    return render(request, 'newsdate.html')

def Contact(request):
    return render(request, 'contact.html')