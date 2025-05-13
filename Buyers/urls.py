from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('buyer/register', views.register, name='register'),
    path('buyer/login', LoginView.as_view(template_name='login.html'), name='login'),
    path('buyer/logout', LogoutView.as_view(), name='logout'),

    path('buyer/home/', views.buyer_home, name='buyer_home'),
    path('buyer/catalogue/', views.buyer_catalogue, name='buyer_catalogue'),
    path('buyer/my_offers/', views.my_offers, name='my_offers'),
    path('buyer/my_offers/finalization', views.finalization, name='finalization'),
    path('buyer/my_offers/finalization/credit-card', views.finalization_credit, name='finalization_credit'),
    path('buyer/my_offers/finalization/bank-transafer', views.finalization_bank, name='finalization_bank'),
    path('buyer/my_offers/finalization/mortgage', views.finalization_mortgage, name='finalization_mortgage'),
    path('buyer/my_offers/finalization/revision', views.finalization_revision, name='finalization_revision'),
    path('buyer/my_offers/finalization/success', views.finalization_success, name='finalization_success'),
    path('buyer/profile/', views.buyer_profile, name='buyer_profile'),
]