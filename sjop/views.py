from django.shortcuts import render,get_object_or_404,redirect, HttpResponse
from django.views.generic.edit import UpdateView,CreateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.base import View
from cart.forms import ProductCartFormAdd
from django.urls import reverse_lazy
from orders.models import Order
from django.contrib import messages
from django.db import IntegrityError
from .models import *
from .forms import *




class ProductStoreUserMixin(ListView):
    model = Product
    fields = ['name','description','price','available']
    success_url = reverse_lazy('')

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)


class ProductStoreManageView(ProductStoreUserMixin,ListView):

    template_name = 'product/list_product_store.html'


class ProductStoreEditMixin(ProductStoreUserMixin):
    template_name = 'product/form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProductStoreUser(ProductStoreUserMixin,ListView,LoginRequiredMixin):
    pass


class ProductStoreUpdate(ProductStoreEditMixin,UpdateView):

    pass


class ProductStoreDeleteView(ProductStoreUserMixin,DeleteView):

    template_name = 'product/delete.html'


class ProductCreateView(ProductStoreEditMixin,CreateView):

    pass









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




@login_required
def create_store(request):

    if request.method=='POST':

        form = StoreCreateForm(request.POST,files=request.FILES)

        if form.is_valid():

            store = form.save(commit=False)

            store.user = request.user

            store.save()

            return redirect('shop:product')
        

    else:

        form = StoreCreateForm()

    return render(request,'product/includes/form_create_store.html',{'form':form})



@login_required
def create_product(request):

    if request.method=='POST':

        form = ProductForm(request.POST)

        if form.is_valid():

            product = form.save(commit=False)

            product.store = request.user_market_shop

            product.save()
        
        return redirect('shop:product')
    

    else:

        form = ProductForm()

    return render(request,'product/includes/form_create_product.html',{'form':form})



@login_required
def store_list(request):

    store = MarketShop.objects.all()

    return render(request,'product/list_store.html',{'store':store})

@login_required
def store_detail(request,id,slug):

    store = get_object_or_404(MarketShop,id=id,slug=slug)

    return render(request,'product/detail_store.html',{'store':store})

