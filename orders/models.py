from django.db import models

from django.contrib.auth.models import User

from django.urls import reverse

from django.utils import timezone

from sjop.models import Product




class Order(models.Model):

    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='orders')
    
    city = models.CharField(max_length=250)

    postal_code = models.CharField(max_length=250)

    address = models.CharField(max_length=250)

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now_add=True)

    paid = models.BooleanField(default=False)


    class Meta:

        ordering = ['-created']

        indexes = [
            models.Index(fields=['-created'])
        ]


    def __str__(self):
        return f"Заказ {self.id}"
    
    def get_total_cost(self):

        return sum(item.get_cost() for item in self.order.all())
    



class OrderItem(models.Model):

    order = models.ForeignKey(Order,
                              on_delete=models.CASCADE,
                              related_name='order')
    
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
    