from django.urls import path

from . import views


app_name = 'order'


urlpatterns = [
    
    path('order-create/',views.order_create,name='order_create'),
    path('admin/order/<int:order_id>/',views.admin_order_detail,name='admin_order_detail')

]
