from django import forms 

from django.contrib.auth.models import User
from django.http import Http404



class UserRegistrationForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput,
                               required=True)

    password2 = forms.CharField(widget=forms.PasswordInput,
                                required=True)

    class Meta:

        model = User

        fields = ['username','first_name','last_name','email']

    
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
    