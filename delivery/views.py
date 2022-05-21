from django.shortcuts import render
from django.views import View
from .models import Menu

class Main(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class MenuItem(View):
    model = Menu

    def get(self, request, *args, **kwargs):
       
        menus = Menu.objects.all()

        context = {
            'menus': menus
        }

        return render(request, 'menu.html', context)
 

class Cart(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'cart.html')
