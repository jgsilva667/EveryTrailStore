from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, 
         name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail,
         name='product_detail'),

    path('users/', include('users.urls',)),
    path('users/', include('django.contrib.auth.urls')),
]