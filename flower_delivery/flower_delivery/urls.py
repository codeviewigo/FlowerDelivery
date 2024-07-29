from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    path('registration/', include('registration.urls')),
    path('catalog/', include('catalog.urls')),
    path('orders/', include('orders.urls')),

]
