from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from adminapp.views import *
from app.views import *
from boardingapp.views import *
from trainerapp.views import *
from userapp.views import *
#project.url.py
from django.urls import include
from django.conf.urls import url
from app.views import *
from adminapp.views import *
from trainerapp.views import *
from userapp.views import *
from boardingapp.views import *
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include('app.urls')),
    url(r'^adminapp/',include('adminapp.urls')),
    url(r'^trainerapp/',include('trainerapp.urls')),
    url(r'^userapp/',include('userapp.urls')),
    url(r'^boardingapp/',include('boardingapp.urls')),
]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
