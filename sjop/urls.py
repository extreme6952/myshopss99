from django.urls import path

from .import views


app_name = 'shop'

urlpatterns = [

    path('',views.product_list,name='product'),
    path('category/<slug:category_slug>/',views.product_list,name='product_category'),
    path('<int:id>/<slug:slug>/',views.product_detail,name='product_detail'),

]
