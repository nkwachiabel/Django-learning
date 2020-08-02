from django.conf.urls import url
from django.urls import path
from first_app import views

#TEMPLATE TAGGING

app_name = 'first_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.users, name='users'),
    path('forms/', views.form_name_view, name='form_name'),
    path('other/', views.other, name='other'),
    path('relative/', views.relative, name='relative'),
    path('index/', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
]
