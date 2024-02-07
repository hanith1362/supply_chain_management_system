from django.urls import path
from . import views
from .views import sales_form,LoginPage,LogoutPage,HomePage,seller

urlpatterns = [
    path('',sales_form,name='sales_form'),
    path('login/',LoginPage,name='login'),
    path('home/',HomePage,name='home'),
     path('logout/',LogoutPage,name='logout'),
     path('seller/',seller,name='seller'),
]