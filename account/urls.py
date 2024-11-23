from django.urls import path,include
from django.contrib.auth.views import LogoutView
from . import views




urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('register/',views.user_registration,name='register'),
    path('user-detail/<username>/',views.user_detail,name='user_detail'),
    path('profile/',views.dashboard,name='profile'),
    path('profile-edit/',views.profile_edit,name='profile_edit'),
    path('logged-out/',LogoutView.as_view(template_name='registration/loggedd_out.html'),name='logout')
]
