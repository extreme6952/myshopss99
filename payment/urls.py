from django.urls import path

from . import views

from .webhooks import webhook_stripe


app_name = 'payment'


urlpatterns = [
    path('process/',views.payment_process,name='process'),
    path('completed/',views.payment_success,name='completed'),
    path('cancel/',views.payment_cancel,name='cancel'),
    path('stripe-webhook/',webhook_stripe,name='stripe-webhook'),

]
