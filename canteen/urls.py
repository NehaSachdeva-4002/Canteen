from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='canteen-home'),
    path('add-to-cart/<int:item_id>/', views.add_to_cart, name='add-to-cart')
]