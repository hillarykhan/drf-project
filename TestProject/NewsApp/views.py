from django.shortcuts import redirect, render
from .models import News, RegistrationData
from .forms import RegistrationForm, RegistrationModel
from django.contrib import messages

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

def NewsDate(request, year):

    article_list = News.objects.filter(pub_date__year = year)

    context = {
        'year':year,
        'article_list':article_list
    }

    return render(request, 'newsdate.html', context)

def Contact(request):
    return render(request, 'contact.html')


def Register(request):

    context = {
        "form":RegistrationForm
    }
    return render(request, 'signup.html', context)

def addUser(request):
    form = RegistrationForm(request.POST)

    if form.is_valid():
        myregister = RegistrationData(
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password'],
            email = form.cleaned_data['email'],
            phone = form.cleaned_data['phone']
        )

        myregister.save()
        messages.add_message(request, messages.SUCCESS, "You have successfully signed up!")
    return redirect('register')

def modelForm(request):
    context = {
        "modelform":RegistrationForm
    }

    return render(request, 'modelform.html', context)

def addModelForm(request):
    mymodelform = RegistrationModel(request.POST)

    if mymodelform.is_valid():
        mymodelform.save()

    return redirect('form')
