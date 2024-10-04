from django.db import models

from django.core.validators import MaxValueValidator,MinValueValidator




class Coupone(models.Model):

    code = models.CharField(max_length=250)

    valid_from = models.DateTimeField()

    valid_to = models.DateTimeField()

    discount = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100),
        ],
        help_text='Процентное соотношение скидки'
    )

    active = models.BooleanField(default=False)


    def __str__(self):
        return self.code
    
    
    