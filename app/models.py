from django.db import models

# Create your models here.
class tblogin(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    usertype=models.CharField(max_length=100)
    
class tbboarlog(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    dob=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    pincode=models.CharField(max_length=100)
    propic=models.ImageField(upload_to='Images/profile',verbose_name="file", null=True,blank=True)
    place=models.CharField(max_length=100)
    street=models.CharField(max_length=100)
    landmark=models.CharField(max_length=100)
    desc=models.CharField(max_length=1000)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    #type of users
    usertype=models.CharField(max_length=100)
    approve=models.CharField(max_length=100)
    exp=models.CharField(max_length=100)
    compname=models.CharField(max_length=100)
    licno=models.ImageField(upload_to='Images/licence',verbose_name="file", null=True,blank=True)
    contact=models.CharField(max_length=100)

class tbcontact(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    msg=models.CharField(max_length=1000)

class tbshoping(models.Model):
    item=models.CharField(max_length=100)
    cato=models.CharField(max_length=100)
    desc=models.CharField(max_length=100)
    quty=models.CharField(max_length=100)
    expdate=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
   
    image=models.ImageField(upload_to='Images/petdocs',verbose_name="file", null=True,blank=True)

class tbpets(models.Model):
    #owner name
    userid=models.IntegerField()
    name=models.CharField(max_length=100)
    cato=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    dob=models.CharField(max_length=100)
    age=models.CharField(max_length=100,null=True)
    desc=models.CharField(max_length=100)
    #vaccination date 
    vname=models.CharField(max_length=100)
    Vdate=models.CharField(max_length=100)
    doc=models.ImageField(upload_to='Images/petdocs',verbose_name="file", null=True,blank=True)
    photo=models.ImageField(upload_to='Images/pets',verbose_name="file", null=True,blank=True)

class tbnoti(models.Model):
    sentid=models.IntegerField()
    recid=models.IntegerField()
    date=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    mater=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    seend=models.CharField(max_length=100)
    arg1=models.CharField(max_length=100)
    arg2=models.CharField(max_length=100)
    arg3=models.CharField(max_length=100)

class tbmycato(models.Model):
    cato=models.CharField(max_length=100)
    
#all about selected users

    

class tbcart(models.Model):
    userid=models.IntegerField()
    itemid=models.IntegerField()
    qty=models.IntegerField()
    img=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    #buy or cato
    bandc=models.CharField(max_length=100)
    total=models.CharField(max_length=100)

#Pet cato- for eg :- rotwheeler
class tbpetcato(models.Model):
    cato=models.CharField(max_length=100)
    petcatoimg=models.ImageField(upload_to='Images/pettype',verbose_name="file", null=True,blank=True)


class tbonuser(models.Model):
    usersid=models.IntegerField()
    #assigned id
    varid=models.IntegerField()
    #assigned date
    date=models.CharField(max_length=100)
    petid=models.IntegerField()
    #date of reporting pets with trainesrs and boardings 
    repdate=models.CharField(max_length=100)
    #descriptions about pets
    descriptions=models.CharField(max_length=50000)
    #last updateation of descr desc 
    desclastupdate=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    #User Accept or not 
    useracc=models.CharField(max_length=100)
    #user date
    dateuseracc=models.CharField(max_length=100)
    handler=models.CharField(max_length=100)
    amount=models.CharField(max_length=100)
    duration=models.CharField(max_length=100)
    days=models.CharField(max_length=100)
class tbpayment(models.Model):
    #new address
    address=models.CharField(max_length=100)
    #full user details
    userid=models.IntegerField()
    #item id
    itemid=models.IntegerField()
    date=models.CharField(max_length=100)
    item=models.CharField(max_length=100)
    qty=models.IntegerField()
    #single item value
    price=models.CharField(max_length=100)
    total=models.CharField(max_length=100)
    #status payed or not payed
    payment=models.CharField(max_length=100)

class tbatm(models.Model):
    Atmno=models.CharField(max_length=14)
    amt=models.CharField(max_length=15)
    expm=models.CharField(max_length=2)
    expy=models.CharField(max_length=4)
    cvv=models.CharField(max_length=3)

#vaccination details
class tbvacc(models.Model):
    petid=models.CharField(max_length=14)
    vacdate=models.CharField(max_length=100)
    vacc=models.CharField(max_length=100)
    status=models.CharField(max_length=100)

class tbhandlers(models.Model):
    name=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='Images/licence',verbose_name="file", null=True,blank=True)
    #licence
    # tlicence=models.ImageField(upload_to='Images/licence',verbose_name="file", null=True,blank=True)
    emailid=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    #Dog assigned or not
    assigments=models.CharField(max_length=100)
    #asigned dogid
    dogid=models.CharField(max_length=100)
    #trinerid
    tid=models.CharField(max_length=100)

class tbchat(models.Model):
    msg=models.CharField(max_length=100)
    sendid=models.IntegerField()
    resvid=models.IntegerField()
    date=models.CharField(max_length=100)
    time=models.CharField(max_length=100)
    seen=models.CharField(max_length=10)

class tbmedia(models.Model):
    sendid=models.IntegerField()
    recvid=models.IntegerField()
    #video or image
    vidimg=models.CharField(max_length=100)
    media=models.ImageField(upload_to='Images/licence',verbose_name="file", null=True,blank=True)

class tbBandTpay(models.Model):
    #id of trainers or boardings
    hisid=models.IntegerField()
    fromdate=models.CharField(max_length=100)
    todate=models.CharField(max_length=100)
    #done or not
    payment=models.CharField(max_length=100)
    paymentid=models.IntegerField(null=True)

class tbfeedback(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    feedback=models.CharField(max_length=1000)
    contact=models.CharField(max_length=100)

class tbnotifications(models.Model):
    name=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    desc=models.CharField(max_length=100)
    img=models.ImageField(upload_to='Images/licence',verbose_name="file", null=True,blank=True)

class chart(models.Model):
    petid=models.IntegerField(null=True)
    userid=models.IntegerField()
    bordid=models.IntegerField()
    month=models.CharField(max_length=100)
    vaccname=models.CharField(max_length=100)
    cvdate=models.CharField(max_length=100)
    expense=models.CharField(max_length=100)
    totalamount=models.CharField(max_length=100)

class tbamount(models.Model):
    boardingid=models.IntegerField()
    breed=models.CharField(max_length=100)
    amount=models.CharField(max_length=100)


class media(models.Model):
    addid=models.IntegerField()
    vidimg=models.CharField(max_length=100)
    media=models.ImageField(upload_to='Images/licence',verbose_name="file", null=True,blank=True)


class monthpayuser(models.Model):
    userid=models.IntegerField()
    recid=models.IntegerField()
    amount=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
