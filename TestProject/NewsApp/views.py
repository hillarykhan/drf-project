from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def Home(request):
    return HttpResponse("<h1>This is our homepage!</h1>")

def News(request):
    return HttpResponse("<h1>This is our latestest news</h1>")

def Contact(request):
    return HttpResponse("<h1>This is where you can contact us!</h1>")