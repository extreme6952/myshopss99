from django.urls import path

from . import views

app_name = 'coupone'


urlpatterns = [
    path('apply-coupone/',views.coupone_field,name='coupone_apply')
]
