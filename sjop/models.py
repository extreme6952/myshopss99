from django.db import models

from django.urls import reverse

from easy_thumbnails.fields import ThumbnailerImageField

from django.contrib.auth.models import User

from django.core.validators import MinValueValidator,MaxValueValidator

from django.utils import timezone

from django.utils.text import slugify

from .fields import OrderField

from unidecode import unidecode



class Category(models.Model):
    name = models.CharField(max_length=250)

    slug = models.CharField(max_length=250,
                            unique=True)

    class Meta:
        ordering = ['name']

        indexes = [
            models.Index(fields=['name'])
        ]

        verbose_name = 'Категория'

        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse(
            "shop:product_category", args=[
                self.slug
            ]
        )


class CategoryMarketShop(models.Model):

    name = models.CharField(max_length=250,unique=True)

    slug = models.SlugField(max_length=250,unique=True)

    class Meta:

        ordering = ['name']

        indexes = [
            models.Index(fields=['name'])
        ]

        verbose_name = 'Категории магазинов'

        verbose_name_plural = 'Категория магазина'

    def __str__(self):
        return self.name
    

class MarketShop(models.Model):

    user = models.OneToOneField(User,
                                on_delete=models.PROTECT,
                                related_name='user_market_shop')
    
    category = models.ForeignKey(CategoryMarketShop,
                                 on_delete=models.CASCADE,
                                 related_name='category_shop',
                                 null=True,
                                 blank=True)

    name = models.CharField(max_length=250,unique=True)   

    slug = models.SlugField(max_length=250,unique=True,blank=True)

    created = models.DateTimeField(auto_now_add=True)

    description = models.TextField(blank=True)

    image = models.ImageField(upload_to='%D/%m/y',blank=True)

    class Meta:

        ordering = ['-user']


    def __str__(self,):

        return  self.name
    

    def save(self,*args, **kwargs):

        if not self.slug:

            self.slug = slugify(unidecode(self.name)) 

        super().save(*args, **kwargs)

    
    def get_absolute_url(self):
        return reverse("shop:detail_store", args=[self.id,self.slug])
    


class Product(models.Model):

    store = models.ForeignKey(MarketShop,on_delete=models.SET_NULL,null=True,blank=True)

    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 related_name='products')

    name = models.CharField(max_length=250)

    slug = models.CharField(max_length=250)

    description = models.TextField(blank=True)

    price = models.DecimalField(max_digits=10,
                                decimal_places=2)

    available = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

    order_field = OrderField(blank=True,for_fields=['category'])

    class Meta:
        ordering = ['name']

        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created'])
        ]

    def __str__(self):
        return f"Товар №{self.id}. Имя товара {self.name}"

    def get_absolute_url(self):
        return reverse("shop:product_detail", args=[self.id,
                                                    self.slug])


class ImageByproduct(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='images')

    image = ThumbnailerImageField(upload_to='product/%Y/%m/%d',
                                  resize_source=dict(quality=95,
                                                     size=(1368, 720),
                                                     sharpen=True),
                                  blank=True,
                                  null=True)



class Rating(models.Model):

    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='stars_product')
    
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    
    stars = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )

    text = models.TextField(blank=True)

    created = models.DateTimeField(auto_now_add=True)

    active = models.BooleanField(default=True)

    class Meta:
        
        ordering = ['-product']

        indexes = [
            models.Index(fields=[
                'product'
            ])
        ]

        unique_together = ['product', 'user']


    def __str__(self):
        return f"Рейтинг товара {self.product} на {self.stars}"
    

