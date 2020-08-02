from django.conf.urls import url
from django.urls import path
from ProjectTwo import views

urlpatterns = [
    path('', views.help, name='help'),
    path('', views.users, name='users'),
    path('', views.index, name='index')
]
