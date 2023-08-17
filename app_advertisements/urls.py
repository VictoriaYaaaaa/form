from django.urls import path
from .views import *

urlpatterns=[
    path('index/',index, name='index'),
    path('top-sellers/',top_sellers, name='top-sellers'),
    path('advertisement-post/',advertisement_post,name='advertisement-post'),
    path('register/',register, name='register'),
    path('profile/',profile, name='profile'),
    path('login/',login, name='login')
]
