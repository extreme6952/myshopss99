from django import forms
from .models import *
from django.forms.models import inlineformset_factory

class RatingModelForm(forms.ModelForm):

    class Meta:

        model = Rating

        fields = ['text','stars']

    def __init__(self,*args, **kwargs):

        super(RatingModelForm,self).__init__(*args, **kwargs)

        self.fields['text'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Напишите свой отзыв'
        })

        self.fields['stars'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Введите оценку отзыва от 1 до 5'
        })

        self.fields['text'].label = 'Ваш отзыв'

        self.fields['stars'].label = 'Ваша оценка'



class StoreCreateForm(forms.ModelForm):

    class Meta:

        model = MarketShop

        fields = ['name','image','description',]


    def __init__(self,*args, **kwargs):

        super(StoreCreateForm,self).__init__(*args, **kwargs)


        self.fields['description'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Придумайте описание своего магазина'
        })

        self.fields['description'].label = 'Например-магазин по продаже запчастей для автомобилей Mercedes-Benz'

        

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product

        fields = ['store', 'category', 'name', 'slug', 
                  'description', 'price', 'available']
        


ImageByproductFormAddProduct = inlineformset_factory(
    Product,
    ImageByproduct,
    fields=['image'],
    extra=1,
    can_delete=True
)