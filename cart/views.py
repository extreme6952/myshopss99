from django.shortcuts import render, get_object_or_404, redirect

from django.views.decorators.http import require_POST

from sjop.models import Product

from .cart import Cart

from .forms import ProductCartFormAdd

from coupens.forms import CouponeForm

@require_POST
def cart_product_add(request, product_id):
    cart = Cart(request)

    product = get_object_or_404(Product,
                                id=product_id)

    form = ProductCartFormAdd(request.POST)

    if form.is_valid():
        cd = form.cleaned_data

        cart.add(
            product=product,
            quantity=cd['quantity'],
            override_quantity=['override']
        )

    return redirect('cart:cart_detail')


@require_POST
def cart_remove_product(request, product_id):
    cart = Cart(request)

    product = get_object_or_404(Product,
                                id=product_id)

    cart.remove(product=product)

    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)

    for item in cart:
        item['update_quantity_form'] = ProductCartFormAdd(
            initial={
                'quantity': item['quantity'],
                'override': True
            }
        )

    coupone_form = CouponeForm()

    return render(request,
                  'cart/cart_detail.html',
                  {
                      'cart':cart,
                      'coupone_form':coupone_form,
                  })
