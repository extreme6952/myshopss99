from django.db import models

from django.urls import reverse

from easy_thumbnails.fields import ThumbnailerImageField

from django.contrib.auth.models import User


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


# class Profile(models.Model):

#     user = models.ForeignKey(User)


class Product(models.Model):
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
