from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import Menu, Order, OrderItem
import json
import datetime

class Main(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            customer = request.user.customer
            order, created = Order.objects.get_or_create(
                customer=customer,
                complete=False
            )
            items = order.orderitem_set.all()
            cartItems = order.get_cart_items
        else:
            items = []
            order = {'get_cart_total': 0, 'get_cart_item':0 }
            #cartItems = order['get_cart_items']
        
        # context = {
        #     'cartItems': cartItems
        # }

        return render(request, 'index.html')


class MenuItem(View):
    model = Menu

    def get(self, request, *args, **kwargs):
       
        meals = Menu.objects.filter(category__name__contains='Meals')
        desserts = Menu.objects.filter(category__name__contains='Desserts')
        drinks = Menu.objects.filter(category__name__contains='Drinks')

        if request.user.is_authenticated:
            customer = request.user.customer
            order, created = Order.objects.get_or_create(
                customer=customer,
                complete=False
            )
            items = order.orderitem_set.all()
            # cartItems = order.get_cart_items
        else:
            items = []
            order = {'get_cart_total': 0, 'get_cart_item':0 }
            # cartItems = order['get_cart_items']

        context = {
            'meals': meals,
            'desserts': desserts,
            'drinks': drinks,
            # 'cartItems': cartItems
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
            # cartItems = order.get_cart_items
        else:
            items = []
            order = {'get_cart_total': 0, 'get_cart_item':0 }
            # cartItems = order['get_cart_items']
        
        context = {
            'items': items,
            'order': order,
            # 'cartItems': cartItems
        }

        return render(request, 'cart.html', context)


class UpdateCart(View):

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        menuId = data['menuId'] 
        action = data['action']

        print('action:', action)
        print('menuId:', menuId)

        # first_name = request.POST.get('first_name')
        # last_name = request.POST.get('last_name')
        # address = request.POST.get('address')
        # email = request.POST.get('email')
        # phone = request.POST.get('phone')
        # message = request.POST.get('message')

        customer = request.user.customer
        menu = Menu.objects.get(id=menuId)
        order, created = Order.objects.get_or_create(
            customer=customer,
            complete=False,
            # first_name=first_name,
            # last_name=last_name,
            # address=address,
            # email=email,
            # phone=phone,
            # message=message
        )

        orderItem, created = OrderItem.objects.get_or_create(
            order=order,
            menu=menu
        )

        if action == 'add':
            orderItem.quantity = (orderItem.quantity + 1)
        elif action == 'remove':
            orderItem.quantity = (orderItem.quantity - 1)

        orderItem.save()
        
        if orderItem.quantity <= 0:
            orderItem.delete()

        return JsonResponse('Item was added', safe=False)

class OrderConfirmation(View):

    def get(self, request, pk, *args, **kwargs):
        order = Menu.objects.get(pk=pk)

        context = {
            'pk': order.pk,
            'price': order.price
        }
        return render(request, 'order_confirmation.html', context)

    def post(self, request, pk, *args, **kwargs):
        print(request.body)


class OrderPayConfirmation(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'order-pay-confirmation.html')