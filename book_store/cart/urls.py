from django.urls import path
from . import views

urlpatterns = [
    path('cart',views.cart,name='cart'),
    path('add/<int:books_id>/', views.add_cart, name='addcart'),
    path('cart_decrement/<int:books_id>/',views.min_cart, name='cart_decrement'),
    path('remove/<int:books_id>/',views.cart_delete, name='remove'),
    path('checkout',views.Checkout,name='checkout'),
    path('bank',views.bank,name='bank'),
    path('pay/', views.pay, name='paymenthandler'),
]