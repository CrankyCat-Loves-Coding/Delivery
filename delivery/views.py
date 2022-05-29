from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import Menu, Order, OrderItem
import json

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
    model = Order
    model = OrderItem

    def get(self, request, *args, **kwargs): 

        if request.user.is_authenticated:
            customer = request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            items = order.orderitem_set.all()
        else:
            items = []
            order = {'get_cart_total': 0, 'get_cart_item':0 }
        
        context = {
            'items': items,
            'order': order
        }

        return render(request, 'cart.html', context)


class UpdateItem(View):

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        menuId = data['menuId']
        action = data['action']

        print('action:', action)
        print('menuId:', menuId)
        return JsonResponse('Item was added', safe=False)