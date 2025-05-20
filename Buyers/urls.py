from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('buyer/register', views.register, name='register_as_buyer'),
    path('buyer/login', LoginView.as_view(template_name='buyers/buyer_login.html'), name='login_as_buyer'),
    path('buyer/logout', LogoutView.as_view(next_page='index'), name='logout'),
    path('buyer/home/', views.index, name='index'),
    path('buyer/catalogue/', views.buyer_catalogue, name='buyer_catalogue'),
    path('buyer/my_offers/', views.my_offers, name='my_offers'),
    path('buyer/profile/', views.buyer_profile, name='buyer_profile'),
]