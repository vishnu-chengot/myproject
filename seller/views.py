from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'seller/home.html')

def add_product(request):
    return render(request,'seller/add product.html')

def change_password(request):
    return render(request,'seller/change password.html')
  
def product_catalog(request):
    return render(request,'seller/product catalog.html')

def profile(request):
    return render(request,'seller/profile.html')

def update_stock(request):
    return render(request,'seller/update stock.html')