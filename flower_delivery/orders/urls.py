from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('user_orders/', views.user_orders, name='user_orders'),
    path('user_orders_detail/<int:pk>/', views.user_orders_detail, name='user_orders_detail'),
]
