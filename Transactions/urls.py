

from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from . import views

urlpatterns = [
    path('buyer/my_offers/finalization', views.finalization, name='finalization'),
    path('buyer/my_offers/finalization/credit-card', views.finalization_credit, name='finalization_credit'),
    path('buyer/my_offers/finalization/bank-transafer', views.finalization_bank, name='finalization_bank'),
    path('buyer/my_offers/finalization/mortgage', views.finalization_mortgage, name='finalization_mortgage'),
    path('buyer/my_offers/finalization/revision', views.finalization_revision, name='finalization_revision'),
    path('buyer/my_offers/finalization/success', views.finalization_success, name='finalization_success'),
]