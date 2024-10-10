from django import forms

from .models import Rating



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