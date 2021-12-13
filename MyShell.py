import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Pizzeria.settings")

import django
django.setup()

from pizzas.models import Pizza, Topping

pizzas = Pizza.objects.all()
for pizza in pizzas:
    print(pizza.id, pizza)

toppings = Topping.objects.all()
for topping in toppings:
    print(topping)

from django.contrib.auth.models import User

for user in User.objects.all():
    print(user.username, user.id)