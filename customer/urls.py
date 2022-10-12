from django.urls import path
from. import views 

urlpatterns=[
 path('home',views.home),
 path('changepassword',views.change_password),
 path('checkout',views.checkout),
 path('mycart',views.my_cart),
 path('myorder',views.my_order),
 path('productdetails',views.product_details),
 path('profile',views.profile),
]
