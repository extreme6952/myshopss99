from django.shortcuts import render,redirect,get_object_or_404

from django.urls import reverse

from django.conf import settings

from orders.models import OrderItem,Order

from cart.cart import Cart

from decimal import Decimal

import stripe


stripe.api_key = settings.STRIPE_SECRET_KEY

stripe.api_version = settings.STRIPE_API_VERSION





def payment_process(request):

    order_id = request.session.get('order_id',None)

    order = get_object_or_404(Order,id=order_id)


    if request.method=='POST':

        success_url = request.build_absolute_uri(
            reverse('payment:completed')
        )

        canceled_url = request.build_absolute_uri(
            reverse('payment:cancel')
        )


        session_data = {
            'mode':'payment',
            'success_url':success_url,
            'cancel_url':canceled_url,
            'client_reference_id':order_id,
            'line_items':[]
        }


        for item in order.orders.all():

            session_data['line_items'].append({
                'price_data':{
                    'unit_amount':int(item.price * Decimal('100')),
                    'currency':'rub',
                    'product_data':{
                        'name':item.product.name
                    }
                },
                
                'quantity':item.quantity

            })

        session= stripe.checkout.Session.create(**session_data)

        return redirect(session.url,code=303)
    
    else:

        return render(
            request,
            'payment/process.html',
            locals()
        )
    

def payment_cancel(request):

    return render(
        request,
        'payment/cancel.html',
        locals()
    )


def payment_success(request):

    return render(
        request,
        'payment/success.html',
        locals()
    )