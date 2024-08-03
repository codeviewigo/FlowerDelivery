# cart/context_processors.py

from .cart import Cart

def cart_context_processor(request):
    cart = Cart(request)
    return {
        'cart_items': len(cart),
        'cart_total_price': cart.get_total_price()
    }
