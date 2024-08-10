from datetime import date

from asgiref.sync import sync_to_async, async_to_sync
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from .models import Order
# from telegram_bot.bot import send_order_notification
import asyncio

from telegram_bot.bot import send_order_notification


@login_required
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )

            send_order_notification(order, cart)
            cart.clear()

            return render(request, 'orders/order_created.html', {'order': order})
    else:
        form = OrderCreateForm()

    return render(request, 'orders/order_create.html', {'cart': cart, 'form': form})


@login_required
def user_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/user_orders.html', {'orders': orders})


@login_required
def user_orders_detail(request, pk):
    order = Order.objects.filter(user=request.user).get(pk=pk)
    order_items = OrderItem.objects.filter(order=order)
    context = {
        'order': order,
        'order_items': order_items
    }

    return render(request, 'orders/user_orders_detail.html', context=context)
