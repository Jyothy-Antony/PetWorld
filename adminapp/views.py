from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from app.models import *
from django.conf import settings
import smtplib
from datetime import timedelta
from datetime import datetime
from django.utils.dateformat import DateFormat
from django.utils.formats import get_format
# Create your views here.
app_name = 'adminapp'
def demoadmin(request):
    id=request.session['adminid']
    data=tblogin.objects.get(id=id)
    user=tbboarlog.objects.filter(usertype="user")
    trainer=tbboarlog.objects.filter(usertype="trainer")
    boarding=tbboarlog.objects.filter(usertype="boarding")
    return render(request,'adminapp/demoadmin.html',{'data':data,'user':user,'trainer':trainer,'boarding':boarding})

def login(request):
    if request.method=="POST":
        user=request.POST.get('username')
        password=request.POST.get('password')
        if tblogin.objects.filter(username=user,password=password):
            data=tblogin.objects.get(username=user,password=password)
            request.session['adminid']=data.id
            return HttpResponseRedirect(reverse('adminapp:demoadmin'))
    return render(request,'adminapp/login.html',{})

def usrdel(request,id):
    tb=tbboarlog.objects.filter(id=id).delete()
    return HttpResponseRedirect(reverse('adminapp:demoadmin'))

def tradel(request,id):
    tb=tbboarlog.objects.filter(id=id).delete()
    return HttpResponseRedirect(reverse,('adminapp:demoadmin'))

def Additem(request):
    catod=tbmycato.objects.all()
    if request.method=="POST":
        item=request.POST.get('item')
        cato=request.POST.get('cato')
        desc=request.POST.get('desc')
        quty=request.POST.get('quty')
        expdate=request.POST.get('expdate')
        price=request.POST.get('price')
        image=request.FILES['image']
        data1 = tbshoping.objects.create(item=item,cato=cato,desc=desc,quty=quty,expdate=expdate,price=price,image=image)
    data= tbshoping.objects.all()
    return render(request,'adminapp/Additem.html',{'data':data,'catod':catod})

def editAdditem(request,id):
    data= tbshoping.objects.get(id=id)
    catod=tbmycato.objects.all()
    if request.method=="POST":
        item=request.POST.get('item')
        cato=request.POST.get('cato')
        desc=request.POST.get('desc')
        quty=request.POST.get('quty')
        expdate=request.POST.get('expdate')
        price=request.POST.get('price')
        colour=request.POST.get('colour')
        data1 = tbshoping.objects.get(id=id)
        data1.item=item
        data1.cato=cato
        data1.desc=desc
        data1.quty=quty
        data1.expdate=expdate
        data1.price=price
        data1.colour=colour
        data1.save()
        return HttpResponseRedirect(reverse('adminapp:Additem'))
    return render(request,'adminapp/editAdditem.html',{'data':data,'catod':catod})

def boadel(request,id):
    tb=tbboarlog.objects.filter(id=id).delete()
    return HttpResponseRedirect(reverse,('adminapp:demoadmin'))

def home(request):
    return render(request,'app/home.html',{})

def ApproveT(request,id):
    tb=tbboarlog.objects.get(id=id)
    if tb.approve=='dissapprove':
        mail=smtplib.SMTP('smtp.mailgun.org',587)
        mail.ehlo()
        mail.starttls()
        mail.login(settings.EMAIL_HOST_USER,settings.EMAIL_HOST_PASSWORD)
        dt = datetime.now()
        df = DateFormat(dt)
        date=df.format('d-m-Y')
        a = dt + timedelta(days=30)
        b=DateFormat(a)
        todate=b.format('d-m-Y')
        body = "Breed \n  Hai " + tb.fname + " " + tb.lname + ",\nYou are approved as Trainer, it is free until " + todate + " After that u want to pay 1000 RS for a month"
        email=tb.email
        mail.sendmail(settings.EMAIL_HOST_USER,email,body)
        tb.approve="Approve"
        tbBandTpay.objects.create(hisid=id,fromdate=date,todate=todate,payment='done')
        tb.save()
    return HttpResponseRedirect(reverse('adminapp:demoadmin'))

def ApproveB(request,id):
    tb=tbboarlog.objects.get(id=id)
    if tb.approve=='dissapprove':
        mail=smtplib.SMTP('smtp.mailgun.org',587)
        mail.ehlo()
        mail.starttls()
        mail.login(settings.EMAIL_HOST_USER,settings.EMAIL_HOST_PASSWORD)
        dt = datetime.now()
        df = DateFormat(dt)
        date=df.format('d-m-Y')
        a = dt + timedelta(days=30)
        b=DateFormat(a)
        todate=b.format('d-m-Y')

        message= "Breed \n  Hai " + tb.fname + " " + tb.lname + ",\nYou are approved as Trainer, it is free until " + todate + " After that u want to pay 1000 RS for a month"
        email=tb.email
        mail.sendmail(settings.EMAIL_HOST_USER,email,message)
        tb.approve="Approve"

        data=tbBandTpay.objects.create(hisid=id,fromdate=date,todate=todate,payment='done')
        tb.save()
    return HttpResponseRedirect(reverse('adminapp:demoadmin'))

def addcato(request):
    if request.method=="POST":
        item=request.POST.get('cato')
        data1 = tbmycato.objects.create(cato=item)
    return render(request,'adminapp/addcato.html',{})

def addpetcato(request):
    petcato=tbpetcato.objects.all()
    if request.method=="POST":
        item=request.POST.get('cato')
        catoimg=request.FILES['catoimg']
        data1 = tbpetcato.objects.create(cato=item,petcatoimg=catoimg)
    return render(request,'adminapp/addpetcato.html',{'petcato':petcato})

def deletepetcato(request,id):
    data=tbpetcato.objects.get(id=id)
    data.delete()
    return HttpResponseRedirect(reverse,('adminapp:addpetcato'))

def viewshoppy(request):
    data=tbpayment.objects.all()
    userdata=tbboarlog.objects.all()
    dataitem=tbshoping.objects.all()
    return render(request,'adminapp/viewshoppy.html',{'data':data,'userdata':userdata,'dataitem':dataitem})

def admintrainer(request):
    data=tbboarlog.objects.filter(usertype='trainer',approve='Approve')
    return render(request,'adminapp/admintrainer.html',{'data':data})

def adminboarding(request):
    data=tbboarlog.objects.filter(usertype='boarding',approve='Approve')
    return render(request,'adminapp/adminboarding.html',{'data':data})

def addnotification(request):
    if request.method=="POST":
        name=request.POST.get('name')
        img=request.FILES['img']
        date=request.POST.get('date')
        desc=request.POST.get('desc')
        data1=tbnotifications.objects.create(name=name,img=img,date=date,desc=desc)
    data=tbnotifications.objects.all()
    return render(request,'adminapp/addnotification.html',{'data':data})

def viewfeedback(request):
    data=tbfeedback.objects.all()
    return render(request,'adminapp/viewfeedback.html',{'data':data})

