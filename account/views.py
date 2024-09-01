from django.shortcuts import render,get_object_or_404,redirect

from django.contrib.auth.decorators import login_required

from .forms import *

from .models import Profile

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

            new_user.set_password(form.cleaned_data['password'])

            new_user.save()

            Profile.objects.create(user=new_user)

            messages.success(
                request,
                'Вы успешно зарегестрировались и теперь можете авторизоваться'
            )

            return redirect('login')
        
        else:

            messages.error(request,'Произошла какая то ошибка')

    else:

        form = UserRegistrationForm()

    return render(
        request,
        'registration/register.html',
        {'form':form}
    )




@login_required
def user_detail(request,username):

    user = get_object_or_404(User,
                                    username=username,
                                    is_active=True)
    

    return render(
        request,
        'account/user/user_detail.html',
        {'user':user}
    )




@login_required
def profile_edit(request):

    if request.method == 'POST':

        user_form = UserEdit(data=request.PSOT,
                        instance=request.user)
        
        profile_form = ProfileEdit(data=request.POST,
                                   instance=request.user.profile
                                   ,
                                   files=request.FILES,)
        

        if user_form.is_valid() and profile_form.is_valid():

            user_form.save()

            profile_form.save()

            messages.success(request,'Данные вашего профиля успешно изменены!!!')

        else:

            messages.success(
                request,
                'При заполнении данных произошла ошибка'
            )

            return redirect('/')


    else:

        user_form = UserEdit(instance=request.user,
                             )
        
        profile_form = ProfileEdit(instance=request.user.profile)
        
    return render(
        request,
        'account/user/user_edit_form.html',
        {
            'profile_form':profile_form,
            'user_form':user_form
        }
    )
