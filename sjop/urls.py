from django.urls import path

from .import views


app_name = 'shop'

urlpatterns = [

    path('',views.product_list,name='product'),
    path('category/<slug:category_slug>/',views.product_list,name='product_category'),
    path('<int:id>/<slug:slug>/',views.product_detail,name='product_detail'),
    path('<int:id>/<slug:slug>/rating-product/', views.review_user_by_product, name='rating_product'),
    path('create-store/',views.create_store,name='create_market'),
    path('list-store',views.store_list,name='store-list'),
    path('store-detail<int:store_id>/',views.ProductStoreManageView.as_view(),name='product_store_detail'),
    path('create-product-store/',views.ProductCreateView.as_view(),name='create_product_from'),
    path('update-product/<int:pk>/<int:store_id>/',views.StoreProductUpdateView.as_view(), name='image_product_update'),
   

]
