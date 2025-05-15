from django.urls import path
from . import views

urlpatterns = [
    path('seller/home/', views.seller_home, name='seller_home'),
    path('seller/offers/', views.seller_offers, name='seller_offers'),
    path('seller/listings/', views.seller_listings, name='seller_listings'),
    path('seller/listings/create/', views.seller_add_listing, name='seller_add_listing'),
    path('seller/listing/listingId/', views.seller_edit_listing, name='seller_edit_listing'),
    path('seller/profile/', views.seller_profile, name='seller_profile'),
]