from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from .models import *
from django import utils
from django.conf import settings
from django.urls import reverse
from django.http import JsonResponse
import datetime

def justfun(request):
    return redirect(mainpage)

# kart lenght
lenkart=0
lenwish=0
#  user login view
userid=0
username=''
def mainpage(request):
    global userid


    #for know the length if the kart 
    a=kart.objects.filter(profileid_id=userid)
    list=[]
    for i in a:
        list+=[i.productid_id]
    global lenkart
    lenghts=len(list)
    lenkart=lenghts


    # for length of wishlist
    x=wishlist.objects.filter(profileid_id=userid)
    y=[]
    for i in x:
        y+=[i.productid_id]  
    
    global lenwish
    lenwish=len(y)


    
    a=userdatabase.objects.all()
    c=products.objects.all()
    global username
    w=wishlist.objects.all()
    b={'a1':a, 'c1':c,'lenght':lenghts,'username':username,'userid':userid,'lenwish':lenwish,'w':w,'y':y}
    return render(request,'home.html',b)  

def specific(request,ids):
    global userid
    global username
    global lenkart



    # for wishlist
    x=wishlist.objects.filter(profileid_id=userid)
    y=[]
    for i in x:
        y+=[i.productid_id]  
    global lenwish
    lenwish=len(y)
    

    a=userdatabase.objects.get(id=ids)
    c=products.objects.filter(seller_id=ids)
    product_count = c.count()
    b={'c1':c,'a1':a, 'product_count':product_count,'lenght':lenkart,'username':username,'userid':userid,'lenwish':lenwish,'y':y}
    return render(request,'specificbrand.html',b)

def genderBOY(request):
    global userid
    global username
    global lenkart


    # for wishlist
    x=wishlist.objects.filter(profileid_id=userid)
    y=[]
    for i in x:
        y+=[i.productid_id] 

    global lenwish
    lenwish=len(y) 


    a=products.objects.filter(gender__in=['B','C'])
    b={'a1':a,'lenght':lenkart,'username':username,'userid':userid,'lenwish':lenwish,'y':y}
    return render(request,'genderBOY.html',b)

def genderGIRL(request):
    global lenkart
    global userid
    global username


    # for wishlist
    x=wishlist.objects.filter(profileid_id=userid)
    y=[]
    for i in x:
        y+=[i.productid_id]  

    global lenwish
    lenwish=len(y) 

    a=products.objects.filter(gender__in=['C','G'])
    b={'a1':a,'lenght':lenkart,'username':username,'userid':userid,'lenwish':lenwish,'y':y}
    return render(request,'genderGIRL.html',b)

def genderCOMMON(request):
    global userid
    global username
    global lenkart

    # for wishlist
    x=wishlist.objects.filter(profileid_id=userid)
    y=[]
    for i in x:
        y+=[i.productid_id]  

    global lenwish
    lenwish=len(y) 

    a=products.objects.filter(gender='C')
    b={'a1':a,'lenght':lenkart,'username':username,'userid':userid,'lenwish':lenwish,'y':y}
    return render(request,'genderCOMMON.html',b)

def accorshoes(request,ids):
    global userid
    global username
    global lenkart

    # for wishlist
    x=wishlist.objects.filter(profileid_id=userid)
    y=[]
    for i in x:
        y+=[i.productid_id]  

    global lenwish
    lenwish=len(y) 

    c=ids
    a=products.objects.filter(producttype=ids)
    b={'a1':a, 'c1':c,'lenght':lenkart,'username':username,'userid':userid,'lenwish':lenwish,'y':y}
    return render(request,'accorshoes.html',b)

def product(request,ids):
    global userid
    global username
    global lenkart
    global lenwish
    a=products.objects.get(id=ids)
    brandname=a.seller_id
    k=userdatabase.objects.get(id=brandname)
    namea=k.name
    b={'a1':a,'v':namea,'lenght':lenkart,'username':username,'userid':userid,'lenwish':lenwish}  
    return render(request, "product.html",b) 

def karts(request):
    global userid
    global username
    global lenkart
    global lenwish
    a=kart.objects.filter(profileid=userid)
    list=[] 
    for i in a:
        list+=[i.productid_id]
    lenghts=len(list)
    global lenkart
    lenkart=lenghts

    # calculationg total
    sum = 0
    for j in a:
        sum=sum + j.total
    b={'a1':a, 'lenght':lenkart,'username':username,'userid':userid,'sum' : sum,'lenwish':lenwish }
    return render(request,'kart.html',b)



def kartsremove(request,ids):
    a=kart.objects.get(id=ids)
    a.delete()
    return redirect(karts)

def productdetails(request):
    global username
    if username == '':
        return redirect(userlogin)
    else :
        if request.method=="POST":
            global userid
            productid=request.POST['product_id']
            productname=request.POST['product_name']
            y=products.objects.get(id=productid)
            image=y.productphoto1
            productprice=request.POST['product_price']
            size=request.POST.get('size')
            if size == None:
                size=''
            qty=request.POST.get('qty')
            sellerid_id=request.POST.get('seller_id')
            total=int(qty)*float(productprice)
            if kart.objects.filter(productid_id=productid,size=size).exists():
                y=kart.objects.get(productid_id=productid,size=size)
                new_quantity=y.quantity+int(qty)
                new_price=new_quantity*float(productprice)
                z=kart.objects.filter(productid_id=productid,size=size).update(quantity=new_quantity,total=new_price)
            else:
                x=kart.objects.create(profileid_id=userid,productname=productname,image=image,productid_id=productid,price=productprice,size=size,quantity=qty,total=total,sellerid_id=sellerid_id)

        return redirect(karts)

def userlogin(request):
    if request.method=='POST':
        username1 = request.POST['username']
        password1 = request.POST['password']
        users=authenticate(username=username1,password=password1)
        if userprofile.objects.filter(email=username1,password=password1).exists():
            gets=userprofile.objects.get(email=username1,password=password1)
            id_gets=gets.id
            name_gets=gets.firstname
            global userid
            global username
            userid=id_gets
            username=name_gets
            return redirect(mainpage)
        elif users is not None and users.is_superuser==1:
            username='admin'
            return redirect(adminpage)
        elif userdatabase.objects.filter(email=username1,password=password1).exists():
            gets=userdatabase.objects.get(email=username1,password=password1)
            id_gets=gets.id
            name_gets=gets.name
            userid=id_gets
            username=name_gets
            return redirect(sellerpage)
        else:
            messages.error(request,"username or password  is incorrect")
            return redirect(userlogin)
    else:
        return render(request, 'login.html')

def usersignup(request):
    if request.method == 'POST':
        firstname1 = request.POST['firstname']
        lastname1 = request.POST['lastname']
        phone1 = request.POST['phone']
        email1 = request.POST['email']
        password1 = request.POST['password']
        conpassword1 = request.POST['conpassword']
        if password1 != conpassword1:
            messages.error(request,"Passwords Are Not Match")
            return redirect(usersignup)
        else:
            x=userprofile.objects.create(firstname=firstname1,lastname=lastname1,phone=phone1,email=email1,password=password1)
            return redirect(userlogin)
    else:
        return render(request,'signup.html')
    
def userlogout(request):
    global userid
    global username
    userid=0
    username=''
    return redirect(mainpage)

def whishlist(request):
    global userid
    global username
    global lenkart
    global lenwish
    if username == '':
        return redirect(userlogin)
    else :
        x=wishlist.objects.filter(profileid_id=userid)
        y=[]
        for i in x:
            y+=[i.productid_id]  

        lenwish=len(y)


        n=products.objects.filter(id__in=y)
        b={'username':username,'userid':userid,'a1':n,'lenwish':lenwish,'lenght':lenkart,'y':y}
        return render(request,'whishlist.html',b)

def wishlistadd(request,ids):
    global userid
    global username
    global lenkart
    global lenwish
    product_id=ids
    if username == '':
        return redirect(userlogin)
    else :
        x=wishlist.objects.create(profileid_id=userid,productid_id=product_id)
        return redirect(request.META.get('HTTP_REFERER'))
    

def wishlistremove(request,idn):
    global userid
    global username
    global lenkart
    global lenwish
    product_id=idn
    if username == '':
        return redirect(userlogin)
    else :
        x=wishlist.objects.get(profileid_id=userid,productid_id=product_id)
        x.delete()
        return redirect(request.META.get('HTTP_REFERER'))
    

# ADMIN PAGE START 

def adminpage(request):
    global username
    if username=='admin':
        x=userdatabase.objects.all()
        b={'c1':x}
        return render(request,'adminpage.html',b)
    else:
        return redirect(mainpage)
      
def addseller(request):
    global username
    if username=='admin':
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('pass')
            conform_password = request.POST.get('conpassword')
            logo_file = request.FILES.get('logo')
            if password !=conform_password:
                messages.error(request,"Passwords Are Not Match")
                return redirect(addseller)
            else:
                a=userdatabase.objects.create(name=name,email=email,password=password,profilephoto=logo_file)
                return redirect(adminpage)
        return render(request,'addseller.html')
    else:
        return redirect(mainpage)

def removeseller(request,ids):
    a=userdatabase.objects.get(id=ids)
    a.delete()
    return redirect(adminpage)


def sellerview(request,ids):
    global username
    if username=='admin':
        a=userdatabase.objects.get(id=ids)
        b={'c1':a}
        return render(request,'sellerview.html',b)

def selleredit(request,ids):
    global username
    if username=='admin':
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('pass')
            conform_password = request.POST.get('conpassword')
            logo_file = request.FILES.get('logo')
            if password !=conform_password:
                messages.error(request,"Passwords Are Not Match")
                return redirect(request.META.get('HTTP_REFERER'))
            else:
                a = userdatabase.objects.get(id=ids)
                a.name = name
                a.email = email
                a.password = password
                if logo_file:
                    a.profilephoto = logo_file
                a.save()
                return redirect(sellerview, ids=ids)
        else:
            a=userdatabase.objects.get(id=ids)
            b={'c1':a}
            return render(request,'selleredit.html',b)
        

# ADMIN PAGE ENDS
        

def sellerpage(request):
    global username
    global userid
    a=products.objects.filter(seller_id=userid)
    b={'c1':a,'username':username}
    return render(request,'sellerpage.html',b)

def productremove(request,ids):
    a=products.objects.get(id=ids)
    a.delete()
    return redirect(sellerpage)

def addproduct(request):
    global username
    global userid
    if username == '':
        return redirect(userlogin)
    else :
        if request.method == 'POST':
            productname = request.POST.get('productname')
            producttype = request.POST.get('producttype')
            gender = request.POST.get('gender')
            price = request.POST.get('price')
            offerprice = request.POST.get('offerprice')
            Description = request.POST.get('Description')
            productphoto1 = request.FILES.get('productphoto1')
            productphoto2 = request.FILES.get('productphoto2')
            productphoto3 = request.FILES.get('productphoto3')
            productphoto4 = request.FILES.get('productphoto4')
            X=products.objects.create(productname=productname,producttype=producttype,gender=gender,price=price,offerprice=offerprice,description=Description,seller_id=userid,productphoto1=productphoto1,productphoto2=productphoto2,productphoto3=productphoto3,productphoto4=productphoto4)
            X.save()
            return redirect(sellerpage)
        else:
            b={'username':username,'userid':userid}
            return render(request,'addproduct.html',b)
        
def viewproduct(request,uid):
    global username
    global userid
    if username == '':
        return redirect(userlogin)
    else :
        a=products.objects.get(id=uid)
        b={'c1':a,'username':username,'userid':userid}
        return render(request,'viewproduct.html',b)
        
def updateproduct(request,uid):
    global username
    global userid
    if username == '':
        return redirect(userlogin)
    else :
        if request.method == 'POST':
            productname = request.POST.get('productname')
            producttype = request.POST.get('producttype')
            gender = request.POST.get('gender')
            price = request.POST.get('price')
            offerprice = request.POST.get('offerprice')
            Description = request.POST.get('Description')
            productphoto1 = request.FILES.get('productphoto1')
            productphoto2 = request.FILES.get('productphoto2')
            productphoto3 = request.FILES.get('productphoto3')
            productphoto4 = request.FILES.get('productphoto4')
            a = products.objects.get(id=uid)
            a.productname=productname
            a.producttype=producttype
            a.gender=gender
            a.price=price
            a.offerprice=offerprice
            a.description=Description
            if productphoto1:
                a.productphoto1=productphoto1
            if productphoto2:
                a.productphoto2=productphoto2
            if productphoto3:
                a.productphoto3=productphoto3
            if productphoto4:
                a.productphoto4=productphoto4
            a.save()
            return redirect(viewproduct, uid=uid)
        else:
            a=products.objects.get(id=uid)
            b={'c1':a,'username':username,'userid':userid}
            return render(request,'updateproduct.html',b)

def addresspage(request):
    global username
    global userid
    global lenwish
    global lenkart
    if username == '':
        return redirect(userlogin)
    else :
        v=userprofile.objects.get(id=userid)
        c=addressmodel.objects.filter(profileid_id=userid)
        addresslen=0
        for i in c:
            addresslen=addresslen+1
        print(addresslen)
        b={'lenght':lenkart,'username':username,'userid':userid,'lenwish':lenwish,'v':v,'a1':c,'addresslen':addresslen}
        return render(request,'addresspage.html',b)

def addressremove(request,ids):
    global username
    global userid
    x=addressmodel.objects.get(profileid_id=userid)
    x.delete()
    return redirect(addresspage)

def addaddress(request):
    global username
    global userid
    global lenwish
    global lenkart
    if username == '':
        return redirect(userlogin)
    else :  
        if request.method == 'POST':
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            address1 = request.POST.get('address1')
            address2 = request.POST.get('address2')
            add=address1+","+address2
            city = request.POST.get('city')
            state = request.POST.get('state')
            postcode = request.POST.get('postcode')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            # if addressmodel.objects.filter(profileid_id=userid).exists():
            #     a=addressmodel.objects.filter(profileid_id=userid).update(profileid_id=userid,firstname=firstname,lastname=lastname,address=add,city=city,state=state,postcode=postcode,phone=phone,email=email)
            # else:
            a=addressmodel.objects.create(profileid_id=userid,firstname=firstname,lastname=lastname,address=add,city=city,state=state,postcode=postcode,phone=phone,email=email)
            a.save()
            return redirect(addresspage)
        
        else:
            b={'lenght':lenkart,'username':username,'userid':userid,'lenwish':lenwish} 
            return render(request,'addaddress.html',b)




def address(request,ids):
    global username
    global userid
    global lenwish
    global lenkart
    if username == '':
        return redirect(userlogin)
    else :
        if request.method == 'POST':
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            address1 = request.POST.get('address1')
            address2 = request.POST.get('address2')
            add=address1+","+address2
            city = request.POST.get('city')
            state = request.POST.get('state')
            postcode = request.POST.get('postcode')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            a=addressmodel.objects.filter(id=ids).update(firstname=firstname,lastname=lastname,address=add,city=city,state=state,postcode=postcode,phone=phone,email=email)
           
            # oderset
            c=kart.objects.filter(profileid_id=userid)
            for i in c:
                profileid_id=userid
                productid_id=i.productid_id
                productname=i.productname
                image=i.image
                quantity=i.quantity
                price=i.price
                size=i.size
                total=i.total
                orderdate=datetime.date.today()
                status='ordered'
                addressb=ids
                sellerid_id=i.sellerid_id
                s=order.objects.create(profileid_id=profileid_id,productid_id=productid_id,productname=productname,image=image,quantity=quantity,price=price,size=size,total=total,orderdate=orderdate,status=status,address_id=addressb,sellerid_id=sellerid_id)
                s.save()
                i.delete() 
            return redirect(mainpage)    
        else:
            a=addressmodel.objects.get(id=ids)
            x=kart.objects.filter(profileid_id=userid)
            sum = 0
            for j in x:
                sum =sum + j.total
            b={'username':username,'userid':userid,'lenwish':lenwish,'lenght':lenkart,'x':x,'sum':sum,'a':a}
            return render(request,'address.html',b)
        

def orderpage(request):
    global username
    global userid
    global lenwish
    global lenkart
    if username == '':
        return redirect(userlogin)
    else :
        x=order.objects.filter(profileid_id=userid)
        orderlen=0
        for i in x:
            orderlen=orderlen+1
        
        b={'username':username,'userid':userid,'lenwish':lenwish,'lenght':lenkart,'orderlen':orderlen,'a1':x}
        return render(request,'orderpage.html',b)
        
def specificorder(request,ids):
    global username
    global userid
    global lenwish
    global lenkart
    if username == '':
        return redirect(userlogin)
    else :
        x=order.objects.get(id=ids)
        m=x.address_id
        y=addressmodel.objects.get(profileid_id=userid,id=m)
        b={'username':username,'userid':userid,'lenwish':lenwish,'lenght':lenkart,'x':x,'y':y}
        return render(request,'specificorder.html',b)
    
def sellerorderpage(request):
    global username
    global userid
    if username == '':
        return redirect(userlogin)
    else :
        x=order.objects.filter(sellerid_id=userid,packed=0) 
        y=order.objects.filter(sellerid_id=userid,packed=1,delivered=0)
        z=order.objects.filter(sellerid_id=userid,delivered=1)
        u=cancelorder.objects.filter(sellerid_id=userid)
        lenpack=0
        for i in x:
            lenpack=lenpack+1 
        lendel=0
        for i in y:
            lendel=lendel+1
        lendd=0
        for i in z:
            lendd=lendd+1   
        lenca=0
        for i in u:
            lenca=lenca+1      
        b={'username':username,'userid':userid,'c1':x,'lenpack':lenpack,'y':y,'lendel':lendel,'lendd':lendd,'z':z,'lenca':lenca,'u':u}
        return render(request,'sellerorderpage.html',b)

def vieworderdetails(request,ids):
    global username
    global userid
    if username == '':
        return redirect(userlogin)
    else :
        x=order.objects.get(id=ids)
        add=x.address_id
        y=addressmodel.objects.get(id=add)
        b={'username':username,'userid':userid,'x':x,'y':y}
        return render(request,'vieworderdetails.html',b)
    

def setpacked(request,ids):
    daate=datetime.date.today()
    status='packed'
    x=order.objects.filter(id=ids).update(packed=1,packeddate=daate,status=status)
    return redirect(sellerorderpage)

def setdelivered(request,ids):
    daate=datetime.date.today()
    status='deleverd'
    x=order.objects.filter(id=ids).update(delivered=1,delivereddate=daate,status=status)
    return redirect(sellerorderpage)

def canceldelivery(requuest,ids):
    global username
    global userid
    x=order.objects.get(id=ids)
    profileid_id=x.profileid_id
    productid_id=x.productid_id
    productname=x.productname
    image=x.image
    quantity=x.quantity
    price=x.price
    size=x.size
    total=x.total
    orderdate=x.orderdate
    packed=x.packed
    packeddate=x.packeddate
    delivered=x.delivered
    delivereddate=x.delivereddate
    status=x.status
    address_id=x.address_id
    sellerid_id=x.sellerid_id
    y=cancelorder.objects.create(profileid_id=profileid_id,productid_id=productid_id,productname=productname,image=image,quantity=quantity,price=price,size=size,total=total,orderdate=orderdate,packed=packed,packeddate=packeddate,delivered=delivered,delivereddate=delivereddate,status=status,address_id=address_id,sellerid_id=sellerid_id)
    y.save()
    x.delete()
    return redirect(orderpage)








            


    




