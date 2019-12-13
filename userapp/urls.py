from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import *
#
urlpatterns = [
    url(r'^$',demouser,name="demouser"),
    url(r'^bfull/(?P<id>[0-9]+)$',bfull,name="bfull"),
    url(r'^tfull/(?P<id>[0-9]+)$',tfull,name="tfull"),
    url(r'^ok/(?P<id>[0-9]+)$',ok,name="ok"),
    url(r'^chat/(?P<id>[0-9]+)$',chat,name="chat"),
    url(r'^monthpay/(?P<id>[0-9]+)$',monthpay,name="monthpay"),
       url(r'^monthpay1/(?P<id>[0-9]+)$',monthpay1,name="monthpay1"),
    
    url(r'^Addpets/$',Addpets,name="Addpets"),
    url(r'^usertrainer/$',usertrainer,name="usertrainer"),
    url(r'^userboarding/$',userboarding,name="userboarding"),
    url(r'^userbreg/$',userbreg,name="userbreg"),
    url(r'^usertreg/$',usertreg,name="usertreg"),
    url(r'^cancelreq/$',cancelreq,name="cancelreq"),
     url(r'^mytrainer/$',mytrainer,name="mytrainer"),
      url(r'^mypet/$',mypet,name="mypet"),
      url(r'^mybordings/$',mybordings,name="mybordings"),
        url(r'^viewnoti/$',viewnoti,name="viewnoti"),
        url(r'^chartview/$',chartview,name="chartview"),
]
