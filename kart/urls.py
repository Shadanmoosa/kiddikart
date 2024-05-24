from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.justfun),
    path('2',views.mainpage),

    # SPECIFIC BRAND
    path('specific/<int:ids>',views.specific),

    # GENDER
     path('boy',views.genderBOY),
     path('girl',views.genderGIRL),
     path('common',views.genderCOMMON),

     path('spec/<str:ids>',views.accorshoes),

    #  productdetails
    path('product/<int:ids>',views.product),

    # kart
    path('kart',views.karts),
    path('remove/<int:ids>',views.kartsremove),

    # product details
    path('20',views.productdetails),

    # address
    path('addresspage',views.addresspage),
    path('address/<int:ids>',views.address),
    path('addressremove/<int:ids>',views.addressremove),
    path('addaddress',views.addaddress),

    # orderpage
    path('orderpage',views.orderpage),
    path('specificorder/<int:ids>',views.specificorder),



    # logins
    path('login',views.userlogin),
    path('signup',views.usersignup),
    path('logout',views.userlogout),
    path('adminlogin',views.adminpage),
    path('addseller',views.addseller),
    path('removeseller/<int:ids>',views.removeseller),
    path('sellerview/<int:ids>',views.sellerview),
    path('selleredit/<int:ids>',views.selleredit),
                # sellerpage
    path('sellerpage',views.sellerpage),
    path('productremove/<int:ids>',views.productremove),
    path('addproduct',views.addproduct),
    path('viewproduct/<int:uid>',views.viewproduct),
    path('updateproduct/<int:uid>',views.updateproduct),
    path('sellerorderpage',views.sellerorderpage),
    path('vieworderdetails/<int:ids>',views.vieworderdetails),
    path('setpacked/<int:ids>',views.setpacked),
    path('setdelivered/<int:ids>',views.setdelivered),
    path('canceldelivery/<int:ids>',views.canceldelivery),


    # wishlist
    path('wishlist',views.whishlist),
    path('wishlistadd/<int:ids>',views.wishlistadd),
    path('wishlistremove/<int:idn>',views.wishlistremove),



     
    
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)