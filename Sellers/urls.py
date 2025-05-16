from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from . import views

urlpatterns = [
    path('seller/home/', views.seller_home, name='seller_home'),
    path('seller/offers/', views.seller_offers, name='seller_offers'),
    path('seller/listings/', views.seller_listings, name='seller_listings'),
    path('seller/listings/create/', views.seller_add_listing, name='seller_add_listing'),
    path('seller/listing/listingId/', views.seller_edit_listing, name='seller_edit_listing'),
    path('seller/profile/', views.seller_profile, name='seller_profile'),
    path('seller/login', LoginView.as_view(template_name='seller/seller_login.html'), name='login_as_seller'),
    path('seller/logout', LogoutView.as_view(next_page='index'), name='logout'),
    path('seller/register', views.seller_register, name='register_as_seller'),

]