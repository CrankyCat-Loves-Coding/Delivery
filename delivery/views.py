from django.shortcuts import render
from django.views import View
from .models import Menu, Order, OrderItem

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
        
        context = {
            'items': items,
            'order': order
        }

        return render(request, 'cart.html', context)
