from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View
from .models import Menu, Order, OrderItem, OrderModel, Customer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm
from django.contrib import messages
import json


class RegisterPage(View):
    def get(self, request, *args, **kwargs):
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
            
                return redirect('login')
        else:
            form = UserCreationForm()

        context = {
            'form': form
        }
        return render(request, 'accounts/signup.html', context)


class LoginPage(View):
    def get(self, request, *args, **kwargs):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(
                request,
                username=username,
                password=password
            )

            if user is not None:
                login(request, user)
                return redirect('index')

        context = {

        }
        return render(request, 'accounts/login.html', context)



class Customer(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'customer.html')


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


# class OrderView(View):

#     def post(self, request, *args, **kwargs):
#         full_name = request.POST.get('full_name')
#         phone = request.POST.get('phone')
#         email = request.POST.get('email')
#         address = request.POST.get('address')
#         eircode = request.POST.get('eircode')
#         message = request.POST.get('message')

#         context = {
#             'full_name': full_name,
#             'phone': phone,
#             'email': email,
#             'address': address,
#             'eircode': eircode,
#             'message': message,
#         }
#         return render(request, 'cart.html', context)


class Cart(View):
    model = Order
    model = OrderItem
    model = OrderModel

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

    def post(self, request, *args, **kwargs):
        full_name = request.POST.get('full_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        eircode = request.POST.get('eircode')
        message = request.POST.get('message')

        order = OrderModel.objects.create (
            full_name=full_name,
            phone=phone,
            email=email,
            address=address,
            eircode=eircode,
            message=message,
        )

        return render(request, 'cart.html')


class UpdateCart(View):

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        menuId = data['menuId'] 
        action = data['action']

        print('action:', action)
        print('menuId:', menuId)

        customer = request.user.customer
        menu = Menu.objects.get(id=menuId)
        order, created = Order.objects.get_or_create(
            customer=customer,
            complete=False,
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


