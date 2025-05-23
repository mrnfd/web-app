"""
URL configuration for castle_apartments project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include
from . import  views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Buyers.urls')),
    path('catalogue/', include('Listings.urls')),
    path('offers/', include('Offers.urls')),
    path('transaction/', include('Transactions.urls')),
    path('login_success/', views.login_success, name='login_success'),
    path('sellers/', views.sellers, name='sellers'),
    path('sellers/<int:seller_id>/', views.seller, name='seller'),
    path('log-in/', views.log_in, name='log_in'),
    #path('log-in/buyer/', views.login_as_buyer, name='login_as_buyer'),
    #path('log-in/seller/', views.login_as_seller, name='login_as_seller'),
    path('', include('Sellers.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
