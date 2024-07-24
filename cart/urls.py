from django.urls import path

from . import views

app_name = 'cart'


urlpatterns = [
    path('add/<int:product_id>/',views.cart_product_add,name="add_product_cart"),
    path('cart_detail/',views.cart_detail,name="cart_detail")
]