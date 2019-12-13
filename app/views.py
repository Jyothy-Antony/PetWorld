from django.shortcuts import render
from app.models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
import smtplib
from datetime import timedelta
from datetime import datetime
from django.utils.dateformat import DateFormat
from django.utils.formats import get_format

# Create your views here.url(r'^demoapp','app/demoapp',name='demoapp'),

app_name = 'app'
def demoapp(request):
    pet=tbpets.objects.all()
    for i in pet:
        dob=datetime.strptime(i.dob,'%Y-%m-%d')
        vaccdat=datetime.strptime(i.Vdate,'%Y-%m-%d')
        dt = datetime.now()
        df = DateFormat(dt)
        date=df.format('d-m-Y')
        nowdate=datetime.strptime(date,'%d-%m-%Y')
        balance=nowdate-dob
        mm=balance/365
        i.age=mm.days
        nan=vaccdat-nowdate
        i.bal=nan.days
        i.save()
    try:
        myid=request.session['userid']
    except:
        try:
            myid=request.session['trainerid']
        except:
            try:
                myid=request.session['boardingid']
            except:
                return render(request,'app/demoapp.html',{})
    if myid:
        cartc=tbcart.objects.filter(userid=myid).count()
        data=tbboarlog.objects.get(id=myid)
        return render(request,'app/demoapp.html',{'cartc':cartc,'data':data})
    return render(request,'app/demoapp.html',{})

def about(request):
    try:
        myid=request.session['userid']
    except:
        try:
            myid=request.session['trainerid']
        except:
            try:
                myid=request.session['boardingid']
            except:
                return render(request,'app/about.html',{})
    if myid:
        data=tbboarlog.objects.get(id=myid)
        cartc=tbcart.objects.filter(userid=myid).count()
    return render(request,'app/about.html',{'cartc':cartc,'data':data})




def nvacc(request,id):
    if request.method=="POST":
        nvaccd=request.POST.get('nvacc')
        vaccdat=datetime.strptime(nvaccd,'%Y-%m-%d')
        data=tbpets.objects.get(id=id)
        data.Vdate=vaccdat
        data.save()
        return HttpResponseRedirect(reverse('app:demoapp'))


def blog(request):
    try:
        myid=request.session['userid']
    except:
        try:
            myid=request.session['trainerid']
        except:
            try:
                myid=request.session['boardingid']
            except:
                return render(request,'app/blog.html',{})
    if myid:
        data=tbboarlog.objects.get(id=myid)
        cartc=tbcart.objects.filter(userid=myid).count()
    return render(request,'app/blog.html',{'cartc':cartc,'data':data})

def contact(request):
    try:
        myid=request.session['userid']
    except:
        try:
            myid=request.session['trainerid']
        except:
            try:
                myid=request.session['boardingid']
            except:
                return render(request,'app/contact.html',{})
    if myid:
        data=tbboarlog.objects.get(id=myid)
        cartc=tbcart.objects.filter(userid=myid).count()
    return render(request,'app/contact.html',{'cartc':cartc,'data':data})

def shopping(request):
    data1=tbshoping.objects.all()
    try:
        myid=request.session['userid']
    except:
        try:
            myid=request.session['trainerid']
        except:
            try:
                myid=request.session['boardingid']
            except:
                return render(request,'app/shopping.html',{'data1':data1})
    if myid:
        data=tbboarlog.objects.get(id=myid)
        cartc=tbcart.objects.filter(userid=myid).count()
    return render(request,'app/shopping.html',{'cartc':cartc,'data':data,'data1':data1})

def fullshoppy(request):
    try:
        myid=request.session['userid']
    except:
        try:
            myid=request.session['trainerid']
        except:
            try:
                myid=request.session['boardingid']
            except:
                return HttpResponseRedirect(reverse('app:Ulogin'))
    else:
        return HttpResponseRedirect(reverse('app:Ulogin'))

def reg(request):
    if request.method=="POST":
        Username =request.POST.get('username')
        password =request.POST.get('password')
        Email =request.POST.get('email')
        Phone =request.POST.get('phone')
        Experience =request.POST.get('exp')
        Company =request.POST.get('compname')
        usertype= request.POST.get('usertype')
        data=tbboarlog.objects.create(usertype=usertype,username=Username,password=password,email=Email,phone=Phone,exp=Experience,compname=Company,approve="dissapprove")
        data2=tblogin.objects.create(username=Email,password=password,usertype=usertype)
    return render(request,'app/reg.html',{})

def Ulogin(request):
    if request.method=="POST":
        Username =request.POST.get('username')
        password =request.POST.get('password')
        usertype2 =request.POST.get('usertype')
        if tblogin.objects.filter(username=Username,password=password):
            data=tblogin.objects.get(username=Username,password=password)
            if data.usertype=="admin":
                request.session['adminid']=data.id
                return HttpResponseRedirect(reverse('adminapp:demoadmin'))
            if data.usertype=="user":
                data1=tbboarlog.objects.get(email=Username,password=password)
                request.session['userid']=data1.id
                return HttpResponseRedirect(reverse('userapp:demouser'))
            if data.usertype=="trainer":
                data1=tbboarlog.objects.get(email=Username,password=password)
                request.session['trainerid']=data1.id
                return HttpResponseRedirect(reverse('trainerapp:demotrainer'))
            if data.usertype=="boarding":
                data1=tbboarlog.objects.get(email=Username,password=password)
                request.session['boardingid']=data1.id
                return HttpResponseRedirect(reverse('boardingapp:demoboarding'))    
    return render(request,'app/Ulogin.html',{})

def logout(request):
    request.session.flush()
    return HttpResponseRedirect(reverse('app:demoapp'))

def SingleView(request,id):
    data1=tbshoping.objects.get(id=id)
    try:
        myid=request.session['userid']
    except:
        try:
            myid=request.session['trainerid']
        except:
            try:
                myid=request.session['boardingid']
            except:
                return render(request,'app/SingleView.html',{'data1':data1})
    if myid:
        data=tbboarlog.objects.get(id=myid)
        cartc=tbcart.objects.filter(userid=myid).count()
    return render(request,'app/SingleView.html',{'cartc':cartc,'data':data,'data1':data1})

def cart(request):
    cartc=""
    try:
        myid=request.session['userid']
    except:
        try:
            myid=request.session['trainerid']
        except:
            try:
                myid=request.session['boardingid']
            except:
                return HttpResponseRedirect(reverse('app:Ulogin'))
    if myid:  
        if request.method=="POST":  
            itemid=request.POST.get('itemid')
            qty=request.POST.get('quantity')
            data=tbshoping.objects.get(id=itemid)
            price=data.price
            total= int(price)*int(qty)
            data1=tbshoping.objects.get(id=itemid)
            data=tbboarlog.objects.get(id=myid)
            cartc=tbcart.objects.filter(userid=myid).count()
            if tbcart.objects.filter(itemid=itemid,userid=myid):
                incart=tbcart.objects.get(itemid=itemid,userid=myid)
                incart.qty=int(incart.qty)+int(qty)
                incart.total=int(incart.total)+total
                incart.save()
            else:
                incart=tbcart.objects.create(itemid=itemid,userid=myid,qty=qty,img="no image",price=price,total=total)
    return render(request,'app/SingleView.html',{'cartc':cartc,'data1':data1,'data':data})

#not tested yet

def buy(request,id):
    try:
        myid=request.session['userid']
    except:
        try:
            myid=request.session['trainerid']
        except:
            try:
                myid=request.session['boardingid']
            except:
                return HttpResponseRedirect(reverse('app:Ulogin'))
    if myid:
        cartc=tbcart.objects.filter(userid=myid).count()
        item=tbshoping.objects.get(id=id)
        userdata=tbboarlog.objects.get(id=myid)
        if request.method=="POST":
            qty=request.POST.get('qty')
            cvv=request.POST.get('cvv')
            cardno=request.POST.get('cardNumber')
            if tbatm.objects.filter(cvv=cvv,Atmno=cardno):
                atmdetails=tbatm.objects.get(cvv=cvv,Atmno=cardno)
                actaddress=request.POST.get('actaddress')
                month=request.POST.get('month')
                year1=request.POST.get('year')
                year=int(year1)
                price=item.price
                total=request.POST.get('price')
                amt=atmdetails.amt
                if atmdetails.amt < total:
                    err="sorry...pls check your act balance"
                    return render(request,'app/buy.html',{'cartc':cartc,'item':item,'userdata':userdata,'err':err})
                dt = datetime.now()
                df = DateFormat(dt)
                date=df.format('d-m-Y')
                yo=df.format('Y')
                mo=df.format('m')
                y=int(yo)
                quty=int(item.quty)-int(qty)
                if quty<0:
                    err="We have only " + item.quty + "left....sorry"
                    return render(request,'app/cartbuy.html',{'cartc':cartc,'item':item,'userdata':userdata,'err':err})
                if year < y:
                    err="Card Expired"
                    return render(request,'app/cartbuy.html',{'cartc':cartc,'item':item,'userdata':userdata,'err':err})
                else:
                    pay=tbpayment.objects.create(address=actaddress,userid=myid,date=date,item=item.item,itemid=id,qty=qty,price=price,total=total,payment='done')
                    item.quty=quty
                    item.save()
                    atmdetails.amt=int(amt)-int(total)
                    atmdetails.save()
                    succ="Payment Successfully completed"
                    return render(request,'app/buy.html',{'succ':succ})
            else:
                err="Not a valid card number"
                return render(request,'app/buy.html',{'cartc':cartc,'item':item,'userdata':userdata,'err':err})
    return render(request,'app/buy.html',{'cartc':cartc,'item':item,'userdata':userdata})

def cartview(request):
    try:
        myid=request.session['userid']
    except:
        try:
            myid=request.session['trainerid']
        except:
            try:
                myid=request.session['boardingid']
            except:
                return HttpResponseRedirect(reverse('app:Ulogin'))
    if myid:
        cartc=tbcart.objects.filter(userid=myid).count()
        data=tbboarlog.objects.get(id=myid)
        cartdata=tbcart.objects.filter(userid=myid)
        itemdata=tbshoping.objects.all()
        cartdata=tbcart.objects.filter(userid=myid)
        total=0
        for i in cartdata:
            total= total + int(i.total)
    return render(request,'app/cartview.html',{'cartc':cartc,'data':data,'cartdata':cartdata,'itemdata':itemdata,'total':total})

def addpetcato(request):
    return render(request,'app/addpetcato.html',{})

def backtouser(request):
    try:
        myid=request.session['userid']
        return HttpResponseRedirect(reverse('userapp:demouser'))
    except:
        try:
            myid=request.session['trainerid']
            return HttpResponseRedirect(reverse('trainerapp:demotrainer'))
        except:
            try:
                myid=request.session['boardingid']
                return HttpResponseRedirect(reverse('boardingapp:demoboarding'))
            except:
                return HttpResponseRedirect(reverse('app:Ulogin'))
#cart buy
#not correctly checked yet.............
def cartbuy(request):
    try:
        myid=request.session['userid']
    except:
        try:
            myid=request.session['trainerid']
        except:
            try:
                myid=request.session['boardingid']
            except:
                return HttpResponseRedirect(reverse('app:Ulogin'))
    if myid:
        cartc=tbcart.objects.filter(userid=myid).count()
        userdata=tbboarlog.objects.get(id=myid)
        cartdata=tbcart.objects.filter(userid=myid)
        total=0
        for i in cartdata:
            #all total of cart items 
            total= total + int(i.total)
#if post--------------------------------------------------------
        if request.method=="POST":
            actaddress=request.POST.get('actaddress')
            month=request.POST.get('month')
            year1=request.POST.get('year')
            cvv=request.POST.get('cvv')
            cardno=request.POST.get('cardNumber')
#check for the account------------------------------------------
            if tbatm.objects.filter(cvv=cvv,Atmno=cardno):
                year=int(year1)
                #atm details of user----------------------------
                atmdetails=tbatm.objects.get(cvv=cvv,Atmno=cardno)
                amt=int(atmdetails.amt)
                #checking user's a/c have money or not
                if amt < total:
                    err="sorry...pls check your act balance"
                    return render(request,'app/buy.html',{'cartc':cartc,'item':item,'userdata':userdata,'err':err})
                dt = datetime.now()
                df = DateFormat(dt)
                date=df.format('d-m-Y')
                yo=df.format('Y')
                mo=df.format('m')
                y=int(yo)
                for i in cartdata:
                    itemid=i.itemid
                    item=tbshoping.objects.get(id=itemid)
                    quty=int(item.quty)-int(i.qty)
                #----------------------------------------------    
                    if quty<0:
                        err="We have only " + item.quty + " left in " + item.item + " ....sorry"
                        return render(request,'app/buy.html',{'cartc':cartc,'item':item,'userdata':userdata,'err':err})
                if year < y:
                    err="Card Expired"
                    return render(request,'app/buy.html',{'cartc':cartc,'item':item,'userdata':userdata,'err':err})
                else:
                    for i in cartdata:
                        itemid=i.itemid
                        item=tbshoping.objects.get(id=itemid)
                        quty=int(item.quty)-int(i.qty)
                        item.quty=quty
                        item.save() 
                        price=int(item.price)
                        itemtotal=price*int(i.qty)
                        pay=tbpayment.objects.create(address=actaddress,userid=myid,date=date,item=item.item,itemid=itemid,qty=i.qty,price=price,total=itemtotal,payment='done')
                        i.delete()
                    atmdetails.amt=int(amt)-int(total)
                    atmdetails.save()
                    succ="Payment Successfully completed"
                    return render(request,'app/cartbuy.html',{'cartc':cartc,'succ':succ})
                #--------------------------------------------------------
            else:
                err="sorry...Please check your a/c number"
                return render(request,'app/cartbuy.html',{'cartc':cartc,'total':total,'userdata':userdata,'err':err})
        else:      
            return render(request,'app/cartbuy.html',{'cartc':cartc,'userdata':userdata,'total':total})

def userreg(request):
    if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        dob=request.POST.get('dob')
        address=request.POST.get('address')
        pincode=request.POST.get('pincode')
        propic=request.FILES['propic']
        place=request.POST.get('place')
        street=request.POST.get('street')
        landmark=request.POST.get('landmark')
        password =request.POST.get('password')
        email =request.POST.get('email')
        if tblogin.objects.filter(username=email):
            err="Somthing problem with your emailid,We have another user using this mailid"
            return render(request,'app/userreg.html',{'err':err})
        phone =request.POST.get('phone')
        usertype="user"
        approve='dissapprove'
        data=tbboarlog.objects.create(fname=fname,lname=lname,dob=dob,address=address,pincode=pincode,propic=propic,place=place,street=street,landmark=landmark,password=password,email=email,phone=phone,usertype=usertype,approve=approve)
        data2=tblogin.objects.create(username=email,password=password,usertype=usertype)
    return render(request,'app/userreg.html',{})

def trainereg(request):
    if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        dob=request.POST.get('dob')
        address=request.POST.get('address')
        pincode=request.POST.get('pincode')
        propic=request.FILES['propic']
        place=request.POST.get('place')
        street=request.POST.get('street')
        landmark=request.POST.get('landmark')
        desc=request.POST.get('desc')
        licno=request.POST.get('licno')
        contact=request.POST.get('contact')
        username =request.POST.get('username')
        password =request.POST.get('password')
        email =request.POST.get('email')
        if tblogin.objects.filter(username=email):
            err="Somthing problem with your emailid,We have another user using this mailid"
            return render(request,'app/trainereg.html',{'err':err})
        phone =request.POST.get('phone')
        exp =request.POST.get('exp')
        compname =request.POST.get('compname')
        usertype="trainer"
        approve='dissapprove'
        data=tbboarlog.objects.create(fname=fname,lname=lname,dob=dob,address=address,pincode=pincode,propic=propic,place=place,street=street,landmark=landmark,desc=desc,licno=licno,password =password,email =email,phone =phone,exp =exp,compname =compname,usertype=usertype,approve=approve) 
        data2=tblogin.objects.create(username=email,password=password,usertype=usertype)
    return render(request,'app/trainereg.html',{})

def boardreg(request):
    if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        dob=request.POST.get('dob')
        address=request.POST.get('address')
        pincode=request.POST.get('pincode')
        propic=request.FILES['propic']
        place=request.POST.get('place')
        street=request.POST.get('street')
        landmark=request.POST.get('landmark')
        desc=request.POST.get('desc')
        licno=request.POST.get('licno')
        contact=request.POST.get('contact')
        username =request.POST.get('username')
        password =request.POST.get('password')
        email =request.POST.get('email')
        if tblogin.objects.filter(username=email):
            err="Somthing problem with your emailid,We have another user using this mailid"
            return render(request,'app/boardreg.html',{'err':err})
        phone =request.POST.get('phone')
        exp =request.POST.get('exp')
        compname =request.POST.get('compname')
        usertype="boarding"
        approve='dissapprove'
        data=tbboarlog.objects.create(fname=fname,lname=lname,dob=dob,address=address,pincode=pincode,propic=propic,place=place,street=street,landmark=landmark,desc=desc,licno=licno,password =password,email =email,phone =phone,exp =exp,compname =compname,usertype=usertype,approve=approve) 
        data2=tblogin.objects.create(username=email,password=password,usertype=usertype)
    return render(request,'app/boardreg.html',{})

def monthlypay(request):
    oldtdate=""
    usertype=""
    if request.method=="POST":
        myid=request.POST.get('myid')
        name=request.POST.get("name")
        cardno=request.POST.get("cardno")
        cvv=request.POST.get("cvv")
        month=request.POST.get("month")
        year1=request.POST.get("year")
        payamt=20000
        data=tbboarlog.objects.get(id=myid)
        usertype=data.usertype
        bandt=tbBandTpay.objects.filter(hisid=myid)
        for i in bandt:
            oldtdate=i.todate
        oldtodate = datetime.strptime(oldtdate,'%d-%m-%Y') 
        dt = datetime.now()
        df = DateFormat(dt)
        date=df.format('d-m-Y')
        nowdate=datetime.strptime(date,'%d-%m-%Y')
        if oldtodate < nowdate: 
            mydate=nowdate
        else:
            mydate=oldtdate     
        if tbatm.objects.filter(cvv=cvv,Atmno=cardno):
            year=int(year1)
            #atm details of user----------------------------
            atmdetails=tbatm.objects.get(cvv=cvv,Atmno=cardno)
            amt=int(atmdetails.amt)
            #after 30 day 
            nowdate=datetime.strptime(mydate,'%d-%m-%Y')
            a = nowdate + timedelta(days=30)
            b=DateFormat(a)
            aft30day=b.format('d-m-Y')
            yo=df.format('Y')
            y=int(yo)
            if year < y:
                if usertype=="trainer":
                    return HttpResponseRedirect(reverse('trainerapp:demotrainer'))
                elif usertype=="trainer":
                    return HttpResponseRedirect(reverse('boardingapp:demoboarding'))
                else:
                    pass
            if amt < 1000:
                if usertype=="trainer":
                    return HttpResponseRedirect(reverse('trainerapp:demotrainer'))
                elif usertype=="trainer":
                    return HttpResponseRedirect(reverse('boardingapp:demoboarding'))
                else:
                    pass
            else:
                #payment place

                #amt need to be deducted from a/c
                atmdetails.data=amt-1000
                atmdetails.save()
                pay=tbpayment.objects.create(address=data.address,userid=myid,itemid=0,qty=0,date=date,item="monthlypay",price=payamt,total=payamt,payment="done")
                for i in bandt:
                    i.fromdate=date
                    i.todate=aft30day
                    #done or not
                    i.payment="done"
                    i.paymentid=pay.id
                    i.save()
    else:
        if usertype=="trainer":
            return HttpResponseRedirect(reverse('trainerapp:demotrainer'))
        elif usertype=="boarding":
            return HttpResponseRedirect(reverse('boardingapp:demoboarding'))
        else:
            return HttpResponseRedirect(reverse('app:demoapp'))
    return render(request,'app/success.html',{})

def feedback(request):
    if request.method=="POST":
        name=request.POST.get('name')
        contact=request.POST.get('contact')
        email=request.POST.get('email')
        feedback=request.POST.get('feedback')
        data=tbfeedback.objects.create(name=name,contact=contact,email=email,feedback=feedback)
    return render(request,'app/feedback.html',{})

def viewnotifications(request):
    data=tbnotifications.objects.all()
    return render(request,'app/viewnotifications.html',{'data':data})

def singleview(request,id):
    data=tbnotifications.objects.get(id=id)
    return render(request,'app/singleview.html',{'data':data})
def viewtrainer(request):
    data=tbboarlog.objects.filter(usertype='trainer',approve='Approve')
    return render(request,'app/viewtrainer.html',{'data':data})

def viewindtrainer(request,id):
    data1=""
    data=tbboarlog.objects.get(id=id)
    if media.objects.filter(addid=id):
        data1=media.objects.filter(addid=id)
    return render(request,'app/viewindtrainer.html',{'data':data,'data1':data1})

def viewborder(request):
    data=tbboarlog.objects.filter(usertype='boarding',approve='Approve')
    return render(request,'app/viewborder.html',{'data':data})

def viewindborder(request,id):
    data1=""
    data=tbboarlog.objects.get(id=id)
    if media.objects.filter(addid=id):
        data1=media.objects.filter(addid=id)
    return render(request,'app/viewindborder.html',{'data':data,'data1':data1})

def success(request):
    return render(request,'userapp/success.html',{})



