from django.contrib import admin

# Register your models here.

from django.contrib import admin

#register my models here
from .models import Pizza, Topping

admin.site.register(Pizza)
admin.site.register(Topping)
