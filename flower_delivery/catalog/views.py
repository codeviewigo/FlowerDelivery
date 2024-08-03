from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Product


def catalog(request):
    products = Product.objects.all()
    paginator = Paginator(products, 6)  # Показать 10 товаров на странице

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'catalog/catalog.html', {'page_obj': page_obj})

def product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'catalog/product.html', {'product': product})