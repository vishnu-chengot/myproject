from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'ecom_admin/home.html')

def approveseller(request):
    return render(request,'ecom_admin/approve seller.html')
   
def viewcustomer(request):
    return render(request,'ecom_admin/view customer.html')  

def viewseller(request):
    return render(request,'ecom_admin/view seller.html')    