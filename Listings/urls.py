from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.catalogue, name='catalogue'),
    path('<int:id>', views.get_listing_by_id, name='listing-by-id'),
]