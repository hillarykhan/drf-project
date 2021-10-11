from django.contrib import admin
from .models import News, RegistrationData, SportNews

# Register your models here.

admin.site.register(News)
admin.site.register(SportNews)
admin.site.register(RegistrationData)