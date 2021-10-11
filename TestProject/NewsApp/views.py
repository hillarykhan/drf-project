from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def Home(request):
    context = {
        "name":"Parwiz Forogh",
        "number":8537812
        
    }

    return render(request, 'home.html', context)

def News(request):
    context = {
        "list":["Python", "Java", "Ruby", "C++", "C#", "Kotlin"]
    }

    return render(request, 'news.html', context)

def Contact(request):
    return render(request, 'contact.html')