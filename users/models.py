from django.contrib.auth.models import AbstractUser
from django.contrib.auth import validators
from django.template.backends import django
from django.utils import timezone
from django.db import models



class CustomUser(AbstractUser):
    username = models.CharField(error_messages={'unique': 'A user with that username already exists.'},
                                  help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
                                  max_length=150, unique=True,
                                  validators=[validators.UnicodeUsernameValidator()],
                                  verbose_name='username')
    first_name = models.CharField(blank=True, max_length=150, verbose_name='first name')
    last_name = models.CharField(blank=True, max_length=150, verbose_name='last name')
    email = models.EmailField(blank=True, max_length=254, verbose_name='email address')
    password = models.CharField(max_length=128, verbose_name='password')
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=50)
    updated_date = models.DateTimeField(auto_now_add=True)

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.cust_name)