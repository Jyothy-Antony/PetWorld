from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import *
import smtplib

urlpatterns = [
    url(r'^$',demoapp,name="demoapp"),
    url(r'^reg/$',reg,name="reg"),
    url(r'^Ulogin/$',Ulogin,name="Ulogin"),
    url(r'^logout/$',logout,name="logout"),
    url(r'^about/$',about,name="about"),
    url(r'^blog/$',blog,name="blog"),
    url(r'^contact/$',contact,name="contact"),
    url(r'^feedback/$',feedback,name="feedback"),
    url(r'^shopping/$',shopping,name="shopping"),
    url(r'^fullshoppy/$',fullshoppy,name="fullshoppy"),
    url(r'^SingleView/(?P<id>[0-9]+)$',SingleView,name="SingleView"),
    url(r'^cart/$',cart,name="cart"),
    url(r'^buy/(?P<id>[0-9]+)$',buy,name="buy"),
    url(r'^cartview/$',cartview,name="cartview"),
    url(r'^backtouser/$',backtouser,name="backtouser"),
    url(r'^cartbuy/$',cartbuy,name="cartbuy"),
    url(r'^userreg/$',userreg,name="userreg"),
    url(r'^boardreg/$',boardreg,name="boardreg"),
    url(r'^trainereg/$',trainereg,name="trainereg"),
    url(r'^monthlypay/$',monthlypay,name="monthlypay"),
    url(r'^viewnotifications/$',viewnotifications,name="viewnotifications"),
    url(r'^nvacc/(?P<id>[0-9]+)$',nvacc,name="nvacc"),
    url(r'^singleview/(?P<id>[0-9]+)$',singleview,name="singleview"),
    url(r'^viewtrainer/',viewtrainer,name="viewtrainer"),
    url(r'^viewindtrainer/(?P<id>[0-9]+)$',viewindtrainer,name="viewindtrainer"),
    url(r'^viewborder/',viewborder,name="viewborder"),
    url(r'^viewindborder/(?P<id>[0-9]+)$',viewindborder,name="viewindborder"),
    url(r'^success/$',success,name="success"),
]