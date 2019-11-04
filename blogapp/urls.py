from django.conf.urls import url
from django.urls import path
from django.conf.urls import url
from . import views

print("inside app url")
urlpatterns = [

        url(r'^login/', views.Login.as_view(), name='login'),
        url(r'^email/$', views.Home.linkmail, name="email"),
        url(r'^comment/$', views.Comment.as_view(), name='comments'),
        url(r'^list/$' , views.Listitems.as_view(), name="list"),
        url(r'^detail/(?P<pk>\d+)$', views.Details.as_view(), name="details"),
        url(r'^about/$', views.About.as_view(), name='about'),
        url(r'^logout/$', views.Login.logout_view, name='logout'),
        url(r'^contact/$', views.ContactView.as_view(), name='contact'),
        url(r'^$', views.Home.as_view(), name='signup')
]
