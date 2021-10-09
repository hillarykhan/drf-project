from django.urls import path
from .views import News

urlpatterns = [
    path('newsapp/', News, name='News')
]