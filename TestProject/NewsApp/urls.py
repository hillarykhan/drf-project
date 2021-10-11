from django.urls import path
from .views import NewsP, Home, Contact, NewsDate

urlpatterns = [
    path('', Home, name='home'),
    path('newsapp/', NewsP, name='news'),
    path('archive/<int:year>', NewsDate, name='newsdate'),
    path('contact/', Contact, name='contact')
]