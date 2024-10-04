from django.shortcuts import render, get_object_or_404, redirect

from django.urls import reverse

from django.contrib import messages

from cart.cart import Cart

from .forms import *

from .models import *

from .tasks import order_created as order_created_celery

from django.contrib.auth.decorators import login_required

from datetime import datetime







@login_required
def order_create(request):

    cart = Cart(request)

    if request.method=='POST':

        form = OrderForm(request.POST)

        if form.is_valid():

            order = form.save(commit=False)

            order.user = request.user

            order.save()

            for product in cart:

                OrderItem.objects.create(order=order,
                                         product=product['product'],
                                         quantity=product['quantity'],
                                         price=product['price'])
                

            cart.clear()

            order_created_celery.delay(order.id)
            
            request.session['order_id'] = order.id

            messages.success(request,'Ваш заказ успешно создан и оплачен')

            return redirect(reverse('payment:process'))

            
    
    else:

        form = OrderForm()

    return render(
        request,
        'order/order_create.html',
        {
            'cart':cart,
            'form':form
        }
    )
            


