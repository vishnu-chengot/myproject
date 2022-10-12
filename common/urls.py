from django.urls import path
from.import views
app_name='common'

urlpatterns=[
  path('adminlogin',views.admin_login,name='admin_sign'),
  path('customerlogin',views.customer_login,name='customer_sign'),
  path('customersignup',views.customer_signup,name='customer'),
  path('projecthome',views.project_home,name='home'),
  path('sellerlogin',views.seller_login,name='seller'),
  path('sellersignup',views.seller_signup,name='signin'),
]