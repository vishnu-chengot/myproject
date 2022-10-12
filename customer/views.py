from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'customer/home.html')

def change_password(request):
    return render(request,'customer/change password.html')

def checkout(request):
    return render(request,'customer/checkout.html')

def my_cart(request):
    return render(request,'customer/my cart.html')

def my_order(request):
    return render(request,'customer/my order.html')

def product_details(request):
    return render(request,'customer/product details.html')

def profile(request):
    return render(request,'customer/profile.html')