from django.db import models
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your models here.
class userdatabase(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=50, blank=True)
    profilephoto = models.ImageField(upload_to='profiles')
    def __str__(self):
        return self.name

class products(models.Model):
    productname = models.CharField(max_length=100)
    producttype = models.CharField(max_length=100)
    GENDER_CHOICES = [
        ('B', 'BOY'),
        ('G', 'GIRL'),
        ('C', 'COMMON'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    price = models.DecimalField(decimal_places=2, max_digits=7)
    offerprice = models.DecimalField(decimal_places=2, max_digits=7)
    description = models.TextField()
    dateposted = models.DateTimeField(auto_now_add=True)
    seller = models.ForeignKey('userdatabase', on_delete=models.CASCADE)
    productphoto1 = models.ImageField(upload_to='products')
    productphoto2 = models.ImageField(upload_to='products' ,blank=True)
    productphoto3 = models.ImageField(upload_to='products' ,blank=True)
    productphoto4 = models.ImageField(upload_to='products' ,blank=True)
    def __str__(self):
        return self.productname
    

class userprofile(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone = models.BigIntegerField()
    email =models.EmailField()
    password=models.CharField(max_length=50)
    def __str__(self):
        return self.firstname
    
class kart(models.Model):
    profileid=models.ForeignKey('userprofile',on_delete=models.CASCADE)
    productid=models.ForeignKey(products,on_delete=models.CASCADE)
    sellerid=models.ForeignKey(userdatabase,on_delete=models.CASCADE)
    productname=models.CharField(max_length=100)
    image=models.ImageField(upload_to="kart") 
    quantity=models.IntegerField(default=1)
    price=models.DecimalField(decimal_places=2,max_digits=7)
    size=models.CharField(max_length=10)
    total=models.DecimalField(decimal_places=2,max_digits=9)
    def __int__(self):
        return self.profileid
    
class wishlist(models.Model):
    profileid=models.ForeignKey('userprofile',on_delete=models.CASCADE)
    productid=models.ForeignKey(products,on_delete=models.CASCADE)
    def __int__(self):
        return self.profileid
            
class addressmodel(models.Model):
    profileid=models.ForeignKey('userprofile',on_delete=models.CASCADE)
    firstname =models.CharField(max_length=100)
    lastname =models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    postcode=models.IntegerField()
    phone=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    def __int__(self):
        return self.profileid
    
class order(models.Model):
    profileid=models.ForeignKey('userprofile',on_delete=models.CASCADE)
    productid=models.ForeignKey(products,on_delete=models.CASCADE)
    productname=models.CharField(max_length=100)
    image=models.ImageField(upload_to="order") 
    quantity=models.IntegerField(default=1)
    price=models.DecimalField(decimal_places=2,max_digits=7)
    size=models.CharField(max_length=10)
    total=models.DecimalField(decimal_places=2,max_digits=9)
    orderdate=models.CharField(max_length=100)
    packed=models.IntegerField(default=0)
    packeddate=models.CharField(max_length=100)
    delivered=models.IntegerField(default=0)
    delivereddate=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    address=models.ForeignKey(addressmodel,on_delete=models.CASCADE)
    sellerid=models.ForeignKey(userdatabase,on_delete=models.CASCADE)
    def __int__(self):
        return self.profileid

class cancelorder(models.Model):
    profileid=models.ForeignKey('userprofile',on_delete=models.CASCADE)
    productid=models.ForeignKey(products,on_delete=models.CASCADE)
    productname=models.CharField(max_length=100)
    image=models.ImageField(upload_to="cancel") 
    quantity=models.IntegerField(default=1)
    price=models.DecimalField(decimal_places=2,max_digits=7)
    size=models.CharField(max_length=10)
    total=models.DecimalField(decimal_places=2,max_digits=9)
    orderdate=models.CharField(max_length=100)
    packed=models.IntegerField(default=0)
    packeddate=models.CharField(max_length=100)
    delivered=models.IntegerField(default=0)
    delivereddate=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    address=models.ForeignKey(addressmodel,on_delete=models.CASCADE)
    sellerid=models.ForeignKey(userdatabase,on_delete=models.CASCADE)
    def __int__(self):
        return self.profileid


