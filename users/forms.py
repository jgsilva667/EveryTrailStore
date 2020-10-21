from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomerCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('first_name','last_name', 'username',  'email','address', 'city', 'state', 'zipcode', 'phone_number')


class CustomerChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('first_name','last_name', 'username',  'email', 'password','address', 'city', 'state', 'zipcode', 'phone_number')