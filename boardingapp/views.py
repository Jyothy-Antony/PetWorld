from django.shortcuts import render
from app.models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
from django.utils.dateformat import DateFormat
from django.utils.formats import get_format
# Create your views here.url(r'^demoboarding','app/demoboarding',name='demoboarding'),
app_name='boardingapp'
def demoboarding(request):
    data1=""
    boardingid=request.session['boardingid']
    mydata=tbboarlog.objects.get(id=boardingid)
    if tbBandTpay.objects.filter(hisid=boardingid):
        pay=tbBandTpay.objects.filter(hisid=boardingid)
        for i in pay:
            fromdate=i.fromdate
            todate=i.todate
            brid=i.id
            ch=i.payment
            if ch=="need to pay":
                err="forgot to pay the bill........."
                return render(request,'boardingapp/demoboarding.html',{'err':err,'mydata':mydata})    
        datef = datetime.strptime(fromdate,'%d-%m-%Y')
        datet = datetime.strptime(todate,'%d-%m-%Y')
        dt = datetime.now()
        df = DateFormat(dt)
        date=df.format('d-m-Y')
        nowdate=datetime.strptime(date,'%d-%m-%Y')
        if datet < nowdate:
            brdata=tbBandTpay.objects.get(id=brid)
            err="forgot to pay the bill........."
            brdata.payment="need to pay"
            brdata.save()
            return render(request,'boardingapp/demoboarding.html',{'err':err,'mydata':mydata})
   
    var="BoardingRequest"
    data=""
    full=tbboarlog.objects.all()
    if tbnoti.objects.filter(subject=var,recid=boardingid):
        data=tbnoti.objects.filter(subject=var,recid=boardingid)
        data1=tbboarlog.objects.all()
    return render(request,'boardingapp/demoboarding.html',{'mydata':mydata,'data':data,'full':full,'data1':data1})




def check(request,id):
    data=tbnoti.objects.get(id=id)
    data.status="Accept"
    data.seen="YES"
    userid=data.sentid
    data.save()
    recid=data.recid
    petid=data.arg1
    boardingid=request.session['boardingid']
    if request.method=="POST":
        date=request.POST.get("date")
        dt = datetime.now()
        df = DateFormat(dt)
        datenow=df.format('d-m-Y')
        amount=request.POST.get('amount')
        descriptions = datenow + " Bordings Accepted user Requested and Add requested user to deliver his/n"
        data1=tbonuser.objects.create(descriptions=descriptions,usersid=userid,petid=petid,varid=boardingid,date=date,status="You can send your pet",amount=amount,handler="",duration="",days="")
    return HttpResponseRedirect(reverse('boardingapp:demoboarding'))

def chat(request,id):
    myid=request.session['boardingid']
    mydata=tbboarlog.objects.get(id=myid)
    thid=int(id)
    if tbchat.objects.filter(resvid=myid,seen="not"):
        oldchat=tbchat.objects.filter(resvid=myid,seen="not")
        for i in oldchat:
            i.seen="yes"
            i.save()
    recdata=tbboarlog.objects.get(id=id)
    if request.method=="POST":
        msg=request.POST.get("msg")
        sentid=myid
        resvid=thid
        dt = datetime.now()
        df = DateFormat(dt)
        date=df.format('d-m-Y')
        time=df.format('H:i')
        seen="not"
        newchat=tbchat.objects.create(msg=msg,sendid=sentid,resvid=resvid,date=date,time=time,seen=seen)
    if tbchat.objects.filter(sendid=myid,resvid=thid) or tbchat.objects.filter(sendid=thid,resvid=myid):
        chat=tbchat.objects.all()
    else:
        return render(request,'boardingapp/chat.html',{'recdata':recdata})
    return render(request,'boardingapp/chat.html',{'myid':myid,'thid':thid,'chat':chat,'recdata':recdata,'mydata':mydata})

def petowners(request):
    boardingid=request.session['boardingid']
    mydata=tbboarlog.objects.get(id=boardingid)
    data=tbonuser.objects.filter(varid=boardingid)
    data1=tbboarlog.objects.all()
    return render(request,'boardingapp/petowners.html',{'data2':data,'udata':data1,'mydata':mydata})

def petowner(request,id):
    datadetail=""
    boardingid=request.session['boardingid']
    petdata=tbpets.objects.all()
    bdata=tbboarlog.objects.get(id=id)
    mydata=tbboarlog.objects.get(id=boardingid)
    userid=bdata.id
    amountdata=tbamount.objects.filter(boardingid=boardingid)
    if request.method=="POST":
        if tbonuser.objects.filter(usersid=userid):
            borid=mydata.id
            userid=bdata.id
            month=request.POST.get('month')
            vaccination=request.POST.get('vacc')
            vaccdate=request.POST.get('date')
            extra=request.POST.get('exp')
            monthpay=request.POST.get('monthpay')
            total=(int(extra)+int(monthpay))
            create=chart.objects.create(bordid=borid,userid=userid,vaccname=vaccination,cvdate=vaccdate,expense=extra,totalamount=total,month=month)  
    return render(request,'boardingapp/petowner.html',{'bdata':bdata,'mydata':mydata,'amountdata':amountdata})

def addmedia(request,id):
    boardingid=request.session['boardingid']
    mydata=tbboarlog.objects.get(id=boardingid)
    if request.method=="POST":
        vidimg=request.POST.get("vidimg")
        petid=request.POST.get("petid")
        for count ,x in enumerate(request.FILES.getlist("media")):
            data=tbmedia.objects.create(sendid=boardingid,recvid=id,vidimg=vidimg,media=x)
    return HttpResponseRedirect(reverse('boardingapp:petowners'))


def viewpets(request,id):
    boardingid=request.session['boardingid']
    mydata=tbboarlog.objects.get(id=boardingid)
    data=tbpets.objects.filter(id=id)
    return render(request,'boardingapp/viewpets.html',{'data':data,'mydata':mydata})

def viewrequests(request,id):
    boardingid=request.session['boardingid']
    mydata=tbboarlog.objects.get(id=boardingid)
    if tbnoti.objects.get(id=id):
        data2=tbnoti.objects.get(id=id)
        petid=data2.arg1
        data1=tbpets.objects.get(id=petid)
    return render(request,'boardingapp/viewrequests.html',{'data1':data1,'data2':data2,'mydata':mydata})

# def chart(request,id): 
#     borid=request.session["boardingid"]
#     bordata=tbboarlog.objects.get(id=borid)
#     return render(request,'boardingapp/chart.html',{})


def addamount(request):
    id=request.session["boardingid"]
    mydata=tbboarlog.objects.get(id=id)
    if request.method=="POST":
        breed=request.POST.get('breed')
        amount=request.POST.get('amount')
        data1=tbamount.objects.create(breed=breed,amount=amount,boardingid=id)
    data=tbamount.objects.filter(boardingid=id)
    return render(request,'boardingapp/addamount.html',{'data':data,'mydata':mydata})

def addprofile(request):
    id=request.session["boardingid"]
    mydata=tbboarlog.objects.get(id=id)
    if request.method=="POST":
        vidimg=request.POST.get('vidimg')
        for count ,x in enumerate(request.FILES.getlist("media")):
            data=media.objects.create(addid=id,media=x,vidimg=vidimg)
    return render(request,'boardingapp/addprofile.html',{'mydata':mydata})
        
def reqdel(request,id):
    tb=tbnoti.objects.filter(id=id).delete()
    return HttpResponseRedirect(reverse('boardingapp:demoboarding'))


def viewpay(request):
    myid=request.session['boardingid']
    mydata=tbboarlog.objects.get(id=myid)
    data=tbboarlog.objects.all()
    if monthpayuser.objects.filter(recid=myid):
        data4=monthpayuser.objects.filter(recid=myid)
    return render(request,'boardingapp/viewpay.html',{'data4':data4,'data':data,'mydata':mydata})