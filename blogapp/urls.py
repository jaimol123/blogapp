from django.conf.urls import url
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.Home.as_view(), name='list'),
        url(r'^login/', views.Login.as_view(), name='login'),

]
