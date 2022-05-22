from django.shortcuts import render
from django.views import View
from .models import Menu

class Main(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class MenuItem(View):
    model = Menu

    def get(self, request, *args, **kwargs):
       
        meals = Menu.objects.filter(category__name__contains='Meals')
        desserts = Menu.objects.filter(category__name__contains='Desserts')
        drinks = Menu.objects.filter(category__name__contains='Drinks')

        context = {
            'meals': meals,
            'desserts': desserts,
            'drinks': drinks,
        }

        return render(request, 'menu.html', context)
 

class Cart(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'cart.html')
