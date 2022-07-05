from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# customer/user page
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


# menu page
class Menu(models.Model):

    CATEGORY = (
        ('Meals', 'Meals'),
        ('Desserts', 'Desserts'),
        ('Drinks', 'Drinks'),
    )

    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000, null=False, blank=False)
    image = CloudinaryField('image', default='placeholder')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ManyToManyField(
        'Category',
        related_name='item',
        choices=CATEGORY
    )

    def __str__(self):
        return self.name


# menu page
class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


# cart page and customer/user page
class Order(models.Model):

    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )
    
    customer = models.ForeignKey(
        Customer,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    menu = models.ForeignKey(
        Menu,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id) 
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


# cart page
class OrderItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    data_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.menu.price * self.quantity
        return total


# cart page
class OrderModel(models.Model):

    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )

    created_on = models.DateTimeField(auto_now_add=True, null=True)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    eircode = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id) 
