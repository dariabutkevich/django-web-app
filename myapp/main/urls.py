from django.urls import path
from . import views
from .views import RegisterUser, LoginUser, logout_user

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('account', views.account, name='account'),
    path('contacts', views.contacts, name='contacts'),
    path('likes', views.likes, name='likes'),
    path('login', LoginUser.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
    path('register', RegisterUser.as_view(), name='register')
]
