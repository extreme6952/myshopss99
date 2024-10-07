from django.db import models

from django.contrib.auth.models import User

from django.urls import reverse

from django.utils import timezone

from sjop.models import Product

from decimal import Decimal

from coupens.models import Coupone

from django.core.validators import MinValueValidator,MaxValueValidator


class Order(models.Model):

    coupon = models.ForeignKey(Coupone,
                               on_delete=models.SET_NULL,
                               related_name='coupons_in_orders',
                               blank=True,
                               null=True)
    
    discount = models.IntegerField(validators=[
        MinValueValidator(0),
        MaxValueValidator(100)
    ],
    default=0)
    

    user = models.ForeignKey(User,
                             on_delete=models.PROTECT,
                             related_name='orders')
    
    city = models.CharField(max_length=250)

    postal_code = models.CharField(max_length=250)

    address = models.CharField(max_length=250)

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now_add=True)

    paid = models.BooleanField(default=False)

    payment_link = models.URLField(blank=True,null=True)

    stripe_id = models.CharField(max_length=250,blank=True)


    class Meta:

        ordering = ['-created']

        indexes = [
            models.Index(fields=['-created'])
        ]


    def get_total_cost_before_discount(self):

        return sum(item.get_cost() for item in self.orders.all())


    def get_discount(self):

        total_cost = self.get_total_cost_before_discount()

        if self.discount:

            return total_cost * (self.discount / Decimal(100))
        
        return Decimal(0)
    

    def get_total_cost(self):

        total_cost = self.get_total_cost_before_discount()

        return total_cost - self.get_discount()

    def __str__(self):
        return f"Заказ {self.id}"
    
    
    



class OrderItem(models.Model):

    order = models.ForeignKey(Order,
                              on_delete=models.CASCADE,
                              related_name='orders')
    
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='product')
    
    price = models.DecimalField(max_digits=10,
                                decimal_places=2)
    
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        
        return str(self.id)
    

    def get_cost(self):

        return self.price * self.quantity
    