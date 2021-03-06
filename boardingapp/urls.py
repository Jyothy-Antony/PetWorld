from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import *
#
urlpatterns = [
    url(r'^$',demoboarding,name="demoboarding"),
    url(r'^check/(?P<id>[0-9]+)$',check,name="check"),
    url(r'^chat/(?P<id>[0-9]+)$',chat,name="chat"),
    url(r'^petowners/$',petowners,name="petowners"),
    url(r'^petowner/(?P<id>[0-9]+)$',petowner,name="petowner"),
    url(r'^addmedia/(?P<id>[0-9]+)$',addmedia,name="addmedia"),
    url(r'^viewpets/(?P<id>[0-9]+)$',viewpets,name="viewpets"),
    url(r'^viewrequests/(?P<id>[0-9]+)$',viewrequests,name="viewrequests"),
    url(r'^reqdel/(?P<id>[0-9]+)$',reqdel,name="reqdel"),
   url(r'^addprofile/$',addprofile,name="addprofile"),
    url(r'^addamount/$',addamount,name="addamount"),
    url(r'^viewpay/$',viewpay,name="viewpay"),
]