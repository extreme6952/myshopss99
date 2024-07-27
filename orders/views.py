from django.shortcuts import render, get_object_or_404, redirect

from django.urls import reverse

from cart.cart import Cart

from .forms import *

from .models import *

from .tasks import order_created as order_created_celery


def order_created(request):
    cart = Cart(request)

    if request.method == 'POST':

        form = OrderForm(data=request.POST)

        if form.is_valid():
            order = form.save()

            for item in cart:

                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )

            cart.clear()

            return render(
                request,
                'order/success.html',
                {'order':order}
            )
        
    else:

        form = OrderForm()

    return render(
        request,
        'order/order_create.html',
        {'form':form}
    )