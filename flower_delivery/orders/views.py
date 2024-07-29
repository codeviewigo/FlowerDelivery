from django.shortcuts import render
from .models import Order


def orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/orders.html', {'orders': orders})
