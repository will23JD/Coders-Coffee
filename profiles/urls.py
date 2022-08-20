from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    path('wishlist', views.wishlist, name='wishlist'),
    path('add/<item_id>', views.add_to_wishlist, name='add_to_wishlist'),
    path('delete/<int:item_id>/', views.delete_from_wishlist, name='delete_from_wishlist'),
]
