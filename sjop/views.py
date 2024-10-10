from django.shortcuts import render,get_object_or_404,redirect, HttpResponse

from django.views.decorators.http import require_POST

from .models import *

from cart.forms import ProductCartFormAdd

from django.contrib.auth.decorators import login_required

from orders.models import Order

from django.contrib import messages

from django.db import IntegrityError

from .forms import *







def product_list(request,category_slug=None):

    product = Product.objects.filter(available=True)

    categories = Category.objects.all()
    
    category = None


    if category_slug:

        category = get_object_or_404(Category,
                                     slug=category_slug)
        
        product = product.filter(category=category)

    return render(
        request,
        'product/product.html',
        {
            'categories':categories,
            'product':product,
            'category':category
         }
    )


def product_detail(request,id,slug):

    product = get_object_or_404(Product,
                                available=True,
                                id=id,
                                slug=slug)
    
    image = ImageByproduct.objects.filter(product=product)

    cart_add_form_product = ProductCartFormAdd()
    
    form = RatingModelForm()

    ratings = product.stars_product.filter(active=True)

    return render(
        request,
        'product/detail.html',
        {
        'product':product,
        'image':image,
        'cart_add_form':cart_add_form_product,
        'form':form,
        'ratings':ratings
         }
    )
    


@login_required
@require_POST
def review_user_by_product(request, id,slug):

    product = get_object_or_404(Product, id=id,slug=slug,available=True)


    # Check if user has purchased the product
    # if not Order.objects.filter(user=request.user, product=product).exists():
    #     return HttpResponse('Вы должны купить товар, чтобы оставить отзыв.')

    form = RatingModelForm(data=request.POST)

    try:

        if form.is_valid():
            # Create a new Rating object with cleaned data
            Rating.objects.create(
                user=request.user,
                product=product,
                stars=form.cleaned_data['stars'],
                text=form.cleaned_data['text']
            )
            messages.success(request, 'Ваш отзыв успешно добавлен.')

            return redirect(product.get_absolute_url())
        else:

            messages.error(request, 'При заполнении данных произошла ошибка.')

    except IntegrityError:

        messages.error(request,'Больше чем один отзыв добавлять нельзя.')

        return redirect(product.get_absolute_url())

    return render(request, 'product/includes/rating_form.html', {
        'product': product,
        'form': form
    })