from django.urls import path
from .views import NewsP, Home, Contact, NewsDate, Register, addUser, modelForm, addModelForm

urlpatterns = [
    path('', Home, name='home'),
    path('newsapp/', NewsP, name='news'),
    path('archive/<int:year>', NewsDate, name='newsdate'),
    path('contact/', Contact, name='contact'),
    path('signup/', Register, name='register'),
    path('addUser/', addUser, name='addUser'),
    path('modelform/', modelForm, name='form'),
    path('addmodelform/', addModelForm, name='modelform')
]