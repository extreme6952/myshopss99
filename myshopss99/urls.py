from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/',include('cart.urls',namespace='cart')),
    path('orders/',include('orders.urls',namespace='order')),
    path("payment/", include('payment.urls'), name="payment"),
    path('',include('account.urls')),
    path('',include('sjop.urls',namespace='shop')),
]+static(settings.MEDIA_URL, 
         document_root=settings.MEDIA_ROOT)
