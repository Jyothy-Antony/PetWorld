from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import *
#adminapp
urlpatterns = [
    url(r'^addcato/$',addcato,name="addcato"),
    url(r'^demoadmin/$',demoadmin,name="demoadmin"),
    url(r'^$',login,name="login"),
    url(r'^usrdel/(?P<id>[0-9]+)$',usrdel,name="usrdel"),
    url(r'^tradel/(?P<id>[0-9]+)$',tradel,name="tradel"),
    url(r'^boadel/(?P<id>[0-9]+)$',boadel,name="boadel"),
    url(r'^home/$',home,name="home"),
    url(r'^ApproveT/(?P<id>[0-9]+)$',ApproveT,name="ApproveT"),
    url(r'^ApproveB/(?P<id>[0-9]+)$',ApproveB,name="ApproveB"),
    url(r'^Additem/$',Additem,name="Additem"),
    url(r'^editAdditem/(?P<id>[0-9]+)',editAdditem,name="editAdditem"),
    url(r'^addpetcato/$',addpetcato,name="addpetcato"),
    url(r'^deletepetcato/(?P<id>[0-9]+)$',deletepetcato,name="deletepetcato"),
    url(r'^viewshoppy/$',viewshoppy,name="viewshoppy"),
    url(r'^admintrainer$',admintrainer,name="admintrainer"),
    url(r'^adminboarding$',adminboarding,name="adminboarding"),
    url(r'^addnotification$',addnotification,name="addnotification"),
     url(r'^viewfeedback$',viewfeedback,name="viewfeedback"),
]