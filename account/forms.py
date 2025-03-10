from django import forms 

from django.contrib.auth.models import User

from django.http import Http404

from phonenumber_field.formfields import PhoneNumberField

from .models import *


class UserRegistrationForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput,
                               required=True)

    password2 = forms.CharField(widget=forms.PasswordInput,
                                required=True)

    class Meta:

        model = User

        fields = ['username','first_name','last_name','email','phone_number']

    
    def clean_password2(self):

        cd = self.cleaned_data

        if cd['password'] != cd['password2']:

            raise forms.ValidationError('Пароль не совпадает')
        
        return cd['password2']
    
    
    def clean_email(self):
        data = self.cleaned_data["email"]

        if User.objects.filter(email=data).exists():

            raise forms.ValidationError('Данный email уже зарегстрирован')
        
        return data
    


class UserEditForm(forms.ModelForm):

    class Meta:

        model = User

        fields = ['username','first_name','last_name','email','phone_number']


    def clean_email(self):

        data = self.cleaned_data['email']

        qs = User.objects.exclude(id=self.instance.id).filter(email=data)

        if qs.exists():

            raise forms.ValidationError('Данный email уже используется')
        
        return data
        

    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите ваше имя'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите вашу фамилию'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите вашу электронную почту'})
        self.fields['phone_number'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите свой номер телефона'})

class ProfileEdit(forms.ModelForm):

    class Meta:

        model = Profile

        fields = ['image']


