from django.shortcuts import render


def home(request):
    return render(request, 'main/home.html')


def about(request):
    return render(request, 'main/contacts.html')


def delivery(request):
    return render(request, 'main/delivery.html')
