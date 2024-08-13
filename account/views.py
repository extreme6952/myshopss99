from re import L
from django.shortcuts import render,get_object_or_404,redirect

from django.contrib.auth.decorators import login_required

from .forms import *

from django.contrib import messages


@login_required
def dashboard(request):

    return render(
        request,
        'account/user/dashboard.html'
    )


def user_registration(request):

    if request.method=='POST':

        form = UserRegistrationForm(data=request.POST)

        if form.is_valid():

            new_user = form.save(commit=False)

            new_user.set_password(new_user.cleaned_data['password'])

            new_user.save()

            messages.success(request,'Вы успешно прошли регистрацию')

            return render(
                'registration/login.html',
                {'new_user':new_user}
            )
        

    else:

        form = UserRegistrationForm()

    return render(
        request,
        'registrations/register.html',
        {'form':form}
    )