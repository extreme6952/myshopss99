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
    path('detail-store/<int:id>/<slug:slug>/',views.store_detail,name='detail_store'),
    path('store-detail/',views.ProductStoreManageView.as_view(),name='product_store_detail')
]
