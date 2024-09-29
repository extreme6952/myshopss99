import stripe

from django.conf import settings

from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt

from orders.models import Order

from .tasks import payment_send_pdf_file

import stripe.error



@csrf_exempt
def webhook_stripe(request):

    payload = request.body

    sig_header = request.META['HTTP_STRIPE_SIGNATURE']

    event = None

    try:

        event = stripe.Webhook.construct_event(
            payload,
            sig_header,
            settings.STRIPE_WEBHOOK_SECRET
        )

    except ValueError as e:

        return HttpResponse(status=400)
    
    except stripe.error.SignatureVerificationError as e:

        return HttpResponse(status=400)

    
    if event.type == 'checkout.session.completed':

        session = event.data.object

        order_id = session.client_reference_id

        if session.mode == 'payment' and session.payment_status == 'paid':

            try:

                print(f"Номер заказа нужно проверить {order_id}")

                order = Order.objects.get(id=order_id)

            except Order.DoesNotExist:

                return HttpResponse(status=404)
            
            order.paid = True

            order.stripe_id = session.payment_intent

            order.save()
            
            payment_send_pdf_file.delay(order.id)

    return HttpResponse(status=200)