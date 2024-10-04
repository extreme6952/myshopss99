from sjop.models import Product

from decimal import Decimal

from django.conf import settings

from coupens.models import Coupone

class Cart:

    def __init__(self, request):

        self.session = request.session

        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart

        self.coupone_id = request.session.get('coupone_id')


    def __iter__(self):

        product_ids = self.cart.keys()

        products = Product.objects.filter(id__in=product_ids)

        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])

            item['total_price'] = item['price'] * item['quantity']

            yield item

    def __len__(self):

        return sum(item['quantity'] for item in self.cart.values())

    def add(self, product, quantity=1, override_quantity=False):

        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {'price': str(product.price),
                                     'quantity': 0}

        if override_quantity:

            self.cart[product_id]['quantity'] = quantity

        else:

            self.cart[product_id]['quantity'] += quantity

        self.save()

    def save(self):

        self.session.modified = True

    def remove(self, product):

        product_id = str(product.id)

        if product_id in self.cart:
            del self.cart[product_id]

            self.save()

    def clear(self):

        del self.session[settings.CART_SESSION_ID]

        self.save()

    def get_total_price(self):

        return sum(item['quantity'] * Decimal(item['price']) for item in self.cart.values())
    

    @property
    def coupon(self):

        if self.coupone_id:

            try:

                return Coupone.objects.get(id=self.coupone_id)
            
            except Coupone.DoesNotExist:

                pass

        return None
    


    def get_discount(self):

        if self.coupone_id:

            discount_value = (self.coupon.discount / Decimal(100)) * self.get_total_price()

            return discount_value

        
        return Decimal(0)
    

    def get_total_price_apply_discount(self):

        return self.get_total_price() - self.get_discount()

        