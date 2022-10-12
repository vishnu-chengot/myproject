from django.urls import path
from.import views 

urlpatterns=[
  path('home',views.home),
  path('addproduct',views.add_product),
  path('changepassword',views.change_password),
  path('productcatalog',views.product_catalog),
  path('profile',views.profile),
  path('updatestock',views.update_stock),
]