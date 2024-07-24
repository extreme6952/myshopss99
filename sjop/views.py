from django.shortcuts import render,get_object_or_404,redirect

from django.views.decorators.http import require_POST

from .models import *

from cart.forms import ProductCartFormAdd

def product_list(request,category_slug=None):


    product = Product.objects.filter(available=True)

    categories = Category.objects.all()
    
    category = None


    if category_slug:

        category = get_object_or_404(Category,
                                     slug=category_slug)
        
        product.filter(category=category)

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
    
    return render(
        request,
        'product/detail.html',
        {
        'product':product,
        'image':image,
        'cart_add_form':cart_add_form_product
         }
    )
    



