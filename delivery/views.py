from django.shortcuts import render
from django.views import View

class Main(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class Menu(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'menu.html')


class Cart(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'cart.html')
