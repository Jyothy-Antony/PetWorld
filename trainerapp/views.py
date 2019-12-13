from django.shortcuts import render
from app.models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
from django.utils.dateformat import DateFormat
from django.utils.formats import get_format
# dt = datetime.now()
# df = DateFormat(dt)
# date=df.format('d-m-Y')
# Create your views here.url(r'^demotrainer','app/demotrainer',name='demotrainer'),
app_name = 'trainerapp'
def demotrainer(request):
    trainerid=request.session['trainerid']
    full=tbboarlog.objects.all()
    mydata=tbboarlog.objects.get(id=trainerid)
    if tbBandTpay.objects.filter(hisid=trainerid):
        pay=tbBandTpay.objects.filter(hisid=trainerid)
        for i in pay:
            fromdate=i.fromdate
            todate=i.todate
            brid=i.id
            if i.payment=="need to pay":
                err="forgot to pay the bill........."
                return render(request,'trainerapp/demotrainer.html',{'err':err,'mydata':mydata})    
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
            return render(request,'trainerapp/demotrainer.html',{'err':err,'mydata':mydata})    
    var="TraingRequest"
    data=""
    c="Accept"
    handlers=""
    if tbnoti.objects.filter(subject=var,recid=trainerid):
        data=tbnoti.objects.filter(subject=var,recid=trainerid)
    if tbhandlers.objects.filter(tid=trainerid,assigments="not"):
        handlers=tbhandlers.objects.filter(tid=trainerid,assigments="not")  
    return render(request,'trainerapp/demotrainer.html',{'mydata':mydata,'data':data,'full':full,'c':c,'handlers':handlers})

def check(request,id):
    data=tbnoti.objects.get(id=id)
    data.status="Accept"
    data.seen="YES"
    userid=data.sentid
    data.save()
    petid=data.arg1
    trainerid=request.session['trainerid']
    if request.method=="POST":
        date=request.POST.get("date")
        dt = datetime.now()
        df = DateFormat(dt)
        datenow=df.format('d-m-Y')
        
        amount=request.POST.get('amount')
        duration=request.POST.get('duration')
        days=request.POST.get('days')
        handlerid=request.POST.get("handler")
        descriptions = datenow + " Trainer Accepted user Requested and Add requested user to deliver his dog on or befor " + date + '/n'
        data=tbonuser.objects.create(descriptions=descriptions,usersid=userid,petid=petid,varid=trainerid,date=date,status="You can send your pet please",handler=handlerid,amount=amount,days=days,duration=duration)
        
        handlers=tbhandlers.objects.get(name=handlerid)
        handlers.assigments="yes"
        handlers.dogid=petid
        handlers.save()
    return HttpResponseRedirect(reverse('trainerapp:demotrainer'))

def addhandlers(request):
    tid=request.session['trainerid']
    mydata=tbboarlog.objects.get(id=tid)
    if request.method=="POST":
        # tlicence=request.FILES['tlicence']
        photo=request.FILES['photo']
        name=request.POST.get('name')
        emailid=request.POST.get('emailid')
        phone=request.POST.get('phone')
        tid=request.session['trainerid']
        assigments="not"
        data=tbhandlers.objects.create(photo=photo,name=name,emailid=emailid,phone=phone,tid=tid,assigments=assigments)
    return render(request,'trainerapp/addhandlers.html',{'mydata':mydata})

def myhandlers(request):
    tid=request.session['trainerid']
    mydata=tbboarlog.objects.get(id=tid)
    data=""
    if tbhandlers.objects.filter(tid=tid):
        data=tbhandlers.objects.filter(tid=tid)
    return render(request,'trainerapp/handlers.html',{'data2':data,'mydata':mydata})

def handler(request,id):
    tid=request.session['trainerid']
    mydata=tbboarlog.objects.get(id=tid)
    data=tbhandlers.objects.get(id=id)
    return render(request,'trainerapp/handler.html',{'data2':data,'mydata':mydata})


def chat(request,id):
    myid=request.session['trainerid']
    mydata=tbboarlog.objects.get(id=myid)
    thid=int(id)
    recdata=tbboarlog.objects.get(id=id)
    if tbchat.objects.filter(resvid=myid,seen="not"):
        oldchat=tbchat.objects.filter(resvid=myid,seen="not")
        for i in oldchat:
            i.seen="yes"
            i.save()
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
        return render(request,'trainerapp/chat.html',{'recdata':recdata,'mydata':mydata})
    return render(request,'trainerapp/chat.html',{'myid':myid,'thid':thid,'chat':chat,'recdata':recdata,'mydata':mydata})

def petowners(request):
    trainerid=request.session['trainerid']
    mydata=tbboarlog.objects.get(id=trainerid)
    data=tbonuser.objects.filter(varid=trainerid)
    data1=tbboarlog.objects.all()
    return render(request,'trainerapp/petowners.html',{'data2':data,'udata':data1,'mydata':mydata})

def petowner(request,id):
    trainerid=request.session['trainerid']
    bdata=tbboarlog.objects.get(id=id)
    mydata=tbboarlog.objects.get(id=trainerid)
    return render(request,'trainerapp/petowner.html',{'bdata':bdata,'mydata':mydata})

def addmedia(request,id):
    trainerid=request.session['trainerid']
    mydata=tbboarlog.objects.get(id=trainerid)
    if request.method=="POST":
        vidimg=request.POST.get("vidimg")
        petid=request.POST.get("petid")
        for count ,x in enumerate(request.FILES.getlist("media")):
            data=tbmedia.objects.create(sendid=trainerid,recvid=id,vidimg=vidimg,media=x)
    return HttpResponseRedirect(reverse('trainerapp:petowners'))



def viewpets(request,id):
    myid=request.session["trainerid"]
    mydata=tbboarlog.objects.get(id=myid)
    data=tbpets.objects.filter(id=id)
    return render(request,'trainerapp/viewpets.html',{'data':data,'mydata':mydata})


def viewrequests(request,id):
    myid=request.session["trainerid"]
    mydata=tbboarlog.objects.get(id=myid)
    if tbnoti.objects.get(id=id):
        data2=tbnoti.objects.get(id=id)
        petid=data2.arg1
        data1=tbpets.objects.get(id=petid)
    return render(request,'trainerapp/viewrequests.html',{'data1':data1,'data2':data2,'mydata':mydata})

def addprofile(request):
    id=request.session["trainerid"]
    mydata=tbboarlog.objects.get(id=id)
    if request.method=="POST":
        vidimg=request.POST.get('vidimg')
        for count ,x in enumerate(request.FILES.getlist("media")):
            data=media.objects.create(addid=id,media=x,vidimg=vidimg)
    return render(request,'trainerapp/addprofile.html',{'mydata':mydata})
        
def reqdel(request,id):
    tb=tbnoti.objects.filter(id=id).delete()
    return HttpResponseRedirect(reverse('trainerapp:demotrainer'))

def viewpay(request):
    myid=request.session['trainerid']
    mydata=tbboarlog.objects.get(id=myid)
    data=tbboarlog.objects.all()
    if monthpayuser.objects.filter(recid=myid):
        data4=monthpayuser.objects.filter(recid=myid)
    return render(request,'trainerapp/viewpay.html',{'data4':data4,'data':data,'mydata':mydata})