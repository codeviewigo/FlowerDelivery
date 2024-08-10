# cart/views.py

from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from catalog.models import Product
from .cart import Cart
import json

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product)
    return redirect('cart:cart_detail')

@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

@require_POST
def cart_update(request):
    cart = Cart(request)
    data = json.loads(request.body)
    product_id = data.get('product_id')
    action = data.get('action')
    product = get_object_or_404(Product, id=product_id)

    if action == 'increase':
        cart.add(product=product, quantity=1)
    elif action == 'decrease':
        cart.add(product=product, quantity=-1)
    elif action == 'remove':
        cart.remove(product)

    return JsonResponse({'status': 'ok'})

@require_POST
def cart_add_with_quantity(request):
    cart = Cart(request)
    data = json.loads(request.body)
    product_id = data.get('product_id')
    quantity = data.get('quantity')
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product, quantity=quantity)
    return JsonResponse({'status': 'ok'})
