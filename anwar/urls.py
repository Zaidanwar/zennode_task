from django.urls import path,include
from anwar.views import *

urlpatterns = [

    path('',Home.as_view(),name="home"),
path('register/',Register.as_view(),name="register"),
path('login/',Log.as_view(),name="login"),
path('mainhome/',Mainhome.as_view(),name="mainhome"),
]