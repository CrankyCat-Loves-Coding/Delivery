from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Order
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
 

class AddressForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'form'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_tag = False

    name = forms.CharField()
    phone = forms.CharField()
    email = forms.CharField()
    address = forms.CharField()
    eircode = forms.CharField()
