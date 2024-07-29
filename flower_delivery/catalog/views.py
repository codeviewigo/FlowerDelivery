from django.shortcuts import render
from .models import Product


def catalog(request):
    products = Product.objects.all()
    return render(request, 'catalog/catalog.html', {'products': products})
