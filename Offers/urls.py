from django.urls import path
from . import views

urlpatterns = [

    #path('',views.index, name='offer-index'),

    path('<int:listing_id>/create_offer',views.create_offer,name='create-offer'),

    path('delete_offer/<int:id>',views.delete_offer,name='delete-offer'),

    path('update_offer/<int:id>', views.update_offer, name='update-offer'),
]