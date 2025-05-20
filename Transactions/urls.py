

from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from . import views

urlpatterns = [
    path('<int:offer_id>/finalization', views.finalization, name='finalization'),
    path('finalization/<int:transaction_id>/delete-transaction', views.delete_transaction, name='delete_transaction'),
    path('finalization/<int:transaction_id>/credit-card', views.finalization_credit, name='finalization_credit'),
    path('finalization/<int:transaction_id>/bank-transafer', views.finalization_bank, name='finalization_bank'),
    path('finalization/<int:transaction_id>/mortgage', views.finalization_mortgage, name='finalization_mortgage'),
    path('finalization/<int:transaction_id>/revision/<str:paymentmethod>', views.finalization_revision, name='finalization_revision'),
    path('finalization/<int:transaction_id>/success', views.finalization_success, name='finalization_success'),
]