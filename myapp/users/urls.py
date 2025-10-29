from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.users, name = 'users')
    # path('login/', include('django.contrib.auth.urls'))
]
