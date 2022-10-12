from django.urls import path
from . import views 

urlpatterns=[
  path('home',views.home),
  path('approveseller',views.approveseller),
  path('viewseller',views.viewseller),
  path('viewcustomer',views.viewcustomer),
]
