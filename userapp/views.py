from django.shortcuts import render
from app.models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
from django.utils.dateformat import DateFormat
from django.utils.formats import get_format
# Create your views here.url(r'^demouser','app/demouser',name='demouser'),
app_name = 'userapp'

def demouser(request):                   
    var="TraingRequestAccepted"
    notif=""
    
    full=tbboarlog.objects.all()
    userid=request.session['userid']
    mydata=tbboarlog.objects.get(id=userid)
    data=""
    nan="You can send your pet please"
    media=""
    dt = datetime.now()
    df = DateFormat(dt)
    date=df.format('d-m-Y')
    nowdate=datetime.strptime(date,'%d-%m-%Y')
    data1=tbboarlog.objects.all()
    if tbonuser.objects.filter(usersid=userid,status=nan):
        data=tbonuser.objects.filter(usersid=userid,status=nan,useracc="")

    if tbnoti.objects.filter(subject=var,recid=userid):
        notif=tbnoti.objects.filter(subject=var,recid=userid)
    if tbmedia.objects.filter(recvid=userid):
        media=tbmedia.objects.filter(recvid=userid)
    return render(request,'userapp/demouser.html',{'mydata':mydata,'full':full,'notif':notif,'data':data,'data1':data1,'media':media})

def usertrainer(request):
    userid=request.session['userid']
    mydata=tbboarlog.objects.get(id=userid)
    data=tbboarlog.objects.filter(usertype='trainer',approve='Approve')
    if tbpets.objects.filter(userid=userid):
        pets=tbpets.objects.filter(userid=userid)
        return render(request,'userapp/usertrainer.html',{'data':data,'pets':pets,'mydata':mydata})
    else:
        err="Add your pet"
        return render(request,'userapp/usertrainer.html',{'data':data,'err':err,'mydata':mydata})
    
def userboarding(request):
    userid=request.session['userid']
    mydata=tbboarlog.objects.get(id=userid)
    data=tbboarlog.objects.filter(usertype='boarding',approve='Approve')
    if tbpets.objects.filter(userid=userid):
        pets=tbpets.objects.filter(userid=userid)
        return render(request,'userapp/userboarding.html',{'data':data,'pets':pets,'mydata':mydata})
    else:
        err="Add your pet"
        return render(request,'userapp/userboarding.html',{'data':data,'err':err,'mydata':mydata})

def Addpets(request):
    userid=request.session['userid']
    mydata=tbboarlog.objects.get(id=userid)
    petcato=tbpetcato.objects.all()
    pets=tbpets.objects.filter(userid=userid)
    if request.method=="POST":
        gender=request.POST.get('gender')
        age=request.POST.get('age')
        #next vaccination date 
        Vdate=request.POST.get('Vdate')
        dob=request.POST.get('dob')
        vname=request.POST.get('vaccname')
        #--------------------------------------------------------
        name=request.POST.get('name')
        cato=request.POST.get('cato')
        desc=request.POST.get('desc')
        doc=request.FILES['doc']
        photo=request.FILES['photo']
        pet=tbpets.objects.create(vname=vname,dob=dob,userid=userid,name=name,cato=cato,desc=desc,doc=doc,photo=photo,gender=gender,age=age,Vdate=Vdate)
    return render(request,'userapp/Addpets.html',{'petcato':petcato,'pets':pets,'mydata':mydata})

def bfull(request,id):
    data=tbboarlog.objects.get(id=id)
    
    data2=""
    userid=request.session['userid']
    mydata=tbboarlog.objects.get(id=userid)
    if tbamount.objects.filter(boardingid=id):
        data2=tbamount.objects.filter(boardingid=id)
    if tbpets.objects.filter(userid=userid):
        pets=tbpets.objects.filter(userid=userid)
        if data.usertype=="trainer":
            return render(request,'userapp/tfull.html',{'data12':data,'pets':pets,'mydata':mydata})
        return render(request,'userapp/bfull.html',{'data12':data,'pets':pets,'data2':data2,'mydata':mydata})
    return render(request,'userapp/bfull.html',{'data12':data,'mydata':mydata})

def tfull(request,id):
    data=tbboarlog.objects.get(id=id)
    userid=request.session['userid']
    mydata=tbboarlog.objects.get(id=userid)
    if tbpets.objects.filter(userid=userid):
        pets=tbpets.objects.filter(userid=userid)
        return render(request,'userapp/tfull.html',{'data12':data,'pets':pets,'mydata':mydata})
    return render(request,'userapp/tfull.html',{'data12':data,'mydata':mydata})

def userbreg(request):
    userid=request.session['userid']
    if tbpets.objects.filter(userid=userid):
        pets=tbpets.objects.filter(userid=userid)
        if request.method=="POST":
            mat=request.POST.get('matter')
            dogid=request.POST.get('arg1')
            boardingid=request.POST.get('boardingid')
            dt = datetime.now()
            df = DateFormat(dt)
            date=df.format('d-m-Y')
            sub="BoardingRequest"
            status=""
            seen=""
            data1=tbnoti.objects.create(sentid=userid,recid=boardingid,date=date,subject=sub,mater=mat,status=status,seend=seen,arg1=dogid)
    return HttpResponseRedirect(reverse('userapp:userboarding'))

def usertreg(request):
    userid=request.session['userid']
    if tbpets.objects.filter(userid=userid):
        pets=tbpets.objects.filter(userid=userid)
        if request.method=="POST":
            mat=request.POST.get('matter')
            dogid=request.POST.get('arg1')
            trainerid=request.POST.get('trainerid')
            dt = datetime.now()
            df = DateFormat(dt)
            date=df.format('d-m-Y')
            sub="TraingRequest"
            status=""
            seen=""
            data1=tbnoti.objects.create(sentid=userid,recid=trainerid,date=date,subject=sub,mater=mat,status=status,seend=seen,arg1=dogid)
    
    else:
        return HttpResponseRedirect('app:Ulogin')
    return HttpResponseRedirect(reverse('userapp:usertrainer'))

def cancelreq(request):

    return HttpResponseRedirect(reverse('userapp:demouser'))

def ok(request,id):
    data=tbonuser.objects.get(id=id)
    data.useracc="ok"
    dt = datetime.now()
    df = DateFormat(dt)
    date=df.format('d-m-Y')
    data.descriptions=data.descriptions + date + "User Selected trainer" + '/n'
    data.save()
    return HttpResponseRedirect(reverse('userapp:demouser'))

def temp(request):
    return render(request,'userapp/temp.html',{})

def mytrainer(request):
    userid=request.session['userid']
    mydata=tbboarlog.objects.get(id=userid)
    if tbpets.objects.filter(userid=userid):
        nan="You can send your pet please"
    if tbonuser.objects.filter(usersid=userid,status=nan):
        data=tbonuser.objects.filter(usersid=userid,status=nan)
        fulldata=tbboarlog.objects.all()
        return render(request,'userapp/mytrainer.html',{'data2':data,'fulldata':fulldata,'mydata':mydata})
    else:
        return render(request,'userapp/mytrainer.html',{'mydata':mydata})

def mypet(request):
    userid=request.session['userid']
    mydata=tbboarlog.objects.get(id=userid)
    data=tbpets.objects.filter(userid=userid)
    boardings=tbboarlog.objects.filter(usertype="boarding")
    trainers=tbboarlog.objects.filter(usertype="trainer")
    return render(request,'userapp/mypet.html',{'data':data,'mydata':mydata})

def chat(request,id):
    myid=request.session['userid']
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
        return render(request,'userapp/chat.html',{'recdata':recdata,'mydata':mydata})
    return render(request,'userapp/chat.html',{'myid':myid,'thid':thid,'chat':chat,'recdata':recdata,'mydata':mydata})

def mybordings(request):
    userid=request.session['userid']
    mydata=tbboarlog.objects.get(id=userid)
    nan="You can send your pet"
    if tbonuser.objects.filter(usersid=userid,status=nan):
        data=tbonuser.objects.filter(usersid=userid,status=nan)
        fulldata=tbboarlog.objects.all()
        return render(request,'userapp/mybordings.html',{'data2':data,'fulldata':fulldata,'mydata':mydata})
    else:
        return render(request,'userapp/mybordings.html',{'mydata':mydata})

def viewnoti(request):
    var="BorardingRequest"
    notif=""
    full=tbboarlog.objects.all()
    userid=request.session['userid']
    mydata=tbboarlog.objects.get(id=userid)
    data=""
    nan="You can send your pet"
    media=""
    dt = datetime.now()
    df = DateFormat(dt)
    date=df.format('d-m-Y')
    nowdate=datetime.strptime(date,'%d-%m-%Y')
    data1=tbboarlog.objects.all()
    if tbonuser.objects.filter(usersid=userid,status=nan):
        data=tbonuser.objects.filter(usersid=userid,status=nan,useracc="")
    if tbnoti.objects.filter(subject=var,recid=userid):
        notif=tbnoti.objects.filter(subject=var,recid=userid)
    return render(request,'userapp/viewnoti.html',{'mydata':mydata,'full':full,'notif':notif,'data':data,'data1':data1})

def chartview(request):
    data=""
    boarddata=tbboarlog.objects.all()
    userid=request.session['userid']
    mydata=tbboarlog.objects.get(id=userid)
    if chart.objects.filter(userid=userid):
        data=chart.objects.filter(userid=userid)
    return render(request,'userapp/chartview.html',{'data':data,'mydata':mydata,'boarddata':boarddata})


def monthpay(request,id):
    myid=request.session['userid']
    mydata=tbboarlog.objects.get(id=myid)
    data1=""
    if tbboarlog.objects.get(id=id):
        data1=tbboarlog.objects.get(id=id)
        recid=data1.id
    if request.method=="POST":
        name=request.POST.get("name")
        cardno=request.POST.get("card")
        cvv=request.POST.get("cvv")
        month=request.POST.get("month")
        year1=request.POST.get("year")
        userid=myid
        amount=request.POST.get('amount')
        if tbatm.objects.filter(cvv=cvv,Atmno=cardno):
            year=int(year1)
            #atm details of user----------------------------
            atmdetails=tbatm.objects.get(cvv=cvv,Atmno=cardno)
            amt=int(atmdetails.amt)
            atmdetails.data=amt-1000
            atmdetails.save()
            data=monthpayuser.objects.create(userid=userid,amount=amount,recid=recid,status="done")
            return HttpResponseRedirect(reverse('userapp:mytrainer'))
    return render(request,'userapp/monthpay.html',{'data1':data1,'mydata':mydata})

def monthpay1(request,id):
    myid=request.session['userid']
    mydata=tbboarlog.objects.get(id=myid)
    data1=""
    if tbboarlog.objects.get(id=id):
        data1=tbboarlog.objects.get(id=id)
        recid=data1.id
    if request.method=="POST":
        name=request.POST.get("name")
        cardno=request.POST.get("card")
        cvv=request.POST.get("cvv")
        month=request.POST.get("month")
        year1=request.POST.get("year")
        userid=myid
        amount=request.POST.get('amount')
        if tbatm.objects.filter(cvv=cvv,Atmno=cardno):
            year=int(year1)
            #atm details of user----------------------------
            atmdetails=tbatm.objects.get(cvv=cvv,Atmno=cardno)
            amt=int(atmdetails.amt)
            atmdetails.data=amt-1000
            atmdetails.save()
            data=monthpayuser.objects.create(userid=userid,amount=amount,recid=recid,status="done")
            return HttpResponseRedirect(reverse('userapp:mybordings'))
    return render(request,'userapp/monthpay1.html',{'data1':data1,'mydata':mydata})

    