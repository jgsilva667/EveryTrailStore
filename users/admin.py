from .models import CustomUser
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomerCreationForm
from. forms import CustomerChangeForm


#list, search, filter and edit customer details
class CustomerAdmin(admin.ModelAdmin):
    add_form = CustomerCreationForm
    form = CustomerChangeForm
    model = CustomUser
    list_display = ['first_name', 'last_name','email', 'state', 'phone_number']
    list_filter = ('last_name', 'state')
    search_fields = ('last_name',)
    ordering = ['last_name']



admin.site.register(CustomUser, CustomerAdmin)