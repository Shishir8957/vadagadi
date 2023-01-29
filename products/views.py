from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Product,Booking
from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from datetime import datetime

# Create your views here.
def home(request):
    product = Product.objects.all().filter(booked=False)
    return render(request, 'productpage.html',{'products':product})

@login_required(login_url='/register')
def viewProduct(request,id):
    product = Product.objects.get(id=id)
    return render(request, 'viewproduct.html',{'products':product})

@login_required(login_url='/register')
def bookdate(request,pk):
    if request.method == "POST":
        starting = request.POST['starting']
        ending = request.POST['ending']
        pickuptime = request.POST['pickuptime']
        needDriver = request.POST.getlist('needDriver')
        starting = datetime.strptime(starting, "%b %d, %Y").date()
        ending = datetime.strptime(ending, "%b %d, %Y").date()

        if str(starting-ending) == '0:00:00':
            a = 0
        else:
            a= (str(starting-ending).split(" "))[0]
        time = datetime.strptime(pickuptime,'%I:%M %p').time()

        product = Product.objects.get(id=pk)
        product.booked=True
        product.save()
        user = request.user
        if len(needDriver):
            needDriver = True
        else:
            needDriver = False
        event = Booking.objects.create(name=user,starting=starting,ending=ending,pickupTime=time,total_days=a,cost_per_day=product.price,product=product,driverStatus=needDriver)
        event.save()
        
    return redirect('register')
