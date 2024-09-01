from django.db import models

from django.urls import reverse

from django.contrib.auth.models import User






class Profile(models.Model):

    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name='profiles')
    
    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

    image = models.ImageField(upload_to='%Y/%m/%d/')

    def __str__(self):
        return f'Profile to {self.user.username}'
    