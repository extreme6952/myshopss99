from django.shortcuts import render, get_object_or_404, redirect

from django.views.decorators.http import require_POST

from .forms import ProductCartFormAdd

from .cart import Cart

from sjop.models import Product

from sjop.models import ImageByproduct


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


def cart_detail(request):
    cart = Cart(request)

    images = {}

    for item in cart:
        product = item['product']

        product_images = ImageByproduct.objects.filter(product=product)

        images[product.id] = product_images

    return render(
        request,
        'cart/cart_detail.html',
        {
            'cart': cart,
            'images': images

        }
    )
