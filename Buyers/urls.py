from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('buyer/home/', views.buyer_home, name='buyer_home'),
    path('buyer/catalogue/', views.buyer_catalogue, name='buyer_catalogue'),
    path('buyer/my_offers/', views.my_offers, name='my_offers'),
    path('buyer/my_offers/finalization', views.finalization, name='finalization'),
    path('buyer/my_offers/finalization/revision', views.finalization_revision, name='finalization_revision'),
    path('buyer/my_offers/finalization/success', views.finalization_success, name='finalization_success'),
    path('buyer/profile/', views.buyer_profile, name='buyer_profile'),
]